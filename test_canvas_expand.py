import pytest
import unittest
from canvas import TextCanvas


class TestCanvasExpanding(unittest.TestCase):

    def test_unity(self):
        c = TextCanvas()
        self.assertEqual(1, c.width())
        self.assertEqual(1, c.height())
        self.assertEqual(' ', c.__repr__())

    def test_grow_width(self):
        c = TextCanvas()
        c.set_at(0, 0, 'A')
        self.assertEqual(1, c.width())
        self.assertEqual(1, c.height())
        self.assertEqual("A", c.__repr__())

    def test_grow_width2(self):
        """
        A,B
        :return:
        """
        c = TextCanvas()
        c.set_at(0, 0, 'A')
        c.set_at(1, 0, 'B')
        self.assertEqual(2, c.width())
        self.assertEqual(1, c.height())
        self.assertEqual("AB", c.__repr__())

    def test_grow_width23(self):
        """
        A,B
        :return:
        """
        c = TextCanvas()
        c.set_at(0, 0, 'A')
        c.set_at(1, 0, 'B')
        c.set_at(4, 0, 'C')
        self.assertEqual("AB  C", c.__repr__())

    def test_linelength(self):
        c = TextCanvas()
        c.set_at(10, 1, 'B')
        c.set_at(10, 0, 'A')
        sep = c.separator
        self.assertEqual(f"          A{sep}          B", c.__repr__())

    def test_grow_height(self):
        """
        1
        A
        :return:
        """
        c = TextCanvas()
        c.set_at(0, 0, 'z')
        c.set_at(0, 1, 'A')
        sep = c.separator
        self.assertEqual(f"z{sep}A", c.__repr__())

    def test_overwrite(self):
        """

        :return:
        """
        # insertion/overwrite
        c = TextCanvas()
        c.set_at(0, 0, 'z')
        c.set_at(0, 0, '1')
        self.assertEqual(1, c.width())
        self.assertEqual(1, c.height())
        self.assertEqual("1", c.__repr__())

    def test_grow_height2(self):
        """
        A
        B
        C
        :return:
        """
        c = TextCanvas()
        c.set_at(0, 0, 'A')
        c.set_at(0, 1, 'B')
        c.set_at(0, 2, 'C')
        sep = c.separator
        self.assertEqual(f"A{sep}B{sep}C", c.__repr__())

    def test_grow_heightbackwards(self):
        """
        A
        B
        C
        D
        :return:
        """
        c = TextCanvas()
        c.set_at(0, 3, 'D')
        c.set_at(0, 2, 'C')
        c.set_at(0, 1, 'B')
        c.set_at(0, 0, 'A')
        sep = c.separator
        self.assertEqual(f"A{sep}B{sep}C{sep}D", c.__repr__())

    def test_grow_str(self):
        c = TextCanvas()
        sep = c.separator
        c.set_at(0, 0, '123')
        c.set_at(3, 0, '456')
        c.set_at(0, 1, 'ABC')
        self.assertEqual(6, c.width())
        self.assertEqual(2, c.height())
        self.assertEqual(f"123456{sep}ABC", c.__repr__())

    def test_multiline(self):
        c = TextCanvas()
        c.set_at(0, 0, 'A')
        c.set_at(0, 1, 'B')
        c.set_at(0, 2, 'C')
        sep = c.separator
        self.assertEqual(f"A{sep}B{sep}C", c.__repr__())

    def test_flip_vert(self):
        c = TextCanvas()
        c.set_at(0, 0, 'A')
        c.set_at(0, 1, 'B')
        d = c.flipped_vert()
        sep = c.separator
        self.assertEqual(f"B{sep}A", d.__repr__())

    def test_flip_horz(self):
        # flip a 1 char wide list
        c = TextCanvas()
        sep = c.separator
        c.set_at(0, 0, 'A')
        d = c.flipped_horz()
        self.assertEqual(f"A", d.__repr__())

        # flip 2 char wide
        c = TextCanvas()
        c.set_at(0, 0, 'AB')
        d = c.flipped_horz()
        self.assertEqual(f"BA", d.__repr__())

        # flip multiline
        # [A]     => [   A]
        # [___B]  => [B___]
        c = TextCanvas()
        c.set_at(0, 0, 'A')
        c.set_at(3, 1, 'B')
        d = c.flipped_horz()
        self.assertEqual(4, d.width())
        self.assertEqual(2, d.height())
        self.assertEqual(f"   A{sep}B   ", d.__repr__())

    def test_shift(self):
        # right
        c = TextCanvas()
        c.set_at(0, 0, 'A')
        c.set_at(3, 1, 'B')
        d = c._shifted_right()
        self.assertEqual(5, d.width())
        self.assertEqual(2, d.height())
        self.assertEqual(f" A\n    B", d.__repr__())
        # down
        d = c._shifted_down(2)
        self.assertEqual(4, d.width())
        self.assertEqual(4, d.height())
        self.assertEqual(f" \n \nA\n   B", d.__repr__())
