#
LEG_CHAR = '-'        # character for a leg
WIRE_CHAR = '-'       # character for a horizontal wire
LEG_HORZ_CHAR = 'M'   # character for a leg
WIRE_HORZ_CHAR = '|'  # character for a horizontal wire

"""
Upright-vertical, Downwards-vertical (180°), Left-to-right,  Right-to-left 
"""
_orientations = ['U', 'D', 'L', 'R']

""" 
 #=number
 N=name
 P=peripheral-name
"""
_details = '#NP'


class PinPrinter(object):
    def __init__(self, numbering_width, name_width,  orientation):
        """
        :param numbering_width:
        :param name_width:
        :param pin_char: char to use for pin on the chip
        :param line_char: char to use for line/hypenation
        """
        self.numbering_width = numbering_width
        self.name_widthe = name_width
        if orientation in ['U', 'D']:
            self.LEG_CHAR = LEG_CHAR
            self.WIRE_CHAR = WIRE_CHAR
        else:
            self.LEG_CHAR = LEG_HORZ_CHAR
            self.WIRE_CHAR = WIRE_HORZ_CHAR


# todo: declare a default static pinprinter that prints chips right-way up, for use by things
# like __repr__ that don't take args. Then move all the implementations to use the printer class

class HeaderPin(object):
    def __init__(self, number: int, name: str, peripheral=None, number_width=1, name_width=1):
        self._number = number
        self._name = name
        self._peripheral = peripheral
        self._number_width = number_width
        self._name_width = name_width

    def __repr__(self):
        return self.render_pin("U", self._number % 2)

    def render_pin(self, orientation, justify_right):
        assert orientation in _orientations
        prn = PinPrinter(0, 0, orientation)
        result = ""
        power = False
        name_pad = prn.WIRE_CHAR
        if '+' in self._name or 'GND' == self._name:
            power = True
        if power:
            name_pad = ' '
        if justify_right:  # left side
            if self._peripheral:
                result = "(" + self._peripheral + ") "

            if power:
                name = self._name.rjust(self._name_width, name_pad)
            else:
                name = self._name.ljust(self._name_width, name_pad)
            result = result + name + prn.WIRE_CHAR
            num = str(self._number).rjust(self._number_width, prn.WIRE_CHAR)
            result = result + num + prn.LEG_CHAR
        else:  # right side
            num = str(self._number).ljust(self._number_width, prn.WIRE_CHAR)
            result = prn.LEG_CHAR + num
            name = self._name.ljust(self._name_width, ' ')
            result = result + prn.WIRE_CHAR + name
            if self._peripheral:
                result = result + " (" + self._peripheral + ")"
            else:
                result = result.rstrip(prn.WIRE_CHAR)

        if orientation in ['L', 'R']:
            result = result.replace('_', '\'')
        return result

    # def render_pin(self, canvas, point, orientation, detail):
    #     print(f"[{self._number}][{self._name}][{self._peripheral}]")
    #     pass

# orientation 'U'p and 'D'own
CHIP_TOP_NOTCH = '\'-u-\''
CHIP_TOP_PLAIN = '.___.'
CHIP_BOTTOM_NOTCH = '\'-n-\''
CHIP_BOTTOM_PLAIN = '\'---\''

# orientations horizontal
CHIP_LEFT_NOTCH = '+|>|+'
CHIP_LEFT_PLAIN = '+|||+'
CHIP_RIGHT_NOTCH = '+|C|+'
CHIP_RIGHT_PLAIN = '+|||+'


class ChipLayout(object):
    def __init__(self, pins_data, notch=False):
        assert len(pins_data) % 2 == 0
        w0 = len(str(pins_data[-1][0]))
        w1 = 0
        w2 = 0  # unused
        for i in pins_data:
            # width of pin name
            if len(i[1]) > w1:
                w1 = len(i[1])
            # width of peripheral name
            if len(i) > 2 and len(i[2]) > w2:
                w2 = len(i[2])
        pins = [HeaderPin(pindata[0], pindata[1], pindata[2] if len(pindata) > 2 else None, w0, w1) for pindata in pins_data]

        self._pins = pins
        self._notch = notch

    def render_chip(self, canvas, point, orientation='U'):
        widest = len(str(self._pins[0]))
        for p in self._pins:
            if len(str(p)) > widest:
                widest = len(str(p))
        #border = ' '*widest
        assert orientation in _orientations
        if orientation in ['U', 'D']:
            row = 0
            if self._notch and orientation == 'U':
                canvas.set_at(widest, row, CHIP_TOP_NOTCH)
                #print(border + CHIP_TOP_NOTCH)
            else:
                canvas.set_at(widest, row, CHIP_TOP_PLAIN)
                #print(border + CHIP_TOP_PLAIN)
            row += 1
            if orientation == 'U':
                for r in range(int(len(self._pins)/2)):
                    line = f"{str(self._pins[r*2 + 0]):>{widest}}" + '|O O|' + str(self._pins[r*2 + 1])
                    canvas.set_at(0, row, line)
                    row += 1
                    #print(line)
            else:
                for r in range(int(len(self._pins)/2), 0, -1):
                    p1 = self._pins[r*2 - 1].render_pin(orientation=orientation, justify_right=True)
                    p2 = self._pins[r*2 - 2].render_pin(orientation=orientation, justify_right=False)
                    line = f"{p1:>{widest}}" + '|O O|' + p2
                    canvas.set_at(0, row, line)
                    row += 1
                    #print(line)

            if self._notch and orientation == 'D':
                canvas.set_at(widest, row, CHIP_BOTTOM_NOTCH)
                #print(border + CHIP_BOTTOM_NOTCH)
            else:
                canvas.set_at(widest, row, CHIP_BOTTOM_PLAIN)
                #print(border + CHIP_BOTTOM_PLAIN)
            row += 1
        elif orientation in ['L', 'R']:
            # draw to canvas a chip outline
            col = 0
            if self._notch and orientation == 'L':
                canvas.draw_string(col, widest, 'D', CHIP_LEFT_NOTCH)
            else:
                canvas.draw_string(col, widest, 'D', CHIP_LEFT_PLAIN)
            col += 1
            if orientation == 'L':
                for r in range(int(len(self._pins)/2)):
                    p1 = self._pins[r*2 + 1].render_pin(orientation=orientation, justify_right=True)
                    p2 = self._pins[r*2 + 0].render_pin(orientation=orientation, justify_right=False)
                    line = f"{p1:>{widest}}" + '-O O-' + p2
                    canvas.draw_string(col, 0, 'D', line)
                    col += 1
                    # last column?
                    if r < int(len(self._pins)/2) -1:
                        canvas.draw_string(col, widest, 'D', '-   -')
                        col += 1
            else:
                for r in range(int(len(self._pins) / 2), 0, -1):
                    p1 = self._pins[r * 2 - 2].render_pin(orientation=orientation, justify_right=True)
                    p2 = self._pins[r * 2 - 1].render_pin(orientation=orientation, justify_right=False)
                    line = f"{p1:>{widest}}" + '-O O-' + p2
                    canvas.draw_string(col, 0, 'D', line)
                    col += 1
                    # last column?
                    if r :
                        canvas.draw_string(col, widest, 'D', '-   -')
                        col += 1

            if self._notch and orientation == 'R':
                canvas.draw_string(col, widest, 'D', CHIP_RIGHT_NOTCH)
            else:
                canvas.draw_string(col, widest, 'D', CHIP_RIGHT_PLAIN)
            col += 1
