#!/usr/bin/env python
"""
Redgum Tutoring - Application Launcher
This script starts the Flask development server.
"""
import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

try:
    import flask
    print(f"✓ Flask {flask.__version__} found")
except ImportError as e:
    print(f"✗ Error: Flask not installed - {e}")
    print("\nTo install Flask, run:")
    print("  pip install flask")
    sys.exit(1)

try:
    from app import app
    print("✓ App module imported successfully")
    print("\nStarting Redgum Tutoring Frontend...")
    print("Open your browser to: http://127.0.0.1:5000/")
    print("Press Ctrl+C to stop the server\n")
    app.run(debug=True)
except Exception as e:
    print(f"✗ Error starting app: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
