import unittest
from unittest.mock import MagicMock, patch
from modules.logger import log_event, log_error, capture_screenshot, log_unhandled_question

class TestLogger(unittest.TestCase):

    def test_log_event(self):
        with patch('builtins.print') as mock_print:
            log_event("INFO", "Test message", {"key": "value"})
            self.assertTrue(mock_print.called)

    def test_log_error(self):
        with patch('builtins.print') as mock_print:
            try:
                raise ValueError("Test error")
            except Exception as e:
                log_error("An error occurred", e)
            self.assertTrue(mock_print.called)

    def test_capture_screenshot(self):
        browser = MagicMock()
        browser.save_screenshot.return_value = True
        capture_screenshot(browser, "testshot")
        browser.save_screenshot.assert_called()

    def test_log_unhandled_question(self):
        with patch('builtins.print') as mock_print:
            log_unhandled_question("What is your favorite color?")
            self.assertTrue(mock_print.called)

if __name__ == "__main__":
    unittest.main()