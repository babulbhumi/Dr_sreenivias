import os
import sys

# Add your project directory to the sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Import your Flask app and map it to 'application' for Passenger
from app import app as application