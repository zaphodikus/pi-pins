#
import copy
from chiplayout import _orientations

class TextCanvasBase(object):
    def __init__(self, separator='', blank=' '):
        self._width = self._height = 1
        self._buffer = [[blank]]
        self.separator = separator
        self.blank = blank

    def set_at(self, x: int, y: int, char):
        if len(char) > 1:
            for idx in range(0, len(char)):
                self.set_at(x+idx, y, char[idx])
            return
        # if y > self._height-1:
        #      self._buffer.extend([[self.blank]] * (y + 1 - self._height))
        #      self._height = y+1
        while y > self._height-1:
             self._buffer.extend([[self.blank]])
             self._height += 1
        if x > len(self._buffer[y]) - 1:
            self._buffer[y].extend([self.blank] * (x + 1 - len(self._buffer[y])))
        if x > self._width - 1:
            self._width = x+1
        self._buffer[y][x] = char

    def height(self):
        return self._height

    def width(self):
        return self._width

    def __repr__(self):
        r = self.separator.join(["".join(char) for char in self._buffer])
        return r


class TextCanvas(TextCanvasBase):
    def __init__(self, separator='\n'):
        super().__init__(separator=separator)

    def draw_string(self, x: int, y:int, direction:str, text:str):
        assert direction in _orientations
        if direction == 'U':
            for y_pixel in range(y, y-len(text), -1):
                assert y_pixel >= 0
                self.set_at(x, y_pixel, text[0])
                text = text[1:]
        elif direction == 'D':
            for y_pixel in range(y, y+len(text)):
                self.set_at(x, y_pixel, text[0])
                text = text[1:]
        else:
            assert False  # unimplemented!

    def flipped_vert(self):
        """
        returns a new canvas object
        :return:
        """
        result = copy.deepcopy(self)
        for h in range(0, self.height()):
            result._buffer[h] = self._buffer[self.height()-h-1]
        return result

    def flipped_horz(self):
        """
        returns a new canvas object
        :return:
        """
        result = copy.deepcopy(self)
        for h in range(0, self.height()):
            # pad right
            row = result._buffer[h][::-1]
            while len(row) < self.width():
                row.insert(0, self.blank)
            result._buffer[h] = row
        return result

    def _shifted_right(self, count=1):
        result = copy.deepcopy(self)
        for h in range(0, self.height()):
            # pad left
            result._buffer[h].insert(0, self.blank * count)
        result._width += count
        return result

    def _shifted_down(self, count=1):
        result = copy.deepcopy(self)
        result._buffer = result._buffer[:0] + [[char] for char in (self.blank * count)] + result._buffer[0:]
        result._height += count
        return result

