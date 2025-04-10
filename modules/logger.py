import os
import time
import traceback
from datetime import datetime

def log_event(event_type, message, data=None):
    """
    Log an event with timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{event_type}] {message}")
    if data:
        print(f"Data: {data}")

def log_error(error_message, exception=None):
    """
    Log an error with optional exception traceback.
    """
    log_event("ERROR", error_message)
    if exception:
        traceback.print_exc()

def capture_screenshot(browser, filename_prefix="screenshot"):
    """
    Capture a screenshot with timestamped filename.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.png"
    browser.save_screenshot(filename)
    print(f"Screenshot saved: {filename}")

def manual_review_pause():
    """
    Pause execution for manual review.
    """
    input("Paused for manual review. Press Enter to continue...")

def log_unhandled_question(question_text):
    """
    Log an unhandled question for future improvements.
    """
    log_event("UNHANDLED_QUESTION", question_text)