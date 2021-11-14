# generate pinout diagrams
#
#
#
from canvas import TextCanvas
from chiplayout import ChipLayout, HeaderPin
from chip_data_raspi import CHIP_DATA as MODELB_DATA

"""
                           .___.
                  +3V3---1-|O O|--2--+5V
          (SDA)  GPIO2---3-|O O|--4--+5V
         (SCL1)  GPIO3---5-|O O|--6--_
    (GPIO_GLCK)  GPIO4---7-|O O|--8-----GPIO14 (TXD0)
                      _--9-|O.O|-10-----GPIO15 (RXD0)
    (GPIO_GEN0) GPIO17--11-|O O|-12-----GPIO18 (GPIO_GEN1)
    (GPIO_GEN2) GPIO27--13-|O O|-14--_
    (GPIO_GEN3) GPIO22--15-|O O|-16-----GPIO23 (GPIO_GEN4)
                  +3V3--17-|O O|-18-----GPIO24 (GPIO_GEN5)
     (SPI_MOSI) GPIO10--19-|O.O|-20--_
     (SPI_MISO) GPIO9 --21-|O O|-22-----GPIO25 (GPIO_GEN6)
     (SPI_SCLK) GPIO11--23-|O O|-24-----GPIO8  (SPI_C0_N)
                      _-25-|O O|-26-----GPIO7  (SPI_C1_N)
       (EEPROM) ID_SD---27-|O O|-28-----ID_SC Reserved for ID EEPROM
                GPIO5---29-|O.O|-30--_
                GPIO6---31-|O O|-32-----GPIO12
                GPIO13--33-|O O|-34--_
                GPIO19--35-|O O|-36-----GPIO16
                GPIO26--37-|O O|-38-----GPIO20
                      _-39-|O O|-40-----GPIO21
                           '---'

"""


def pins():
    for pindata in MODELB_DATA:
        pin = HeaderPin(pindata[0], pindata[1], pindata[2] if len(pindata) > 2 else None)
        pin.render_pin(None, None, None, None)


def chips():
    chip = ChipLayout(MODELB_DATA, notch=False)
    canvas = TextCanvas()
    chip.render_chip(canvas, None, orientation='U')
    print(canvas)

    canvas = TextCanvas()
    chip.render_chip(canvas, None, orientation='D')
    print(canvas)
    print('-'*50)

    canvas = TextCanvas()
    chip.render_chip(canvas, None, orientation='L')
    print(canvas)
    print('-'*50)

    canvas = TextCanvas()
    chip.render_chip(canvas, None, orientation='R')
    print(canvas)
    print('-'*50)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #pins()
    chips()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
