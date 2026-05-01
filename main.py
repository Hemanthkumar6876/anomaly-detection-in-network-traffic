#!/usr/bin/env python3
"""
NetGuard - Advanced Network Anomaly Detection System
ML-powered network monitoring with VPN detection
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    try:
        from ui.app import NetGuardApp
        app = NetGuardApp()
        app.run()
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"Error starting NetGuard: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
