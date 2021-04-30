import cubeVol
import unittest


class CubeTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(cubeVol.cubeVol(12), 12*12*12)

    def test2(self):
        self.assertEqual(cubeVol.cubeVol(-6.66), -6.66*6.66*6.66)

    def test3(self):
        self.assertEqual(cubeVol.cubeVol("cube"), "cube"*"cube"*"cube")


if __name__ == '__main__':
    unittest.main()
