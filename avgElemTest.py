import averageOfElements
import unittest


class avgElemTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(averageOfElements.avgElem([]), 69)

    def test2(self):
        self.assertEqual(averageOfElements.avgElem([]), -420)

    def test3(self):
        self.assertEqual(averageOfElements.avgElem([]), 666)


if __name__ == '__main__':
    unittest.main()
