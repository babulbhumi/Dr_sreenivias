from flask import (
    Flask, render_template, request, jsonify,
    abort, redirect, url_for, session
)
import sqlite3, os, hashlib, urllib.parse
from datetime import datetime
from functools import wraps

# ─── THIS IS THE CRITICAL IMPORT ─────────────────────────────────
from services_data import SERVICES

# ─────────────────────────────────────────────────────────────────

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "drsreenivas-admin-secret-2025")

# ---------------------------------------------------------------------------
# Clinic-wide data
# ---------------------------------------------------------------------------
CLINIC = {
    "name": "Dr. Sreenivas Aesthetics",
    "tagline": "Sculpting Confidence. Redefining Beauty.",
    "phone": "095023 27644",
    "email": "drsreenivasaesthetics@gmail.com",
    "address": (
        "No 16/2/431, First Floor, Mini Bypass Road, above IDFC Bank, "
        "opposite Millineum Substation, Srinivasa Agraharam, "
        "Ramamurthy Nagar, Nellore, Andhra Pradesh 524001"
    ),
    "social": {
        "instagram": "https://www.instagram.com/drsreenivasaesthetics?igsh=NDFvdG1qdDl5dm56",
        "facebook": "https://www.facebook.com/share/1DTpxKeWMm/",
        "youtube": "https://youtube.com/@drsreenivasaesthetics?si=RlJ5WFxE4pwdP5Oa",
    },
}

# ---------------------------------------------------------------------------
# Doctor profiles
# ---------------------------------------------------------------------------
DOCTORS = [
    {
        "id": "dr-rao",
        "name": "Dr. Pavuluru Sreenivasa Rao",
        "title": "MS, MCh — Plastic & Reconstructive Surgery",
        "image": "dr_rao.jpg",
        "expertise_tags": [
            "Advanced Plastic & Cosmetic Surgery",
            "Reconstructive Microsurgery",
            "Complex Body Contouring",
            "Craniofacial Surgery",
            "Post-Bariatric Body Reshaping",
        ],
        "bio": (
            "With decades of surgical mastery, Dr. Rao is one of the region's "
            "most sought-after plastic surgeons. Holding an MCh in Plastic Surgery, "
            "his philosophy centres on natural, harmonious results achieved through "
            "cutting-edge technique and meticulous attention to detail. He leads "
            "complex reconstructive and cosmetic cases with equal expertise."
        ),
    },
    {
        "id": "dr-lakshmi",
        "name": "Dr. Veli Velli Jaswantha Lakshmi",
        "title": "MBBS · Diploma in Aesthetic Medicine · Certified PMU Artist",
        "credentials": "APMC / FMR / 104005",
        "image": "dr_lakshmi.jpg",
        "expertise_tags": [
            "Aesthetic Medicine & Injectables",
            "Permanent Makeup Artistry (PMU)",
            "Non-Surgical Facial Rejuvenation",
            "Skin Brightening & Pigmentation",
            "Botox, Fillers & Thread Lifts",
        ],
        "bio": (
            "Dr. Lakshmi seamlessly merges clinical precision with an artist's "
            "sensibility to deliver transformative yet understated aesthetic results. "
            "A certified PMU Artist registered under APMC (FMR / 104005), she is "
            "highly regarded for her mastery of injectables and non-surgical "
            "rejuvenation techniques."
        ),
    },
]

# ---------------------------------------------------------------------------
# Latest Blogs Data
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Latest Blogs Data (Now a Dictionary using { } instead of [ ])
#
LATEST_BLOGS = {
    "breast-reduction-surgery": {
        "slug": "breast-reduction-surgery",
        "title": "Everything You Need to Know About Breast Reduction Surgery",
        "date": "April 26, 2025",
        "image": "clinic-interior.jpg",  # Replace with actual image filename later
        "excerpt": "Struggling with large breasts? Learn how breast reduction surgery can alleviate chronic pain, improve posture, and restore your confidence.",
        "category": "Plastic Surgery",
        "content": """
            <p class="lead mb-4">Many people assume that having large breasts is a blessing, but in reality, it can lead to persistent discomfort, back and neck pain, and difficulty finding well-fitting clothes or supportive bras. If you’re experiencing these challenges, breast reduction surgery—also known as reduction mammoplasty—could provide a lasting solution.</p>

            <p>At Dr. Sreenivas Aesthetics Nellore, we specialize in advanced breast-reduction procedures that enhance not only your appearance but also your overall well-being.</p>

            <h3>What is Breast Reduction Surgery?</h3>
            <p>Breast reduction surgery, or reduction mammoplasty, is a surgical procedure designed to remove excess breast tissue, fat, and skin. This helps reshape the breasts, making them lighter, firmer, and more proportionate to your body frame.</p>
            <p>For many individuals, the surgery is not just about aesthetics—it’s a medical necessity. Oversized breasts can cause chronic pain, poor posture, and skin irritation due to excessive weight.</p>

            <h3>How Does Breast Reduction Surgery Work?</h3>
            <p>Unlike a mastectomy (which removes the entire breast), breast reduction surgery reduces size while preserving shape and natural contour. The procedure typically includes:</p>
            <ul>
                <li><strong>Tissue Reduction:</strong> Removal of excess fat and glandular tissue.</li>
                <li><strong>Breast Reshaping:</strong> Lifting and contouring the breasts for a youthful appearance.</li>
                <li><strong>Nipple Repositioning:</strong> Placing the nipple in a higher position to align with the new breast shape.</li>
            </ul>

            <h3>Key Benefits of Breast Reduction</h3>
            <div class="row mb-4">
                <div class="col-md-6">
                    <p><strong>✔️ Relief from Chronic Pain:</strong> Reduces strain on the back, neck, and shoulders.</p>
                    <p><strong>✔️ Improved Posture:</strong> Helps correct poor posture caused by heavy breasts.</p>
                </div>
                <div class="col-md-6">
                    <p><strong>✔️ Enhanced Mobility:</strong> Engage in physical activities like running and yoga with ease.</p>
                    <p><strong>✔️ More Clothing Options:</strong> Enjoy a wider selection of clothing and lingerie.</p>
                </div>
            </div>

            <div class="alert alert-info mt-4" style="background: var(--cream); border: 1px solid var(--gold-300); padding: 2rem;">
                <h4 class="text-navy" style="font-family: var(--font-display);">Transform Your Life at Dr. Sreenivas Aesthetics</h4>
                <p>If you’re struggling with the physical and emotional burden of large breasts, breast reduction surgery can be life-changing. Book a consultation today with Dr. Sreenivas, a leading plastic surgeon in Nellore, and take the first step toward a more comfortable and confident you!</p>
                <a href="/contact#book" class="btn btn-hero-primary mt-2">Book a Consultation Today</a>
            </div>
        """
    },
    "plastic-vs-cosmetic-surgery": {
        "slug": "plastic-vs-cosmetic-surgery",
        "title": "Plastic vs Cosmetic Surgery | Dr Sreenivas Nellore",
        "date": "April 12, 2025",
        "image": "clinic-interior.jpg",
        "excerpt": "Discover the key differences between plastic and cosmetic surgery, and learn which procedure is right for your functional or aesthetic goals.",
        "category": "Cosmetic Surgery",
        "content": """
            <p class="lead mb-4">At Dr. Sreenivas Aesthetics in Nellore, we believe in empowering individuals through both medical and aesthetic transformation. One of the most commonly misunderstood terms in this space is plastic surgery.</p>

            <p>Contrary to popular belief, plastic doesn’t refer to synthetic materials—it comes from the Greek word “plastikos”, meaning to mold or shape. Plastic surgery is a specialized medical field that focuses on repairing and reconstructing facial and body defects caused by trauma, birth disorders, diseases, or injury.</p>

            <h3>The Key Difference: Plastic Surgery vs. Cosmetic Surgery</h3>
            <p>While plastic and cosmetic surgeries often overlap, they are distinct specialties with unique purposes:</p>

            <h4>🔹 Plastic Surgery (Reconstructive)</h4>
            <p>Plastic surgery is reconstructive in nature. It is performed to repair functional impairments. The goal is to restore normal appearance and bodily function.</p>
            <ul>
                <li>Breast reconstruction post-mastectomy</li>
                <li>Cleft lip/palate repair</li>
                <li>Burn injury treatment</li>
                <li>Gender affirmation surgery</li>
            </ul>

            <h4>🔹 Cosmetic Surgery (Aesthetic)</h4>
            <p>Cosmetic surgery, on the other hand, is focused entirely on aesthetic enhancement. These procedures are elective and are done to improve symmetry, proportion, and beauty.</p>
            <ul>
                <li>Facelifts</li>
                <li>Liposuction</li>
                <li>Breast augmentation</li>
                <li>Rhinoplasty (nose reshaping)</li>
            </ul>

            <h3>Popular Cosmetic Surgery Procedures at Dr. Sreenivas Aesthetics:</h3>
            <ul style="list-style-type: none; padding-left: 0;">
                <li class="mb-2"><strong>✨ Breast Augmentation:</strong> Enhances breast size and volume using implants or fat transfer.</li>
                <li class="mb-2"><strong>✨ Liposuction:</strong> Removes stubborn fat from areas like the abdomen, thighs, arms, and chin for better contour.</li>
                <li class="mb-2"><strong>✨ Tummy Tuck (Abdominoplasty):</strong> Restores abdominal muscles and removes excess skin for a flat, firm belly.</li>
                <li class="mb-2"><strong>✨ Mommy Makeover:</strong> A combination of procedures tailored to reverse the effects of childbirth.</li>
                <li class="mb-2"><strong>✨ Botox & Dermal Fillers:</strong> Non-surgical treatments to smooth lines and add volume.</li>
            </ul>

            <div class="mt-5 text-center">
                <h4 style="font-family: var(--font-display); color: var(--navy-900);">Experience the Art of Transformation</h4>
                <p>At Dr. Sreenivas Aesthetics, we combine world-class expertise with compassionate care to offer safe, precise, and personalized plastic and cosmetic surgery solutions. Rediscover confidence. Reclaim your beauty.</p>
            </div>
        """
    },
    "best-cosmetic-surgeon-nellore": {
        "slug": "best-cosmetic-surgeon-nellore",
        "title": "Best Cosmetic Surgeon Near You Nellore: How to Choose the Right One",
        "date": "March 29, 2025",
        "image": "clinic-interior.jpg",
        "excerpt": "Choosing the right cosmetic surgeon is the most important decision in your aesthetic journey. Here are the top factors to consider when selecting a specialist in Nellore.",
        "category": "Cosmetic Surgery",
        "content": """
            <p class="lead mb-4">Undergoing a cosmetic or plastic surgery procedure is a life-changing decision. The most critical factor in ensuring a safe, beautiful, and natural-looking result is choosing the right surgeon.</p>

            <p>If you are searching for the best cosmetic surgeon in Nellore, you might feel overwhelmed by the options. Here is a comprehensive guide on exactly what to look for before making your choice.</p>

            <h3>1. Check Their Board Certification and Qualifications</h3>
            <p>Not every doctor who performs cosmetic procedures is a fully trained plastic surgeon. Always look for a surgeon who holds an advanced degree in Plastic and Reconstructive Surgery (such as an MCh). This guarantees they have undergone rigorous, specialized surgical training.</p>
            <p><em>Dr. Pavuluru Sreenivasa Rao holds an MS and an MCh in Plastic & Reconstructive Surgery, making him one of the most highly qualified specialists in the region.</em></p>

            <h3>2. Review Before-and-After Photos</h3>
            <p>A surgeon’s portfolio is their visual resume. Look closely at before-and-after photos of patients who have similar body types or facial structures to yours. Pay attention to the consistency of their results—do the outcomes look natural, or do they look "overdone"?</p>

            <h3>3. Prioritize Patient Safety and Facility Standards</h3>
            <p>The clinic or hospital where the surgery takes place is just as important as the surgeon. Ensure the facility is equipped with state-of-the-art technology, maintains strict hygiene protocols, and has emergency care capabilities.</p>

            <h3>4. Evaluate Their Approach to Consultations</h3>
            <p>A great cosmetic surgeon will never pressure you into a procedure. During your consultation, they should listen carefully to your goals, assess your anatomy, explain the risks, and offer an honest, realistic expectation of the results.</p>

            <div class="alert alert-info mt-4" style="background: var(--navy-950); color: var(--white); border: none; padding: 2rem; border-radius: var(--radius-md);">
                <h4 style="color: var(--gold-400); font-family: var(--font-display);">Why Choose Dr. Sreenivas Aesthetics?</h4>
                <p style="color: rgba(255,255,255,0.8);">With over 15 years of surgical excellence, our clinic is dedicated to delivering world-class aesthetic and reconstructive outcomes. We combine surgical precision with an artist's touch.</p>
            </div>
        """
    },
    "liposuction-vs-tummy-tuck": {
        "slug": "liposuction-vs-tummy-tuck",
        "title": "Liposuction vs. Tummy Tuck: Which is Right for You?",
        "date": "May 05, 2025",
        "image": "clinic-interior.jpg",  # Replace with actual image filename later
        "excerpt": "Struggling with a stubborn midsection? Discover the key differences between liposuction and an abdominoplasty to find out which procedure fits your goals.",
        "category": "Body Contouring",
        "content": """
            <p class="lead mb-4">Achieving a flat, toned midsection can be incredibly frustrating. Even with a strict diet and rigorous exercise routine, stubborn fat pockets and loose skin can refuse to budge. When this happens, patients in Nellore often ask Dr. Sreenivas: <em>"Do I need liposuction, or do I need a tummy tuck?"</em></p>

            <p>While both are highly effective body contouring procedures, they solve two completely different problems. Here is how to know which one is right for you.</p>

            <h3>Liposuction: The Fat Removal Specialist</h3>
            <p>Liposuction is designed exclusively to remove localized pockets of excess fat. At Dr. Sreenivas Aesthetics, we use advanced <strong>Power-Assisted Liposuction (PAL)</strong> to gently break up and permanently remove fat cells.</p>
            <ul>
                <li><strong>Best for:</strong> Patients who have good skin elasticity but stubborn fat bulges (like "love handles" or a belly pooch).</li>
                <li><strong>What it DOES NOT do:</strong> Liposuction cannot tighten loose skin or repair separated abdominal muscles.</li>
                <li><strong>Recovery:</strong> Relatively quick, usually requiring a few days of rest before returning to light activities.</li>
            </ul>

            <h3>Tummy Tuck (Abdominoplasty): The Complete Restoration</h3>
            <p>A tummy tuck is a more comprehensive surgical procedure. It removes excess fat, permanently cuts away sagging skin, and surgically tightens the underlying abdominal muscles that have been stretched out.</p>
            <ul>
                <li><strong>Best for:</strong> Women post-pregnancy, individuals who have lost a massive amount of weight, or anyone with a protruding abdomen due to muscle separation (diastasis recti).</li>
                <li><strong>What it DOES NOT do:</strong> It is not a weight-loss surgery. You should be close to your ideal weight before the procedure.</li>
                <li><strong>Recovery:</strong> Requires about 2 to 3 weeks of downtime to ensure the muscles heal properly.</li>
            </ul>

            <div class="alert alert-info mt-4" style="background: var(--cream); border: 1px solid var(--gold-300); padding: 2rem;">
                <h4 class="text-navy" style="font-family: var(--font-display);">Not Sure Which You Need?</h4>
                <p>During a private consultation, Dr. Sreenivas will assess your skin quality, muscle tone, and fat distribution to recommend the perfect procedure—or a combination of both! Contact us today to schedule your assessment.</p>
                <a href="/contact#book" class="btn btn-hero-primary mt-2">Book Your Consultation</a>
            </div>
        """
    },
    "non-surgical-facial-rejuvenation": {
        "slug": "non-surgical-facial-rejuvenation",
        "title": "The Ultimate Guide to Non-Surgical Facial Rejuvenation",
        "date": "May 15, 2025",
        "image": "clinic-interior.jpg",
        "excerpt": "Want to reverse the signs of aging without going under the knife? Learn how Botox, Dermal Fillers, and Aesthetic Medicine can refresh your appearance.",
        "category": "Aesthetic Medicine",
        "content": """
            <p class="lead mb-4">Aging is a privilege, but that doesn't mean you have to live with deep wrinkles, volume loss, or a tired appearance. Thanks to modern aesthetic medicine, you can achieve a refreshed, youthful glow without the downtime of traditional plastic surgery.</p>

            <p>Under the expert care of Dr. Veli Velli Jaswantha Lakshmi, our clinic offers world-class, non-surgical facial rejuvenation tailored to your unique anatomy.</p>

            <h3>1. Botox (Neuromodulators)</h3>
            <p>Botox is the gold standard for treating "dynamic" wrinkles—the lines formed by repeated facial expressions. By temporarily relaxing the underlying muscles, the skin above them smooths out.</p>
            <ul>
                <li><strong>Best used for:</strong> Forehead lines, crow's feet around the eyes, and the "11" lines between the eyebrows.</li>
                <li><strong>Results last:</strong> Typically 3 to 4 months.</li>
            </ul>

            <h3>2. Dermal Fillers (Hyaluronic Acid)</h3>
            <p>As we age, we naturally lose fat and bone density in our faces, leading to hollowing and sagging. Dermal fillers are injected to instantly restore lost volume, hydrate the skin, and contour the face.</p>
            <ul>
                <li><strong>Best used for:</strong> Plumping thinning lips, lifting sunken cheeks, softening smile lines (nasolabial folds), and contouring the jawline.</li>
                <li><strong>Results last:</strong> 6 to 18 months, depending on the product and treated area.</li>
            </ul>

            <h3>3. Permanent Makeup Artistry (PMU)</h3>
            <p>As a Certified PMU Artist, Dr. Lakshmi offers specialized semi-permanent enhancements to perfect your facial symmetry effortlessly.</p>
            <ul>
                <li><strong>Microblading / Powder Brows:</strong> Creates perfect, natural-looking eyebrows that frame the face and lift the eye area.</li>
                <li><strong>Lip Blushing:</strong> Restores youthful color and definition to the borders of the lips.</li>
            </ul>

            <h3>The "Liquid Facelift" Approach</h3>
            <p>Often, the best results come from combining these treatments. By strategically using Botox to smooth the upper face and Fillers to lift the lower face, Dr. Lakshmi can create a "Liquid Facelift" that shaves years off your appearance in under an hour.</p>

            <div class="alert alert-info mt-4" style="background: var(--navy-950); color: var(--white); border: none; padding: 2rem; border-radius: var(--radius-md);">
                <h4 style="color: var(--gold-400); font-family: var(--font-display);">Ready for a Refresh?</h4>
                <p style="color: rgba(255,255,255,0.8);">Subtle, natural results are the hallmark of excellent aesthetic medicine. Book a skin and facial assessment with Dr. Lakshmi to create your customized anti-aging plan.</p>
                <a href="/contact#book" class="btn btn-cta-gold mt-2">Schedule Your Visit</a>
            </div>
        """
    },
    "what-is-a-mommy-makeover": {
        "slug": "what-is-a-mommy-makeover",
        "title": "What is a Mommy Makeover? Reclaiming Your Pre-Pregnancy Body",
        "date": "May 22, 2025",
        "image": "clinic-interior.jpg",
        "excerpt": "Pregnancy and breastfeeding take a toll on a woman's body. Discover how a customized Mommy Makeover can restore your contours and your confidence.",
        "category": "Plastic Surgery",
        "content": """
            <p class="lead mb-4">Motherhood is a beautiful journey, but it often leaves behind physical changes that diet and exercise simply cannot fix. Deflated breasts, stretched abdominal muscles, and stubborn fat pockets can leave you feeling like a stranger in your own body.</p>

            <p>At Dr. Sreenivas Aesthetics, we believe mothers deserve to feel confident and beautiful. This is why the <strong>Mommy Makeover</strong> has become one of our most popular and transformative procedures.</p>

            <h3>What Exactly is a Mommy Makeover?</h3>
            <p>A Mommy Makeover is not a single surgery; it is a customized combination of body contouring procedures performed during a single operation. By combining surgeries, patients save on recovery time and anesthesia costs while achieving a complete transformation.</p>

            <h3>Common Procedures Included:</h3>
            <div class="row mb-4">
                <div class="col-md-12">
                    <h4>1. Breast Rejuvenation</h4>
                    <p>Breastfeeding and weight fluctuations often lead to volume loss and sagging. Depending on your needs, Dr. Sreenivas may perform a <strong>Breast Lift (Mastopexy)</strong> to raise the breasts to a youthful position, a <strong>Breast Augmentation</strong> to restore lost volume, or a combination of both.</p>

                    <h4>2. Tummy Tuck (Abdominoplasty)</h4>
                    <p>Pregnancy stretches the abdominal skin and often separates the core muscles (diastasis recti). A tummy tuck repairs these torn muscles and removes the excess overhanging skin, restoring a flat, firm core.</p>

                    <h4>3. PAL Liposuction</h4>
                    <p>Hormonal changes can cause stubborn fat to accumulate in the flanks, thighs, and back. Power-Assisted Liposuction is used to sculpt these areas and create a beautiful hourglass silhouette.</p>
                </div>
            </div>

            <h3>Is the Recovery Difficult?</h3>
            <p>Because multiple surgeries are performed at once, the initial recovery requires patience. Most mothers need about 2 to 3 weeks of help around the house and should avoid heavy lifting (including lifting toddlers) for 4 to 6 weeks. However, the trade-off of a single recovery period is highly preferred by busy mothers.</p>

            <div class="alert alert-info mt-4" style="background: var(--cream); border: 1px solid var(--gold-300); padding: 2rem;">
                <h4 class="text-navy" style="font-family: var(--font-display);">Take the First Step</h4>
                <p>You’ve dedicated your life to your family; now it’s time to do something for yourself. Schedule a private, compassionate consultation with Dr. Sreenivas to design your customized Mommy Makeover.</p>
                <a href="/contact#book" class="btn btn-hero-primary mt-2">Book Your Consultation</a>
            </div>
        """
    }
}

# ---------------------------------------------------------------------------
# Config & Database setup
# ---------------------------------------------------------------------------
DB_PATH = os.path.join(os.path.dirname(__file__), "appointments.db")
WHATSAPP_NUMBER = "917903812908"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = hashlib.sha256("admin@2025".encode()).hexdigest()


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id             INTEGER PRIMARY KEY AUTOINCREMENT,
                name           TEXT NOT NULL,
                phone          TEXT NOT NULL,
                email          TEXT NOT NULL,
                service        TEXT NOT NULL,
                doctor         TEXT,
                preferred_date TEXT,
                message        TEXT,
                source         TEXT,
                status         TEXT DEFAULT 'New',
                created_at     TEXT NOT NULL
            )
        """)
        db.commit()


init_db()


# ---------------------------------------------------------------------------
# Admin auth decorator
# ---------------------------------------------------------------------------
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("admin_logged_in"):
            return redirect(url_for("admin_login"))
        return f(*args, **kwargs)

    return decorated


# ---------------------------------------------------------------------------
# WhatsApp URL builder
# ---------------------------------------------------------------------------
def build_whatsapp_url(data: dict) -> str:
    msg = (
        f"*New Appointment — Dr. Sreenivas Aesthetics*\n\n"
        f"*Name:* {data.get('name', '')}\n"
        f"*Phone:* {data.get('phone', '')}\n"
        f"*Email:* {data.get('email', '')}\n"
        f"*Service:* {data.get('service', '')}\n"
        f"*Doctor Preference:* {data.get('doctor', 'No preference')}\n"
        f"*Preferred Date:* {data.get('preferred_date', 'Not specified')}\n"
        f"*Message:* {data.get('message', '')}\n"
        f"*Source:* {data.get('source', 'Not specified')}\n\n"
        f"_Submitted: {datetime.now().strftime('%d %b %Y, %I:%M %p')}_"
    )
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(msg)}"


# ---------------------------------------------------------------------------
# Context processor
# ---------------------------------------------------------------------------
@app.context_processor
def inject_globals():
    return {"clinic": CLINIC, "services": SERVICES}


# ---------------------------------------------------------------------------
# Public routes
# ---------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html", doctors=DOCTORS, blogs=LATEST_BLOGS.values())


@app.route("/about")
def about():
    return render_template("about.html", doctors=DOCTORS)


@app.route("/services")
def services_overview():
    return render_template("services.html")


@app.route("/services/<string:slug>")
def service_detail(slug):
    service = SERVICES.get(slug)
    if not service:
        abort(404)
    return render_template("service_detail.html", service=service, slug=slug)


@app.route("/gallery/photos")
def gallery_photos():
    return render_template("gallery_photos.html")


@app.route("/gallery/videos")
def gallery_videos():
    return render_template("gallery_videos.html")


@app.route("/blogs")
def blogs():
    # Pass the dictionary values as a list to the template
    return render_template("blogs.html", blogs=LATEST_BLOGS.values())


@app.route("/blog/<string:slug>")
def blog_detail(slug):
    # Look up the specific blog
    blog = LATEST_BLOGS.get(slug)
    if not blog:
        abort(404)
    return render_template("blog_detail.html", blog=blog)


# ---------------------------------------------------------------------------
# Contact / Appointment (Saves to DB & returns WhatsApp URL)
# ---------------------------------------------------------------------------
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.get_json(silent=True) or {}

        name = data.get("name", "").strip()
        phone = data.get("phone", "").strip()
        email = data.get("email", "").strip()
        service = data.get("service", "").strip()
        doctor = data.get("doctor", "").strip()
        preferred_date = data.get("preferred_date", "").strip()
        message = data.get("message", "").strip()
        source = data.get("source", "").strip()

        if not name or not phone or not email or not service or not message:
            return jsonify({
                "status": "error",
                "message": "Please fill in all required fields."
            }), 400

        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with get_db() as db:
                db.execute("""
                    INSERT INTO appointments
                      (name, phone, email, service, doctor,
                       preferred_date, message, source, status, created_at)
                    VALUES (?,?,?,?,?,?,?,?,?,?)
                """, (name, phone, email, service, doctor,
                      preferred_date, message, source, "New", created_at))
                db.commit()
        except Exception as e:
            print(f"DB error: {e}")

        wa_url = build_whatsapp_url({
            "name": name, "phone": phone, "email": email,
            "service": service, "doctor": doctor,
            "preferred_date": preferred_date,
            "message": message, "source": source,
        })

        return jsonify({
            "status": "success",
            "message": (
                f"Thank you, {name}! Your request has been received. "
                "Redirecting you to WhatsApp..."
            ),
            "whatsapp_url": wa_url,
        })

    return render_template("contact.html")


# ---------------------------------------------------------------------------
# Admin — Login / Logout
# ---------------------------------------------------------------------------
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        pw_hash = hashlib.sha256(password.encode()).hexdigest()
        if username == ADMIN_USERNAME and pw_hash == ADMIN_PASSWORD_HASH:
            session["admin_logged_in"] = True
            session["admin_user"] = username
            return redirect(url_for("admin_dashboard"))
        error = "Invalid username or password."
    return render_template("admin_login.html", error=error)


@app.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect(url_for("admin_login"))


# ---------------------------------------------------------------------------
# Admin — Dashboard
# ---------------------------------------------------------------------------
@app.route("/admin")
@app.route("/admin/dashboard")
@login_required
def admin_dashboard():
    with get_db() as db:
        total = db.execute("SELECT COUNT(*) FROM appointments").fetchone()[0]
        new_count = db.execute("SELECT COUNT(*) FROM appointments WHERE status='New'").fetchone()[0]
        confirmed = db.execute("SELECT COUNT(*) FROM appointments WHERE status='Confirmed'").fetchone()[0]
        completed = db.execute("SELECT COUNT(*) FROM appointments WHERE status='Completed'").fetchone()[0]
        cancelled = db.execute("SELECT COUNT(*) FROM appointments WHERE status='Cancelled'").fetchone()[0]
        today_count = db.execute("SELECT COUNT(*) FROM appointments WHERE DATE(created_at)=DATE('now')").fetchone()[0]

        service_stats = db.execute("""
            SELECT service, COUNT(*) as cnt
            FROM appointments GROUP BY service ORDER BY cnt DESC
        """).fetchall()

        all_appointments = db.execute("SELECT * FROM appointments ORDER BY id DESC").fetchall()

    stats = {
        "total": total, "new": new_count, "confirmed": confirmed,
        "completed": completed, "cancelled": cancelled, "today": today_count,
    }
    return render_template("admin_dashboard.html", stats=stats, service_stats=service_stats,
                           all_appointments=all_appointments)


# ---------------------------------------------------------------------------
# Admin — Update & Delete
# ---------------------------------------------------------------------------
@app.route("/admin/appointment/<int:appt_id>/status", methods=["POST"])
@login_required
def update_status(appt_id):
    data = request.get_json(silent=True) or {}
    status = data.get("status", "New")
    if status not in {"New", "Confirmed", "Completed", "Cancelled"}:
        return jsonify({"success": False}), 400
    with get_db() as db:
        db.execute("UPDATE appointments SET status=? WHERE id=?", (status, appt_id))
        db.commit()
    return jsonify({"success": True, "status": status})


@app.route("/admin/appointment/<int:appt_id>/delete", methods=["POST"])
@login_required
def delete_appointment(appt_id):
    with get_db() as db:
        db.execute("DELETE FROM appointments WHERE id=?", (appt_id,))
        db.commit()
    return jsonify({"success": True})


@app.route("/admin/appointment/<int:appt_id>/whatsapp")
@login_required
def whatsapp_followup(appt_id):
    with get_db() as db:
        row = db.execute("SELECT * FROM appointments WHERE id=?", (appt_id,)).fetchone()
    if not row:
        abort(404)
    return redirect(build_whatsapp_url(dict(row)))


# ---------------------------------------------------------------------------
# Error handlers
# ---------------------------------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html"), 500


# --- DEBUGGING TRICK ---
with app.app_context():
    print("--- REGISTERED ROUTES ---")
    for rule in app.url_map.iter_rules():
        print(f"Endpoint Name: {rule.endpoint} | Path: {rule}")
    print("-------------------------")
if __name__ == "__main__":
    app.run(debug=True)
