import fullName
import unittest


class nameTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(fullName.fullName("Chris", "Evans"), "Chris Evans")

    def test2(self):
        self.assertEqual(fullName.fullName(
            "Toni", "Collette"), "Toni Collette")

    def test3(self):
        self.assertEqual(fullName.fullName("Agent", "47"), "Agent 47")


if __name__ == '__main__':
    unittest.main()
