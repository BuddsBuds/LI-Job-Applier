import os
import json
import unittest
from modules.personal_data import extract_resume_data, scrape_linkedin_profile, save_personal_data, load_personal_data

class TestPersonalData(unittest.TestCase):

    def setUp(self):
        self.test_config = "test_personal_data.json"
        self.resume_path = "/path/to/test_resume.pdf"
        self.profile_url = "https://www.linkedin.com/in/testprofile/"

    def tearDown(self):
        if os.path.exists(self.test_config):
            os.remove(self.test_config)

    def test_extract_resume_data(self):
        data = extract_resume_data(self.resume_path)
        self.assertIn("name", data)
        self.assertIn("skills", data)

    def test_scrape_linkedin_profile(self):
        data = scrape_linkedin_profile(self.profile_url)
        self.assertIn("headline", data)
        self.assertIn("skills", data)

    def test_save_and_load_personal_data(self):
        dummy_data = {"name": "Test User", "skills": ["Python", "Automation"]}
        save_personal_data(dummy_data, self.test_config)
        loaded = load_personal_data(self.test_config)
        self.assertEqual(dummy_data, loaded)

if __name__ == "__main__":
    unittest.main()