import os
import logging
from config import REPORT_PATH
import pytest
# import datetime

# Ensure logs directory exists
def ensure_logs_directory():
    logs_dir = 'logs'
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

# Configure logging
def pytest_configure(config):
    ensure_logs_directory()
    # timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
    # config.option.htmlpath = f"reports/test_{timestamp}_report.html"
    # config.option.htmlpath = "reports/test_report.html"
    config.option.htmlpath = REPORT_PATH
    config.option.self_contained_html = True
    logging.basicConfig(filename='logs/test.log', level=logging.INFO, format='%(message)s')

# Custom report title
# @pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Pytest API Test Report"

# # Hook to capture log messages and add them to the report
# @pytest.hookimpl(tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     if call.when == 'call':
#         log_message = ""
#         try:
#             with open('logs/test.log', 'r') as log_file:
#                 log_message = log_file.read()
#         except FileNotFoundError:
#             log_message = "Log file not found."
        
#         # Capture log details in the report
#         if call.excinfo is None:
#             item.extra = f"<div>{log_message}</div>"
#         else:
#             item.extra = f"<div>{log_message}</div><pre>{call.excinfo.typename}: {call.excinfo.value}</pre>"

# # Add log messages to the results summary
# @pytest.hookimpl(tryfirst=True)
# def pytest_html_results_summary(prefix, summary, postfix):
#     for item in prefix:
#         if hasattr(item, 'extra'):
#             summary.write(item.extra)
