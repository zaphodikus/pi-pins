import pytest
import unittest
from canvas import TextCanvas
from chiplayout import HeaderPin
from chip_data_raspi import CHIP_DATA as MODELB_DATA


class TestPinRotations(unittest.TestCase):

    def test_pin1(self):
        c = TextCanvas()
        p = [HeaderPin(MODELB_DATA[10][0], MODELB_DATA[10][1], MODELB_DATA[10][2], 2, 5),
             HeaderPin(MODELB_DATA[11][0], MODELB_DATA[11][1], MODELB_DATA[11][2], 2, 5)]
        s = [p[0].render_pin(orientation='U', justify_right=True),
             p[1].render_pin(orientation='U', justify_right=False)]
        widest = 22
        chip_width = 5
        c.draw_string(0, widest + 1, 'D', '+|||+')
        c.draw_string(2, widest + 1, 'D', '+|||+')

        for i in 0, 1:
            print(s[i])
        c.draw_string(1, widest*2+chip_width, 'U', s[0])
        c.draw_string(1, widest, 'U', s[1])
        print(c)
        self.assertEqual(2, c.width())
        self.assertEqual(50, c.height())
        #self.assertEqual(' ', c.__repr__())

