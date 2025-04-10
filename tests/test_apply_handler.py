import unittest
from unittest.mock import MagicMock
from modules.apply_handler import is_resume_upload_needed, click_next_or_review, click_submit

class TestApplyHandler(unittest.TestCase):

    def setUp(self):
        self.browser = MagicMock()

    def test_is_resume_upload_needed_false(self):
        self.browser.find_element.side_effect = Exception("No upload prompt")
        result = is_resume_upload_needed(self.browser)
        self.assertFalse(result)

    def test_click_next_or_review_no_button(self):
        self.browser.find_element.side_effect = Exception("No button")
        result = click_next_or_review(self.browser)
        self.assertFalse(result)

    def test_click_submit_no_button(self):
        self.browser.find_element.side_effect = Exception("No submit button")
        try:
            click_submit(self.browser)
        except Exception:
            self.fail("click_submit() raised Exception unexpectedly!")

if __name__ == "__main__":
    unittest.main()