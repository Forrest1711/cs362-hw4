import averageOfElements
import unittest


class avgElemTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(averageOfElements.avgElem(
            [4, 13, 26, 69, 119, 183]), 69)

    def test2(self):
        self.assertEqual(averageOfElements.avgElem([-10000, -420, 9160]), -420)

    def test3(self):
        self.assertEqual(averageOfElements.avgElem([]), 0)


if __name__ == '__main__':
    unittest.main()
