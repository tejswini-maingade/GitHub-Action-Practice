import unittest


class TestApplication(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(2 + 3, 5)

    def test_string(self):
        self.assertEqual("DevOps".upper(), "DEVOPS")


if __name__ == "__main__":
    unittest.main()
