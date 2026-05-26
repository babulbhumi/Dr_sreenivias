# =============================================================
#  services_data.py  —  Dr. Sreenivas Aesthetics
#  Single source of truth for ALL 11 service pages.
# =============================================================

SERVICES = {

    # ════════════ 1. PLASTIC & RECONSTRUCTIVE SURGERY ════════════
    "plastic-surgery": {
        "name": "Plastic & Reconstructive Surgery",
        "category": "Plastic Surgery",
        "icon": "🩺",
        "meta_description": "Advanced plastic and reconstructive surgery at Dr. Sreenivas Aesthetics. Expert care for trauma, burns, scar revision, and congenital corrections.",
        "tagline": "Restoring form, function, and confidence with world-class reconstructive surgical techniques.",
        "hero_stats": [
            {"value": "20+", "label": "Years Experience"},
            {"value": "1000+", "label": "Reconstructions"},
            {"value": "MCh", "label": "Qualified Surgeon"},
        ],
        "highlight_cards": [
            {"icon": "bi-bandaid", "title": "Scar Revision", "text": "Advanced techniques to minimize the appearance of surgical or traumatic scars."},
            {"icon": "bi-fire", "title": "Burn Reconstruction", "text": "Restoring skin mobility and aesthetics after severe burn injuries."},
            {"icon": "bi-person-bounding-box", "title": "Trauma Repair", "text": "Complex facial and body reconstruction following accidents."},
            {"icon": "bi-heart-pulse", "title": "Congenital Defects", "text": "Correction of birth abnormalities like cleft lip and palate."},
        ],
        "overview_paragraphs": [
            "Plastic and reconstructive surgery goes beyond cosmetics; it is about restoring a patient's quality of life, function, and dignity after trauma, illness, or congenital issues. Dr. Pavuluru Sreenivasa Rao brings decades of specialized experience in complex microsurgery and tissue transfer.",
            "Our clinic handles a wide spectrum of reconstructive needs, including post-cancer reconstruction, severe burn scar management, facial trauma repair, and the revision of unsatisfactory scars from previous surgeries.",
            "Every reconstructive journey is deeply personal. We prioritize patient safety, aesthetic harmony, and the restoration of normal physical function, ensuring you feel whole and confident again."
        ],
        "ideal_candidates": [
            "Individuals with restrictive or prominent scars",
            "Patients recovering from severe burns or trauma",
            "Those seeking post-cancer tissue reconstruction",
            "Children or adults with congenital anomalies",
            "Patients requiring correction of previous surgical outcomes"
        ],
        "glance": {
            "duration": "Varies widely (1 - 6 hours)",
            "anaesthesia": "Local or General",
            "recovery": "2 - 6 weeks depending on complexity",
            "results_visible": "Progressive over 6 - 12 months",
            "sessions": "May require staged procedures"
        },
        "procedure_steps": [
            {"icon": "bi-clipboard-pulse", "title": "Clinical Assessment", "description": "Thorough evaluation of the defect, tissue availability, and functional impairment."},
            {"icon": "bi-map", "title": "Surgical Mapping", "description": "Planning incisions, flaps, or grafts to ensure the best aesthetic and functional outcome."},
            {"icon": "bi-scissors", "title": "Reconstruction", "description": "Execution of the surgical plan using advanced microsurgical or tissue rearrangement techniques."},
            {"icon": "bi-bandaid", "title": "Wound Care", "description": "Specialized dressings and immediate post-operative care to ensure graft survival."},
            {"icon": "bi-arrow-repeat", "title": "Rehabilitation", "description": "Long-term monitoring and physical therapy recommendations to restore full function."}
        ],
        "before_after_cases": [
            {"title": "Facial Trauma Repair", "description": "Restoration of facial symmetry following a complex fracture."},
            {"title": "Burn Contracture Release", "description": "Improved neck mobility and skin texture after severe burn injuries."},
            {"title": "Keloid Scar Revision", "description": "Flattening and fading of a prominent chest keloid."}
        ],
        "faqs": [
            {"question": "What is the difference between cosmetic and reconstructive surgery?", "answer": "Cosmetic surgery reshapes normal structures to improve appearance. Reconstructive surgery is performed on abnormal structures caused by trauma, infection, tumors, or disease to improve function and approximate a normal appearance."},
            {"question": "Will scar revision erase my scar completely?", "answer": "No surgery can completely erase a scar. However, scar revision can significantly improve the size, thickness, color, and restrictiveness of the scar, making it blend beautifully with surrounding skin."},
            {"question": "Are reconstructive procedures covered by insurance?", "answer": "Unlike cosmetic procedures, many reconstructive surgeries (like post-trauma or congenital defect repair) may be covered by health insurance. We can assist with the necessary medical documentation."}
        ]
    },

    # ════════════ 2. AESTHETICS (BOTOX/FILLERS/PMU) ════════════
    "aesthetics": {
        "name": "Aesthetic Medicine & PMU",
        "category": "Facial Aesthetics",
        "icon": "✨",
        "meta_description": "Non-surgical aesthetic medicine in Nellore. Botox, dermal fillers, thread lifts, and Permanent Makeup (PMU) by Dr. Veli Jaswantha Lakshmi.",
        "tagline": "Enhance your natural beauty with premium non-surgical treatments and flawless permanent makeup artistry.",
        "hero_stats": [
            {"value": "1000+", "label": "Happy Clients"},
            {"value": "Certified", "label": "PMU Artist"},
            {"value": "Zero", "label": "Downtime"},
        ],
        "highlight_cards": [
            {"icon": "bi-lightning-charge", "title": "Anti-Wrinkle (Botox)", "text": "Smooth out frown lines, crow's feet, and forehead wrinkles effortlessly."},
            {"icon": "bi-droplet", "title": "Dermal Fillers", "text": "Restore lost volume to cheeks, lips, and jawline with premium HA fillers."},
            {"icon": "bi-brush", "title": "Permanent Makeup", "text": "Flawless microblading, ombré brows, and lip blush that lasts for years."},
            {"icon": "bi-arrow-up-circle", "title": "Thread Lifts", "text": "Non-surgical skin tightening and lifting for a rejuvenated profile."},
        ],
        "overview_paragraphs": [
            "Aesthetic medicine provides powerful anti-aging and facial enhancement solutions without the need for invasive surgery. Led by Dr. Veli Velli Jaswantha Lakshmi (APMC/FMR/104005), our clinic offers the highest standard of injectable treatments and cosmetic artistry.",
            "Whether you are looking to smooth dynamic wrinkles with Botox, restore youthful volume with Hyaluronic Acid fillers, or achieve a flawless daily look with Permanent Makeup (PMU), our approach is always subtle, elegant, and uniquely tailored to your facial anatomy.",
            "We believe that aesthetic treatments should never make you look 'done' or unnatural. Our goal is to make you look rested, vibrant, and like the absolute best version of yourself."
        ],
        "ideal_candidates": [
            "Individuals showing early signs of aging (fine lines, volume loss)",
            "Those wanting fuller lips or defined cheekbones without surgery",
            "People seeking semi-permanent solutions for sparse eyebrows or pale lips",
            "Patients looking for 'lunchtime' procedures with no downtime",
            "Adults wanting to maintain a fresh, youthful appearance"
        ],
        "glance": {
            "duration": "30 - 90 minutes",
            "anaesthesia": "Topical Numbing Cream",
            "recovery": "Immediate (Mild swelling for 24-48 hours)",
            "results_visible": "Immediate to 2 weeks",
            "sessions": "Maintenance every 6-12 months"
        },
        "procedure_steps": [
            {"icon": "bi-chat-dots", "title": "Facial Assessment", "description": "Detailed analysis of your skin quality, muscle movement, and volume distribution."},
            {"icon": "bi-palette", "title": "Customized Plan", "description": "Selecting the exact units of Botox, type of filler, or pigment shade for PMU."},
            {"icon": "bi-thermometer", "title": "Preparation", "description": "Application of premium numbing cream to ensure absolute comfort."},
            {"icon": "bi-magic", "title": "The Treatment", "description": "Precise administration of injectables or meticulous PMU application."},
            {"icon": "bi-calendar-check", "title": "Follow-up", "description": "A 2-week review to assess the settled results and perfect any details."}
        ],
        "before_after_cases": [
            {"title": "Lip Augmentation", "description": "Subtle volume enhancement and definition using HA fillers."},
            {"title": "Microblading", "description": "Sparse, uneven brows transformed into full, natural-looking arches."},
            {"title": "Forehead Smoothing", "description": "Complete relaxation of deep forehead lines using anti-wrinkle injections."}
        ],
        "faqs": [
            {"question": "How long do dermal fillers last?", "answer": "Depending on the type of filler used and the area treated (e.g., lips vs. cheeks), results typically last between 6 to 18 months."},
            {"question": "Is Botox safe?", "answer": "Yes. Botulinum toxin has been used safely in medicine for decades. When administered by a qualified doctor like Dr. Lakshmi, it is a highly safe and predictable treatment."},
            {"question": "Does PMU look like a traditional tattoo?", "answer": "No. Modern PMU uses specialized pigments and superficial techniques (like micro-strokes) to mimic natural hair and soft makeup, avoiding the harsh, blocky look of old tattoos."}
        ]
    },

    # ════════════ 3. LASER TREATMENTS ════════════
    "laser": {
        "name": "Laser Skin Therapy",
        "category": "Skin & Laser",
        "icon": "⚡",
        "meta_description": "Medical-grade laser treatments in Nellore. CO2 fractional lasers, Q-Switch, laser hair removal, and pigmentation treatments.",
        "tagline": "Erase imperfections and reveal flawless skin with advanced, medical-grade laser technology.",
        "hero_stats": [
            {"value": "FDA", "label": "Approved Tech"},
            {"value": "95%", "label": "Clearance Rate"},
            {"value": "Safe", "label": "For All Skin Types"},
        ],
        "highlight_cards": [
            {"icon": "bi-stars", "title": "Acne Scar Removal", "text": "Fractional CO2 lasers stimulate deep collagen to smooth pitted scars."},
            {"icon": "bi-brightness-high", "title": "Pigmentation & Melasma", "text": "Q-Switch lasers safely break down dark spots and uneven skin tone."},
            {"icon": "bi-scissors", "title": "Laser Hair Reduction", "text": "Permanent, painless reduction of unwanted body and facial hair."},
            {"icon": "bi-arrow-repeat", "title": "Skin Resurfacing", "text": "Peel away dull, aging skin layers to reveal a glowing, youthful complexion."},
        ],
        "overview_paragraphs": [
            "Sun damage, aging, and acne can leave lasting marks on our skin. Our advanced laser therapy suite utilizes clinically proven, FDA-approved technology to treat these concerns at a cellular level, delivering results that topical creams simply cannot achieve.",
            "We specialize in Fractional CO2 laser resurfacing for severe acne scars and anti-aging, as well as Q-Switch Nd:YAG lasers for the safe removal of pigmentation, melasma, and tattoos.",
            "Every laser protocol is customized to your specific Fitzpatrick skin type to ensure maximum efficacy while strictly avoiding hyperpigmentation or thermal damage."
        ],
        "ideal_candidates": [
            "Patients with active acne or deep acne scarring",
            "Individuals suffering from melasma, sun spots, or hyperpigmentation",
            "Those seeking a permanent solution to unwanted hair",
            "Patients with fine lines, enlarged pores, or dull skin texture",
            "Anyone seeking overall skin rejuvenation"
        ],
        "glance": {
            "duration": "20 - 60 minutes",
            "anaesthesia": "Topical Numbing (for resurfacing)",
            "recovery": "None to 5 days (depending on laser type)",
            "results_visible": "After 1 - 3 sessions",
            "sessions": "Typically a course of 3 - 6 sessions"
        },
        "procedure_steps": [
            {"icon": "bi-search", "title": "Skin Analysis", "description": "Determining your exact skin type and the depth of the pigmentation or scarring."},
            {"icon": "bi-shield-check", "title": "Safety Prep", "description": "Eye protection is provided, and cooling gels or numbing creams are applied."},
            {"icon": "bi-lightning", "title": "Laser Pass", "description": "Precise delivery of light energy to target melanin, hair follicles, or scar tissue."},
            {"icon": "bi-snow", "title": "Cooling & Calming", "description": "Post-laser cooling masks and serums are applied to reduce redness."},
            {"icon": "bi-sun", "title": "Sun Protection", "description": "Strict SPF application and aftercare instructions to protect newly treated skin."}
        ],
        "before_after_cases": [
            {"title": "Acne Scar Resurfacing", "description": "Significant smoothing of deep 'ice-pick' scars using Fractional CO2."},
            {"title": "Melasma Clearance", "description": "Fading of stubborn cheek pigmentation after 4 sessions of Q-Switch laser."},
            {"title": "Laser Hair Reduction", "description": "Smooth, hair-free underarms achieved after a standard course of treatment."}
        ],
        "faqs": [
            {"question": "Is laser hair removal permanent?", "answer": "It is accurately described as 'permanent hair reduction.' While it destroys current active follicles, hormonal changes can cause new fine hairs to grow years later. Maintenance sessions are rare but possible."},
            {"question": "Does CO2 laser resurfacing hurt?", "answer": "We use strong topical numbing creams prior to Fractional CO2 treatments. Patients usually feel a warm, prickling sensation, but it is highly tolerable."},
            {"question": "Can I go in the sun after laser?", "answer": "No. Strict sun avoidance and the use of high-SPF sunscreen are mandatory for at least 2 weeks post-treatment to prevent hyperpigmentation."}
        ]
    },

    # ════════════ 4. HAIR TRANSPLANTATION ════════════
    "hair-transplantation": {
        "name": "Hair Transplantation",
        "category": "Hair Restoration",
        "icon": "💆",
        "meta_description": "Best Hair Transplant clinic in Nellore. Advanced FUE and FUT procedures for natural, permanent hair regrowth by Dr. Sreenivasa Rao.",
        "tagline": "Restore your hairline and your confidence with permanent, natural-looking follicular unit extraction (FUE).",
        "hero_stats": [
            {"value": "98%", "label": "Graft Survival Rate"},
            {"value": "5000+", "label": "Grafts in 1 Session"},
            {"value": "100%", "label": "Natural Look"},
        ],
        "highlight_cards": [
            {"icon": "bi-droplet", "title": "Advanced FUE", "text": "Individual follicle extraction leaving no linear scars and ensuring fast recovery."},
            {"icon": "bi-grid-3x3", "title": "High Density", "text": "Strategic dense-packing techniques to maximize volume in balding areas."},
            {"icon": "bi-person", "title": "Artistic Hairlines", "text": "Custom-designed hairlines that perfectly match your age and facial structure."},
            {"icon": "bi-activity", "title": "PRP Integration", "text": "Combining transplants with Platelet-Rich Plasma to boost graft survival."},
        ],
        "overview_paragraphs": [
            "Hair loss can severely impact self-esteem, but modern hair transplantation offers a permanent, completely natural solution. At Dr. Sreenivas Aesthetics, we specialize in advanced FUE (Follicular Unit Extraction) and FUT techniques.",
            "Unlike older 'plug' methods, we extract healthy, DHT-resistant hair follicles from the back of your scalp and artistically implant them into thinning areas one by one. This mimics the natural angle, direction, and density of your original hair.",
            "Because the transplanted hair is genetically resistant to the hormones that cause baldness, the results are permanent. You can cut, style, and wash your new hair exactly as you always have."
        ],
        "ideal_candidates": [
            "Men suffering from male pattern baldness (receding hairline or crown loss)",
            "Women experiencing diffuse thinning or traction alopecia",
            "Individuals seeking to restore eyebrows or beard density",
            "Patients with sufficient donor hair at the back of the scalp",
            "Those with realistic expectations about hair density and growth timelines"
        ],
        "glance": {
            "duration": "6 - 10 Hours",
            "anaesthesia": "Local Anaesthesia",
            "recovery": "3 - 7 Days",
            "results_visible": "6 - 12 Months for full growth",
            "sessions": "Usually 1 (Extensive loss may require 2)"
        },
        "procedure_steps": [
            {"icon": "bi-pencil", "title": "Design & Planning", "description": "Drawing the new hairline and determining the exact number of grafts required."},
            {"icon": "bi-scissors", "title": "Extraction", "description": "Painless removal of individual hair follicles from the donor area under local anaesthesia."},
            {"icon": "bi-grid", "title": "Incision Creation", "description": "Micro-incisions are made in the bald areas at precise angles to mimic natural growth."},
            {"icon": "bi-arrow-down-square", "title": "Implantation", "description": "Grafts are delicately placed into the incisions by our expert surgical team."},
            {"icon": "bi-calendar-check", "title": "Growth Phase", "description": "Transplanted hair sheds after 3 weeks, then regrows permanently starting at month 4."}
        ],
        "before_after_cases": [
            {"title": "Frontal Hairline Restoration", "description": "A deep receding hairline completely restored with 2,500 grafts."},
            {"title": "Crown Density Fix", "description": "Significant thickening of a bald crown using high-density FUE."},
            {"title": "Beard Reconstruction", "description": "Patchy facial hair transformed into a full, dense beard."}
        ],
        "faqs": [
            {"question": "Is the procedure painful?", "answer": "The procedure is done under local anaesthesia, meaning the scalp is completely numb. You will feel no pain during the surgery. Mild soreness for a few days post-op is managed with standard painkillers."},
            {"question": "Will people know I had a transplant?", "answer": "Once fully grown, the hair looks 100% natural because it is your own hair. The FUE method leaves tiny, dot-like scars in the donor area that are virtually invisible even with a short haircut."},
            {"question": "When will I see the final results?", "answer": "Patience is key. The transplanted hairs will fall out after 3 weeks (this is normal). New growth begins around month 3 or 4, with final, thick results visible between 10 to 12 months."}
        ]
    },

    # ════════════ 5. RHINOPLASTY (NOSE SURGERY) ════════════
    "rhinoplasty": {
        "name": "Rhinoplasty (Nose Surgery)",
        "category": "Facial Surgery",
        "icon": "👃",
        "meta_description": "Expert rhinoplasty and nose reshaping in Nellore. Fix deviated septums, dorsal humps, and refine nasal tips with Dr. Sreenivasa Rao.",
        "tagline": "Refine your profile and achieve perfect facial harmony with precision nose reshaping.",
        "hero_stats": [
            {"value": "99%", "label": "Satisfaction Rate"},
            {"value": "300+", "label": "Noses Reshaped"},
            {"value": "3D", "label": "Facial Analysis"},
        ],
        "highlight_cards": [
            {"icon": "bi-symmetry-vertical", "title": "Facial Harmony", "text": "Reshaping the nose to perfectly balance your cheeks, chin, and overall profile."},
            {"icon": "bi-lungs", "title": "Functional Repair", "text": "Correcting deviated septums to radically improve airflow and breathing."},
            {"icon": "bi-arrows-angle-contract", "title": "Tip & Hump Refinement", "text": "Smoothing out dorsal humps and lifting or refining bulbous nasal tips."},
            {"icon": "bi-arrow-repeat", "title": "Revision Surgery", "text": "Expert corrective surgery for patients unhappy with past procedures done elsewhere."},
        ],
        "overview_paragraphs": [
            "Rhinoplasty is widely considered the most artistically demanding procedure in plastic surgery. Even a millimeter of change can dramatically alter facial balance. Dr. Sreenivasa Rao approaches every nose as a unique structural and aesthetic challenge.",
            "Whether you are looking to smooth a prominent bridge, refine a wide tip, or straighten a crooked nose, our goal is never to create a 'cookie-cutter' look. Instead, we craft a nose that looks natural and belongs seamlessly on your face.",
            "In addition to aesthetics, we also perform functional rhinoplasty (Septoplasty) to clear breathing obstructions, ensuring your nose works as beautifully as it looks."
        ],
        "ideal_candidates": [
            "Individuals unhappy with the size, shape, or angle of their nose",
            "Patients suffering from breathing issues due to a deviated septum",
            "Those seeking to repair nasal trauma or sports injuries",
            "Patients over the age of 18 (when facial growth is complete)",
            "Individuals looking to fix an unsatisfactory previous nose surgery"
        ],
        "glance": {
            "duration": "2 - 4 Hours",
            "anaesthesia": "General Anaesthesia",
            "recovery": "1 - 2 Weeks (Splint removal after 7 days)",
            "results_visible": "70% at 1 month, final refinement up to 1 year",
            "sessions": "1"
        },
        "procedure_steps": [
            {"icon": "bi-camera", "title": "3D Planning", "description": "In-depth consultation and photographic analysis to agree on the exact target shape."},
            {"icon": "bi-bandaid", "title": "Incision Approach", "description": "Using either an 'open' (tiny incision under the tip) or 'closed' (all incisions hidden inside) technique."},
            {"icon": "bi-hammer", "title": "Structural Reshaping", "description": "Cartilage and bone are meticulously sculpted, reduced, or grafted to create the new framework."},
            {"icon": "bi-shield", "title": "Splinting", "description": "A customized external splint is applied to protect the delicate new shape during early healing."},
            {"icon": "bi-check2-circle", "title": "Reveal", "description": "The splint is removed after 7 days, revealing the immediate transformation."}
        ],
        "before_after_cases": [
            {"title": "Dorsal Hump Removal", "description": "A prominent bump on the bridge was smoothed for a straight, elegant profile."},
            {"title": "Bulbous Tip Refinement", "description": "A wide, drooping nasal tip was lifted and narrowed to match the patient's delicate features."},
            {"title": "Functional Correction", "description": "A crooked nose straightened to improve both aesthetics and severe breathing issues."}
        ],
        "faqs": [
            {"question": "Will I have visible scars?", "answer": "If a 'closed' rhinoplasty is performed, all incisions are inside the nostrils with zero visible scarring. An 'open' rhinoplasty leaves a tiny, 2mm scar under the tip of the nose that fades to become virtually undetectable."},
            {"question": "When can I see the final result?", "answer": "You will see a massive difference when the splint is removed at day 7. However, the nose retains subtle swelling for months. The absolute final, refined shape is typically judged at the 1-year mark."},
            {"question": "Does it affect breathing?", "answer": "Cosmetic changes should never compromise breathing. In fact, we routinely combine aesthetic reshaping with septoplasty to actively improve your nasal airflow."}
        ]
    },

    # ════════════ 6. BREAST SURGERY ════════════
    "breast-surgery": {
        "name": "Breast Surgery (Augmentation & Reduction)",
        "category": "Breast & Chest",
        "icon": "🌸",
        "meta_description": "Safe and natural-looking breast augmentation, lift, and reduction surgeries in Nellore by expert plastic surgeon Dr. Sreenivasa Rao.",
        "tagline": "Achieve perfect proportion and renewed confidence with custom-tailored breast enhancements.",
        "hero_stats": [
            {"value": "100%", "label": "FDA Implants"},
            {"value": "Custom", "label": "Size Mapping"},
            {"value": "Seamless", "label": "Hidden Scars"},
        ],
        "highlight_cards": [
            {"icon": "bi-arrow-up-circle", "title": "Breast Augmentation", "text": "Enhance volume and shape using premium silicone implants or natural fat transfer."},
            {"icon": "bi-arrow-down-circle", "title": "Breast Reduction", "text": "Relieve neck and back pain by safely reducing heavy, oversized breasts."},
            {"icon": "bi-chevron-up", "title": "Breast Lift (Mastopexy)", "text": "Restore youthful perkiness and correct sagging caused by pregnancy or weight loss."},
            {"icon": "bi-heart", "title": "Asymmetry Correction", "text": "Surgical balancing to ensure both breasts match beautifully in size and shape."},
        ],
        "overview_paragraphs": [
            "Whether you desire a fuller cup size, need relief from the physical burden of overly large breasts, or wish to restore volume lost after childbirth, breast surgery is one of the most confidence-boosting procedures we perform.",
            "Dr. Rao utilizes 3D sizing techniques to help you choose the perfect implant size that complements your unique body frame. We exclusively use FDA-approved, highly cohesive silicone gel implants (often called 'gummy bear' implants) for the most natural look and feel.",
            "For patients seeking a lift or reduction, our advanced techniques focus on maximizing breast shape while keeping incisions as discreet and well-hidden as possible."
        ],
        "ideal_candidates": [
            "Women seeking more volume or improved breast shape",
            "Mothers wanting to restore perkiness after breastfeeding ('Mommy Makeover')",
            "Women suffering back and shoulder pain from overly large breasts",
            "Patients with noticeably uneven or asymmetrical breasts",
            "Healthy non-smokers with realistic aesthetic goals"
        ],
        "glance": {
            "duration": "1.5 - 3 Hours",
            "anaesthesia": "General Anaesthesia",
            "recovery": "1 - 2 Weeks (No heavy lifting for 4 weeks)",
            "results_visible": "Immediate (Settles naturally over 3 months)",
            "sessions": "1"
        },
        "procedure_steps": [
            {"icon": "bi-rulers", "title": "Sizing & Simulation", "description": "Trying on external sizers to find the exact volume that fits your goals and anatomy."},
            {"icon": "bi-check2-square", "title": "Surgical Plan", "description": "Deciding on incision placement (under the crease, around the areola) and implant position (under or over the muscle)."},
            {"icon": "bi-hospital", "title": "The Surgery", "description": "Precise creation of the pocket and insertion of the implant, or removal of excess tissue for reductions."},
            {"icon": "bi-bandaid", "title": "Surgical Bra", "description": "Waking up in a specialized compression bra to support the new shape and minimize swelling."},
            {"icon": "bi-arrow-down", "title": "The 'Drop and Fluff'", "description": "Over 3-6 months, implants settle into their natural pocket, softening and taking on a beautiful teardrop shape."}
        ],
        "before_after_cases": [
            {"title": "Volume Enhancement", "description": "A natural-looking transition from an A-cup to a full C-cup using moderate profile implants."},
            {"title": "Breast Lift Post-Pregnancy", "description": "Restoration of youthful breast height and firmness without the use of implants."},
            {"title": "Therapeutic Reduction", "description": "Significant reduction of breast size, alleviating years of chronic neck pain."}
        ],
        "faqs": [
            {"question": "How long do breast implants last?", "answer": "Modern cohesive gel implants are extremely durable and are designed to last a lifetime. They do not have an 'expiration date', though some women choose to update them after 10-15 years if their size preferences change."},
            {"question": "Will I still be able to breastfeed?", "answer": "In most breast augmentation surgeries, the milk ducts are left completely intact, allowing for normal breastfeeding. Breast reductions and lifts carry a higher risk of affecting milk supply, which will be discussed during consultation."},
            {"question": "Where are the scars hidden?", "answer": "For augmentation, scars are typically hidden in the natural fold under the breast (inframammary fold) and fade excellently. Lifts and reductions require more incisions, usually around the areola and down the center, which fade to fine white lines."}
        ]
    },

    # ════════════ 7. LIPOSUCTION ════════════
    "liposuction": {
        "name": "Liposuction & Fat Reduction",
        "category": "Body Contouring",
        "icon": "📏",
        "meta_description": "Advanced PAL Liposuction in Nellore. Safely remove stubborn belly fat, love handles, and double chins with Dr. Sreenivasa Rao.",
        "tagline": "Sculpt your dream silhouette by permanently eliminating stubborn, diet-resistant fat.",
        "hero_stats": [
            {"value": "PAL", "label": "Technology"},
            {"value": "360°", "label": "Contouring"},
            {"value": "Permanent", "label": "Fat Removal"},
        ],
        "highlight_cards": [
            {"icon": "bi-bullseye", "title": "Targeted Removal", "text": "Erase stubborn fat pockets from the belly, thighs, arms, and back."},
            {"icon": "bi-lightning-charge", "title": "PAL Technology", "text": "Power-Assisted Liposuction ensures smoother results with less bruising."},
            {"icon": "bi-arrow-left-right", "title": "Fat Grafting", "text": "Purify and inject your removed fat to naturally enhance your buttocks or face."},
            {"icon": "bi-person-lines-fill", "title": "HD Sculpting", "text": "High-definition techniques to reveal underlying abdominal muscle tone."},
        ],
        "overview_paragraphs": [
            "Despite rigorous dieting and exercise, certain areas of the body simply refuse to let go of fat. Liposuction is the gold standard for physically removing these stubborn fat cells to reshape and contour your body.",
            "Dr. Rao utilizes Power-Assisted Liposuction (PAL), a cutting-edge technique where a vibrating cannula gently breaks up fat tissue. This allows for precise, high-volume fat extraction while minimizing trauma to surrounding blood vessels and nerves, resulting in a much faster, more comfortable recovery.",
            "Because the fat cells are completely removed from the body, the contouring results are permanent, provided you maintain a stable lifestyle and weight."
        ],
        "ideal_candidates": [
            "Individuals close to their ideal weight with specific bulges of fat",
            "Patients with good skin elasticity (skin that bounces back)",
            "Those looking to target 'love handles', bra rolls, or double chins",
            "Healthy adults who are non-smokers",
            "Patients understanding that liposuction is for contouring, not weight loss"
        ],
        "glance": {
            "duration": "1 - 3 Hours (Depending on areas)",
            "anaesthesia": "General or Local with Sedation",
            "recovery": "3 - 7 Days (Compression garment for 4 weeks)",
            "results_visible": "1 Month (Final results at 3-6 months)",
            "sessions": "1"
        },
        "procedure_steps": [
            {"icon": "bi-pen", "title": "Marking", "description": "Standing topographic mapping of the fat deposits to guide the surgery."},
            {"icon": "bi-droplet", "title": "Tumescent Fluid", "description": "Injection of a specialized fluid that numbs the area and minimizes bleeding."},
            {"icon": "bi-activity", "title": "Fat Extraction", "description": "Using PAL technology to gently break apart and suction out the targeted fat cells."},
            {"icon": "bi-layers", "title": "Compression", "description": "Immediate fitting of a custom compression garment to reduce swelling and shape the skin."},
            {"icon": "bi-calendar-check", "title": "Skin Retraction", "description": "Over several months, the skin tightens and retracts over your newly sculpted framework."}
        ],
        "before_after_cases": [
            {"title": "Abdomen & Flanks 360", "description": "Complete elimination of love handles and lower belly fat for an hourglass figure."},
            {"title": "Double Chin Removal", "description": "Submental liposuction to reveal a sharp, defined jawline."},
            {"title": "Arm Contouring", "description": "Removal of 'bat-wing' fat for slim, toned upper arms."}
        ],
        "faqs": [
            {"question": "Is liposuction a weight-loss surgery?", "answer": "No. Liposuction is a contouring procedure. It removes localized fat that masks your natural shape. While you will lose some pounds of fat, the goal is inches lost and improved silhouette, not massive weight reduction."},
            {"question": "Will the fat grow back?", "answer": "The specific fat cells removed are gone forever. However, if you consume a caloric surplus, the remaining fat cells in your body can expand. Maintaining a healthy lifestyle ensures your new shape lasts a lifetime."},
            {"question": "What is a compression garment and why do I need it?", "answer": "It is a tight, elastic bodysuit worn post-surgery. It serves two vital purposes: it squeezes out post-surgical swelling, and it forces your empty skin to shrink and adhere smoothly to your new, slimmer muscle contours."}
        ]
    },

    # ════════════ 8. TUMMY TUCK (ABDOMINOPLASTY) ════════════
    "tummy-tuck-body-lift": {
        "name": "Tummy Tuck & Body Lift",
        "category": "Body Contouring",
        "icon": "🧍",
        "meta_description": "Transform your core with Abdominoplasty (Tummy Tuck) in Nellore. Remove loose skin and repair muscles after pregnancy or weight loss.",
        "tagline": "Reclaim a flat, firm, and toned abdomen by removing excess skin and tightening core muscles.",
        "hero_stats": [
            {"value": "Muscle", "label": "Repair"},
            {"value": "Excess Skin", "label": "Removed"},
            {"value": "Flatter", "label": "Profile"},
        ],
        "highlight_cards": [
            {"icon": "bi-scissors", "title": "Skin Excision", "text": "Surgical removal of the loose, hanging 'apron' of skin on the lower belly."},
            {"icon": "bi-link", "title": "Muscle Repair", "text": "Sewing separated abdominal muscles (Diastasis Recti) back tightly together."},
            {"icon": "bi-record-circle", "title": "Belly Button Styling", "text": "Creating a new, natural-looking, youthful belly button position."},
            {"icon": "bi-arrow-left-right", "title": "Mini vs Full", "text": "Tailored procedures depending on the severity of the loose skin."},
        ],
        "overview_paragraphs": [
            "Pregnancy and massive weight loss are incredible journeys, but they often leave behind stretched abdominal muscles and loose, hanging skin that no amount of crunches or dieting can fix. A Tummy Tuck (Abdominoplasty) is the only way to structurally repair this damage.",
            "During the procedure, Dr. Rao acts as an internal tailor. He first tightens the abdominal wall muscles like a corset, restoring core strength and flattening the stomach. He then meticulously removes the excess, stretched skin.",
            "The result is a dramatically flatter, firmer, and more youthful abdominal profile. For patients with massive weight loss, we also offer extended Body Lifts that address sagging skin around the hips and back."
        ],
        "ideal_candidates": [
            "Mothers experiencing Diastasis Recti (muscle separation) post-pregnancy",
            "Individuals left with sagging skin aprons after massive weight loss",
            "Patients who have reached a stable, healthy weight",
            "Healthy adults committed to maintaining their results",
            "Non-smokers (crucial for proper wound healing)"
        ],
        "glance": {
            "duration": "2.5 - 4 Hours",
            "anaesthesia": "General Anaesthesia",
            "recovery": "2 - 3 Weeks (Drain removal at 5-7 days)",
            "results_visible": "Immediate flattening, scars fade over 12 months",
            "sessions": "1"
        },
        "procedure_steps": [
            {"icon": "bi-pen", "title": "Incision Placement", "description": "A low horizontal incision is made, designed to be hidden beneath bikini or underwear lines."},
            {"icon": "bi-arrows-collapse", "title": "Muscle Corseting", "description": "The weakened underlying abdominal muscles are pulled together and stitched tightly in place."},
            {"icon": "bi-scissors", "title": "Skin Removal", "description": "The skin is pulled taut downward, and the excess overlapping tissue is surgically removed."},
            {"icon": "bi-circle", "title": "Umbilicoplasty", "description": "A small opening is created to bring the belly button through to its new, natural position."},
            {"icon": "bi-bandaid", "title": "Suturing & Drains", "description": "The incision is closed with fine sutures, and temporary drains may be placed to prevent fluid buildup."}
        ],
        "before_after_cases": [
            {"title": "Post-Pregnancy Repair", "description": "Complete flattening of a protruding belly caused by severe muscle separation."},
            {"title": "Weight Loss Skin Removal", "description": "Excision of a heavy skin apron following a 30kg weight loss journey."},
            {"title": "Mini Tummy Tuck", "description": "Correction of a stubborn lower belly 'pooch' beneath the belly button."}
        ],
        "faqs": [
            {"question": "How long is the scar?", "answer": "A full tummy tuck scar runs horizontally from hipbone to hipbone. While it is long, Dr. Rao meticulously places it very low on the pelvis so it is completely hidden by standard underwear or bikini bottoms."},
            {"question": "Can I get pregnant after a tummy tuck?", "answer": "Yes, it is medically safe to get pregnant after a tummy tuck. However, we strongly advise patients to wait until they are finished having children, as future pregnancies will stretch the skin and muscles out again, ruining the surgical result."},
            {"question": "What is Diastasis Recti?", "answer": "During pregnancy, the growing baby forces the two vertical halves of your abdominal muscle to split apart. Often, they do not fuse back together, leaving a permanent bulge. A tummy tuck physically sews them back together."}
        ]
    },

    # ════════════ 9. FACELIFT & CONTOURING ════════════
    "facelift": {
        "name": "Facelift & Contouring",
        "category": "Facial Surgery",
        "icon": "✨",
        "meta_description": "Turn back the clock with a natural-looking SMAS Facelift in Nellore. Say goodbye to jowls, deep folds, and sagging neck skin.",
        "tagline": "Erase a decade of aging with a natural, meticulously executed facial lift.",
        "hero_stats": [
            {"value": "10-15", "label": "Years Erased"},
            {"value": "SMAS", "label": "Deep Muscle Lift"},
            {"value": "Natural", "label": "Un-pulled Look"},
        ],
        "highlight_cards": [
            {"icon": "bi-arrow-up-circle", "title": "SMAS Facelift", "text": "Lifting the deep muscular layer of the face for long-lasting, natural results."},
            {"icon": "bi-person-lines-fill", "title": "Neck Lift", "text": "Smoothing 'turkey neck' banding and tightening loose skin under the chin."},
            {"icon": "bi-dash-circle", "title": "Mini-Lift", "text": "A targeted lift for early jowling with shorter incisions and faster recovery."},
            {"icon": "bi-droplet", "title": "Fat Grafting", "text": "Adding lost youthful volume back to the cheeks using your own purified fat."},
        ],
        "overview_paragraphs": [
            "As we age, gravity, sun exposure, and volume loss cause the face to sag, creating deep folds around the mouth, jowls along the jawline, and loose skin on the neck. A Facelift (Rhytidectomy) is the ultimate gold standard for comprehensive facial rejuvenation.",
            "Dr. Rao performs advanced SMAS facelifts. Instead of just pulling the skin tight (which creates a fake, 'windblown' look), he lifts and secures the underlying muscle layer. This restores your facial structures to where they were ten years ago.",
            "The result is exceptionally natural. You will not look like a different person; you will look like a completely refreshed, vibrant version of yourself."
        ],
        "ideal_candidates": [
            "Men and women in their 40s to 60s showing moderate to severe facial sagging",
            "Patients with prominent jowls hiding their jawline",
            "Individuals with deep nasolabial folds (smile lines)",
            "Those with loose, banding skin on the neck",
            "Healthy non-smokers (smoking severely impacts facial healing)"
        ],
        "glance": {
            "duration": "3 - 5 Hours",
            "anaesthesia": "General or Deep IV Sedation",
            "recovery": "2 Weeks (Social downtime)",
            "results_visible": "1 Month (Scars mature over 6 months)",
            "sessions": "1"
        },
        "procedure_steps": [
            {"icon": "bi-scissors", "title": "Hidden Incisions", "description": "Incisions are carefully hidden within the hairline and in the natural creases around the ear."},
            {"icon": "bi-layers", "title": "Deep Tissue Lift", "description": "The SMAS (muscle and connective tissue) layer is lifted and sutured into a higher, youthful position."},
            {"icon": "bi-magic", "title": "Redraping", "description": "The skin is gently laid back over the lifted muscle without any tension to avoid a 'pulled' look."},
            {"icon": "bi-trash", "title": "Excess Removal", "description": "The overlapping, redundant skin is carefully trimmed away."},
            {"icon": "bi-bandaid", "title": "Suturing", "description": "Incisions are closed with microscopic sutures to ensure the finest, most invisible scars possible."}
        ],
        "before_after_cases": [
            {"title": "Jawline Restoration", "description": "Heavy jowls completely eliminated to reveal a sharp, defined jaw angle."},
            {"title": "Neck Lift", "description": "Correction of severe neck sagging and vertical muscle banding."},
            {"title": "Full Facial Rejuvenation", "description": "A combination of facelift and eyelid surgery erasing over 15 years of visible aging."}
        ],
        "faqs": [
            {"question": "Will my face look tight or fake?", "answer": "No. The 'fake' look happens when surgeons only pull the skin. Because Dr. Rao lifts the heavy muscle layer underneath, the tension is on the muscle, not the skin. Your skin simply rests naturally over the newly lifted structure."},
            {"question": "How long does a facelift last?", "answer": "While a facelift resets the clock by 10 to 15 years, the clock does keep ticking. Aging will naturally resume from this new, rejuvenated baseline. Most patients enjoy their results for 10-15 years or more."},
            {"question": "Where are the scars?", "answer": "Scars follow the hairline at the temples, trace perfectly around the natural curves of the ear, and extend slightly into the scalp behind the ear. Once healed, they are notoriously difficult to see, even up close."}
        ]
    },

    # ════════════ 10. INTIMATE WELLNESS ════════════
    "intimate-wellness": {
        "name": "Intimate Wellness & Surgery",
        "category": "Intimate Wellness",
        "icon": "🌸",
        "meta_description": "Discreet and professional intimate wellness procedures in Nellore. Labiaplasty, Vaginoplasty, and Hymenoplasty by expert female surgeons.",
        "tagline": "Reclaim your physical comfort and intimate confidence in a completely private, judgment-free environment.",
        "hero_stats": [
            {"value": "100%", "label": "Confidentiality"},
            {"value": "Female", "label": "Care Team Options"},
            {"value": "High", "label": "Satisfaction Rate"},
        ],
        "highlight_cards": [
            {"icon": "bi-flower2", "title": "Labiaplasty", "text": "Surgical reduction of elongated labia minora for relief from chafing and discomfort."},
            {"icon": "bi-flower1", "title": "Vaginoplasty", "text": "Tightening of the vaginal canal and muscles stretched by childbirth."},
            {"icon": "bi-shield-check", "title": "Hymenoplasty", "text": "Cosmetic restoration of the hymen performed with absolute medical discretion."},
            {"icon": "bi-lightning-charge", "title": "Non-Surgical RF", "text": "Radiofrequency treatments for mild laxity and improved tissue health without surgery."},
        ],
        "overview_paragraphs": [
            "Changes to intimate areas due to childbirth, aging, or genetics are incredibly common, yet rarely discussed. These changes can cause chronic physical discomfort during exercise or intercourse, and significant emotional self-consciousness.",
            "Our intimate wellness suite offers a compassionate, safe space to address these concerns. Procedures like Labiaplasty remove excess, pinching tissue, while Vaginoplasty physically repairs and tightens separated vaginal muscles.",
            "We uphold the strictest standards of patient privacy and confidentiality. Your consultations, records, and procedures are guarded with absolute discretion, ensuring you feel comfortable and respected at every step."
        ],
        "ideal_candidates": [
            "Women experiencing pain, twisting, or chafing of labial tissue during sports or in tight clothing",
            "Mothers experiencing significant vaginal laxity or decreased sensation after vaginal childbirth",
            "Women feeling self-conscious about the aesthetic appearance of their intimate area",
            "Patients seeking cultural or personal restoration via Hymenoplasty",
            "Healthy adults seeking to improve their intimate quality of life"
        ],
        "glance": {
            "duration": "1 - 2 Hours",
            "anaesthesia": "Local with Sedation or General",
            "recovery": "3 - 5 Days (No intercourse/tampons for 6 weeks)",
            "results_visible": "Immediate (Swelling subsides over 4 weeks)",
            "sessions": "1"
        },
        "procedure_steps": [
            {"icon": "bi-lock", "title": "Private Consultation", "description": "A completely confidential discussion of your physical symptoms and aesthetic goals."},
            {"icon": "bi-pen", "title": "Surgical Planning", "description": "Careful mapping to ensure enough tissue is removed for comfort, but enough remains for protection and sensation."},
            {"icon": "bi-scissors", "title": "Precision Excision", "description": "Using fine surgical instruments to trim tissue or tighten the internal muscular canal."},
            {"icon": "bi-node-minus", "title": "Dissolvable Sutures", "description": "The area is closed with ultra-fine, dissolvable stitches that do not need to be removed."},
            {"icon": "bi-house-heart", "title": "Comfortable Recovery", "description": "Patients go home the same day with specific hygiene protocols and pain management plans."}
        ],
        "before_after_cases": [
            {"title": "Labiaplasty", "description": "Reduction of protruding tissue that caused chronic pain during exercise."},
            {"title": "Vaginoplasty Post-Birth", "description": "Internal tightening restoring friction and resolving mild stress incontinence."},
            {"title": "Hymenoplasty", "description": "Successful, discreet structural restoration."}
        ],
        "faqs": [
            {"question": "Is labiaplasty purely cosmetic?", "answer": "No. While it improves aesthetics, the vast majority of our patients request it because long tissue gets pulled, twisted, or chafed during running, cycling, or wearing yoga pants, causing actual physical pain."},
            {"question": "Will surgery decrease my sensitivity?", "answer": "No. The incisions are made very carefully to avoid the nerve-dense areas (like the clitoris). In fact, Vaginoplasty often increases sexual satisfaction by restoring proper muscle tone and friction."},
            {"question": "When can I exercise or have intercourse again?", "answer": "Light walking is fine after a few days, but you must avoid vigorous exercise, swimming, using tampons, and sexual intercourse for a strict 6-week period to allow the delicate tissues to heal completely."}
        ]
    },

    # ════════════ 11. GYNECOMASTIA (MALE CHEST) ════════════
    "gynecomastia": {
        "name": "Gynecomastia (Male Chest Reduction)",
        "category": "Body Contouring",
        "icon": "🛡️",
        "meta_description": "Gynecomastia surgery in Nellore. Expert male breast reduction combining PAL liposuction and gland excision for a flat, masculine chest.",
        "tagline": "Permanently eliminate 'man boobs' and reclaim a flat, firm, and masculine chest contour.",
        "hero_stats": [
            {"value": "100%", "label": "Permanent Fix"},
            {"value": "Hidden", "label": "Areolar Scars"},
            {"value": "PAL", "label": "Lipo Technology"},
        ],
        "highlight_cards": [
            {"icon": "bi-scissors", "title": "Gland Excision", "text": "Surgical removal of the hard, rubbery glandular tissue beneath the nipple."},
            {"icon": "bi-lightning-charge", "title": "PAL Liposuction", "text": "Power-Assisted fat removal to sculpt the surrounding chest wall smoothly."},
            {"icon": "bi-arrows-angle-contract", "title": "Skin Tightening", "text": "Advanced techniques to ensure the chest skin shrinks tight to the new muscle contour."},
            {"icon": "bi-person-bounding-box", "title": "Masculine Definition", "text": "Focusing on revealing the natural shape of the underlying pectoral muscles."},
        ],
        "overview_paragraphs": [
            "Gynecomastia, the enlargement of male breast tissue, affects millions of men and can cause severe social anxiety, preventing them from taking off their shirts at the beach or wearing fitted clothing. It is caused by a mix of excess fat and enlarged glandular tissue.",
            "Because glandular tissue is dense and rubbery, no amount of diet or chest workouts will make it disappear. Surgery is the only effective, permanent cure.",
            "Dr. Rao uses a highly effective dual-approach: PAL Liposuction is used to remove the fatty deposits and sculpt the chest wall, followed by a tiny, hidden incision around the areola to physically pull out the stubborn gland. The result is a permanently flat, masculine chest."
        ],
        "ideal_candidates": [
            "Men bothered by the appearance of enlarged breasts ('man boobs')",
            "Individuals with puffy or protruding nipples caused by glandular tissue",
            "Men whose chest size has not improved despite rigorous weightlifting and fat loss",
            "Healthy males whose breast development has stabilized",
            "Those who avoid swimming or tight clothing due to chest embarrassment"
        ],
        "glance": {
            "duration": "1.5 - 2 Hours",
            "anaesthesia": "General or Local with IV Sedation",
            "recovery": "3 - 5 Days (Compression vest for 4 weeks)",
            "results_visible": "Immediate flattening (Swelling hides final definition for 6 weeks)",
            "sessions": "1"
        },
        "procedure_steps": [
            {"icon": "bi-pen", "title": "Pectoral Mapping", "description": "Marking the borders of the gland, the fat deposits, and the natural line of the pectoral muscle."},
            {"icon": "bi-droplet", "title": "Liposuction Contouring", "description": "Using a tiny cannula to vacuum out the soft fat surrounding the gland to flatten the chest."},
            {"icon": "bi-scissors", "title": "Gland Removal", "description": "Making a tiny, semi-circular incision at the border of the nipple to pull out the hard glandular disk."},
            {"icon": "bi-bandaid", "title": "Closure", "description": "Suturing the edge of the areola. The scar blends perfectly into the color change of the nipple."},
            {"icon": "bi-layers", "title": "Compression Vest", "description": "Putting on a tight surgical vest that forces the skin to heal flat against the chest wall."}
        ],
        "before_after_cases": [
            {"title": "Puffy Nipple Correction", "description": "Removal of a small gland causing a pointed, puffy look through t-shirts."},
            {"title": "Severe Gynecomastia", "description": "Removal of heavy fat and massive glands, restoring a completely flat chest."},
            {"title": "Asymmetrical Chest", "description": "Correction of a chest where only the left side had developed breast tissue."}
        ],
        "faqs": [
            {"question": "Will the breasts grow back?", "answer": "No. The glandular tissue is physically removed from the body and cannot regenerate. As long as you avoid extreme weight gain or the use of anabolic steroids (which can cause new gland growth), the results are permanent."},
            {"question": "Will I have a large scar?", "answer": "For 90% of cases, the only scar is a tiny crescent shape right on the border of the dark areola skin and the normal chest skin. It blends in so well that it is virtually invisible. Only extremely severe cases with massive skin sagging require larger scars."},
            {"question": "When can I go to the gym?", "answer": "You can return to light cardio (like a stationary bike) after 2 weeks. However, you must avoid heavy chest workouts (bench press, pushups) for 4 to 6 weeks to allow the muscle wall to heal completely."}
        ]
    }
}

# ── Helper: list all services grouped by category ──────────
SERVICE_CATEGORIES = {
    "Plastic Surgery":   ["plastic-surgery"],
    "Facial Surgery":    ["facelift", "rhinoplasty", "aesthetics"],
    "Body Contouring":   ["liposuction", "tummy-tuck-body-lift", "gynecomastia"],
    "Breast & Chest":    ["breast-surgery"],
    "Hair & Skin":       ["hair-transplantation", "laser"],
    "Intimate Wellness": ["intimate-wellness"],
}