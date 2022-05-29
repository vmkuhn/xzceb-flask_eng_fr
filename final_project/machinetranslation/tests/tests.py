import unittest
import translator as trans

class TestStringMethods(unittest.TestCase):

    def test_french_to_english(self):
        self.assertEqual(trans.french_to_english(""),"")
        self.assertEqual(trans.french_to_english(None),None)
        self.assertEqual(trans.french_to_english('Bonjour'),'Hello')

    def test_english_to_french(self):
        self.assertEqual(trans.english_to_french(""),"")
        self.assertEqual(trans.english_to_french(None),None)
        self.assertEqual(trans.english_to_french('Hello'),'Bonjour')


if __name__ == '__main__':
    unittest.main()