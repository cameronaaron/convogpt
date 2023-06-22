import unittest
from unittest.mock import patch
import json
from chatapp import ChatApp, JsonDataStore


class TestChatApp(unittest.TestCase):
    def setUp(self):
        self.user_id = "123"
        self.datastore = JsonDataStore("datastore.json")
        self.app = ChatApp(self.user_id, self.datastore)

    def test_generate_response_with_flirty_message(self):
        response = self.app.generate_response("Hey there ;)", "flirty", self.user_id)
        self.assertIn("Hey", response)
        self.assertIn("there", response)
        self.assertIn(";", response)

    def test_generate_response_with_professional_message(self):
        response = self.app.generate_response("Dear Sir/Madam,", "professional", self.user_id)
        self.assertIn("Thank", response)
        self.assertIn("regards", response)

    def test_generate_response_with_friendly_message(self):
        response = self.app.generate_response("What's up?", "friendly", self.user_id)
        self.assertIn("Not much", response)
        self.assertIn("you?", response)

    def test_run_with_user_input(self):
        with patch('builtins.input', side_effect=["1", "Hello", "friendly", self.user_id]):
            self.app.run()

    def test_save_user_profile(self):
        profile = {"name": "John", "age": 30}
        self.datastore.save_user_profile(self.user_id, profile)
        loaded_profile = self.datastore.load_user_profile(self.user_id)
        self.assertEqual(profile, loaded_profile)

    def test_save_conversation_history(self):
        conversation = [{"message": "Hello", "type": "friendly", "response": "Hi there!"}]
        self.datastore.save_conversation_history(self.user_id, conversation)
        loaded_conversation = self.datastore.load_conversation_history(self.user_id)
        self.assertEqual(conversation, loaded_conversation)

if __name__ == '__main__':
    unittest.main()