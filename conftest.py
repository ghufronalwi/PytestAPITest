import os
import logging
from config import REPORT_PATH

# Ensure logs directory exists
def ensure_logs_directory():
    logs_dir = 'logs'
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

# Configure logging
def pytest_configure(config):
    ensure_logs_directory()
    config.option.htmlpath = REPORT_PATH
    config.option.self_contained_html = True
    logging.basicConfig(filename='logs/test.log', level=logging.INFO, format='%(message)s')

# Custom report title
def pytest_html_report_title(report):
    report.title = "Pytest API Test Report"