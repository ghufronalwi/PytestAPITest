import sys
import subprocess
import os
import webbrowser
from config import REPORT_PATH

def check_and_install_packages():
    missing_packages = []

    # List of packages to check
    required_packages = ["requests", "pytest", "jsonschema", "pytest_html"]

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"Missing packages: {', '.join(missing_packages)}. Installing them now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    else:
        print("All required packages are already installed.")

def run_tests():
  print("Running tests...")
  subprocess.run(["pytest"])

def open_report():
  report_path = os.path.abspath(REPORT_PATH)
  print(f"Opening report: {report_path}")
  webbrowser.open(f"file://{report_path}")

def main():
  check_and_install_packages()
  run_tests()
  open_report()

if __name__ == "__main__":
    main()