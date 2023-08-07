"""Test cases for QuadTree.py"""

import unittest
from QuadTree import *
# import QuadTree

class TestQuadTree(unittest.TestCase):
    def test_1(self):
        linear_1 = "GGGBWBWWGBBBWWGWGWBWBWGBBWBGGBWBWWGBWBWWGWGWBWBWGWBWB"
        expected = """X......X\n.X....X.\n..XXXX..\n...XX...\n...XX...\n..X..X..\n.X....X.\nX......X\n""".strip()
        self.assertEqual(decode(linear_1), expected)

    def test_2(self):
        linear_2 = "GGBGBBBWGWBBWBGBGBBBWGWBBWBGBGWBBWGWBBBGWWBBGBGWBBWGWWBBB"
        expected = """XXXXXXXX\nXX.XXX.X\nXX.XXX.X\nXX.XXX.X\nXX.XXX.X\nXX.XXX.X\nXX.....X\nXXXXXXXX\n""".strip()
        self.assertEqual(decode(linear_2), expected)

    def test_3(self):
        sample = """XXXXXXXX\nXX.XXX.X\nXX.XXX.X\nXX.XXX.X\nXX.XXX.X\nXX.XXX.X\nXX.....X\nXXXXXXXX\n""".strip()
        g = (str_to_grid(sample))
        t = build_quad_tree(g, 0, 0, 8)
        s = str(t)
        assert s == "GGBGBBBWGWBBWBGBGBBBWGWBBWBGBGWBBWGWBBBGWWBBGBGWBBWGWWBBB"

    def test_4(self):
        sample="""X......X\n.X....X.\n..XXXX..\n...XX...\n...XX...\n..X..X..\n.X....X.\nX......X\n""".strip()
        g = (str_to_grid(sample))
        t = build_quad_tree(g, 0, 0, 8)
        s = str(t)
        assert s == "GGGBWBWWGBBBWWGWGWBWBWGBBWBGGBWBWWGBWBWWGWGWBWBWGWBWB"


if __name__ == "__main__":
    unittest.main()