import unittest
import NitterFollows

class TestBasicUsage(unittest.TestCase):
    def test_follow_parsing(self):
        self.assertEqual(NitterFollows.parse_followers_txt("FOLLOWERS.txt"), 
        ["Mental Outlaw", "Luke Smith", "Joshua Moon", "wigger"])

if __name__ == "__main__":
    unittest.main()