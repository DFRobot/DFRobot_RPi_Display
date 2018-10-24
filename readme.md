# DFRobot_Display
<pre>
library for graphics.
many display device of DFRobot depend on it.

this lib supports python3 and python2.
Chinese and English print available, other language untest.

usage:
download and unpack this lib to your raspberryPi
open your cmd window
change direction to the libs examples

use cmd:
python demo_xxxx.py
to run test
</pre>
## file strcture
------------------------------------------
<pre>
--dfrobot_display:
    __init__.py
    dfrobot_display.py
    dfrobot_fonts.py
    dfrobot_printString.py
--dfrobot_interface_raspberry:
    __init__.py
    dfrobot_raspberry_gpio.py
    dfrobot_raspberry_spi.py
    dfrobot_raspberry_i2c.py
--display_extension:
    __init__.py
    logo_colorbits1.bmp
    logo_colorbits24.bmp
    fonts_6_8.py
    fonts_8_16.py
    freetype_helper.py
    wqydkzh.ttf
--devices:
  __init__.py
  dfrobot_epaper.py
--examples:
    __init__.py
    --dfrobot_epaper
        __init__.py
        demo_graphics.py
        demo_bitmap.py
        demo_print.py
        demo_withKey.py
readme.md
</pre>
### devices
<pre>
driver for device
select driver that you need
</pre>
### dfrobot_display
library base, all must download
### dfrobot_interface_raspberry
interface for raspberry
### display_extension
optional files <br>

file | remark
---- | ------
logo_colorbits1.bmp | bmp file saved as bitcounts = 1
logo_colorbits24.bmp | bmp file saved as bitcounts = 24
fonts_6_8.py | bitmap for alphabet fonts, width = 6, height = 8 usage is [here](#fonts_x_x)
fonts_8_16.py | bitmap for alphabet fonts, width = 8, height = 16 usage is [here](#fonts_x_x)
freetype_helper.py | use it if you installed freetype-py(cmd: python3 -m pip install freetype-py), usage is [here](#Freetype_Helper)
wqydkzh.ttf | 文泉驿等宽正黑.ttf gpl license fonts file, use with freetype_helper.py

## library dfrobot_display

```py

class DFRobot_Display:

  WHITE24 = 0xffffff
  SILVER24 = 0xc0c0c0
  GRAY24 = 0x808080
  BLACK24 = 0x000000
  RED24 = 0xff0000
  MAROON24 = 0x800000
  YELLOW24 = 0xffff00
  OLIVE24 = 0x808000
  GREEN24 = 0x00ff00
  DARKGREEN24 = 0x008000
  CYAN24 = 0x00ffff
  BLUE24 = 0x0000ff
  NAVY24 = 0x000080
  FUCHSIA24 = 0xff00ff
  PURPLE24 = 0x800080
  TEAL24 = 0x008080

  WHITE16 = color24to16(WHITE24)
  SILVER16 = color24to16(SILVER24)
  GRAY16 = color24to16(GRAY24)
  BLACK16 = color24to16(BLACK24)
  RED16 = color24to16(RED24)
  MAROON16 = color24to16(MAROON24)
  YELLOW16 = color24to16(YELLOW24)
  OLIVE16 = color24to16(OLIVE24)
  GREEN16 = color24to16(GREEN24)
  DARKGREEN16 = color24to16(DARKGREEN24)
  CYAN16 = color24to16(CYAN24)
  BLUE16 = color24to16(BLUE24)
  NAVY16 = color24to16(NAVY24)
  FUCHSIA16 = color24to16(FUCHSIA24)
  PURPLE16 = color24to16(PURPLE24)
  TEAL16 = color24to16(TEAL24)

  WHITE = WHITE16
  SILVER = SILVER16
  GRAY = GRAY16
  BLACK = BLACK16
  RED = RED16
  MAROON = MAROON16
  YELLOW = YELLOW16
  OLIVE = OLIVE16
  GREEN = GREEN16
  DARKGREEN = DARKGREEN16
  CYAN = CYAN16
  BLUE = BLUE16
  NAVY = NAVY16
  FUCHSIA = FUCHSIA16
  PURPLE = PURPLE16
  TEAL = TEAL16

  BITMAP_TBMLLR = "TBMLLR"  # scan with row, top to bottom, msb to left, lsb to right
  BITMAP_TBMRLL = "TBMRLL"  # scan with row, top to bottom, msb to right, lsb to left
  BITMAP_BTMLLR = "BTMLLR"  # scan with row, bottom to top, msb to left, lsb to right
  BITMAP_BTMRLL = "BTMRLL"  # scan with row, bottom to top, msb to right, lsb to left
  BITMAP_LRMTLB = "LRMTLB"  # scan with column, left to right, msb to top, lsb to bottom
  BITMAP_LRMBLT = "LRMBLT"  # scan with column, left to right, msb to bottom, lsb to top
  BITMAP_RLMTLB = "RLMTLB"  # scan with column, right to left, msb to top, lsb to bottom
  BIMTAP_RLMBLT = "RLMBLT"  # scan with column, right to left, msb to bottom, lsb to top
  BITMAP_UNKNOW = "UNKNOW"  # unknow bitmap scan type

  '''
    init class
    @param width        screen width
           height       screen height
  '''
  def __init__(self, width, height):
  

  '''
    set color to format RBG565
    use for lcd
  '''
  def setColorTo16(self):

  '''
    set color to format RBG888
    use for lcd
  '''
  def setColorTo24(self):
  
  '''
    set line width
    @param w        line width
  '''
  def setLineWidth(self, w):

  '''
    set default fonts format (no effert to extension fonts)
    @param size           text size
           color          text color
           background     text background
           intervalRow    text interval with row
           intervalCol    text interval with column
  '''
  def setText(self, size, color, background, intervalRow, intervalCol):

  '''
    set text print cursor
    @param x        position x
           y        position y
  '''
  def setTextCursor(self, x, y):

  '''
    set bitmap size
    @param size       bitmap size
  '''
  def setBitmapSize(self, size):

  '''
    set bitmap format
    @param fmt        bitmap fmt, optional: BITMAP_XXXXXX
  '''
  def setBitmapFmt(self, fmt):

  '''
    set extension fonts class
    @param obj        fonts class like freetype_helper

    eg: setExFonts(Freetype_Helper("your file path"))
  '''
  def setExFonts(self, obj):

  '''
    set extension fonts format
    @param width        fonts width
           height       fonts height
  '''
  def setExFontsFmt(self, width, height):

  '''
    draw oen pixel
    @param x        position x
           y        position y
           color    color
  '''
  def pixel(self, x, y, color):
  
  '''
    clear screen with color
    @param color        color
  '''
  def clear(self, color):
  
  '''
    draw a vertical line
    @param x        position x
           y        position y
           h        length
           color    color
  '''
  def VLine(self, x, y, h, color):
  
  '''
    draw a horizontal line
    @param x        position x
           y        position y
           w        width
           color    color
  '''
  def HLine(self, x, y, w, color):
  
  '''
    draw a line
    @param x        position x
           y        position y
           x1       position x1
           y1       position y1
           color    color
  '''
  def line(self, x, y, x1, y1, color):
  
  '''
    draw a triangle
    @param x        position x
           y        position y
           x1       position x1
           y1       position y1
           x2       position x2
           y2       position y2
           color    color
  '''
  def triangle(self, x, y, x1, y1, x2, y2, color):
  
  '''
    draw a fill triangle
    @param x        position x
           y        position y
           x1       position x1
           y1       position y1
           x2       position x2
           y2       position y2
           color    color
  '''
  def fillTriangle(self, x, y, x1, y1, x2, y2, color):
  
  '''
    draw a rectangle
    @param x        position x
           y        position y
           w        widht
           h        height
           color    color
  '''
  def rect(self, x, y, w, h, color):
  
  '''
    draw a fill rectangle
    @param x        position x
           y        position y
           w        width
           h        height
           color    color
  '''
  def fillRect(self, x, y, w, h, color):

  QUADRANT_1 = 1
  QUADRANT_2 = 2
  QUADRANT_3 = 4
  QUADRANT_4 = 8
  QUADRANT_ALL = 15
  
  '''
    draw a circle with optional quadrant
    @param x        position x
           y        position y
           r        radius
           quadrant quadrant
           color    color
  '''
  def circleHelper(self, x, y, r, quadrant, color):
  
  '''
    draw a circle
    @param x        position x
           y        position y
           r        radius
           color    color
  '''
  def circle(self, x, y, r, color):
  
  '''
    draw a fill circle with optional quadrant
    @param x        position x
           y        position y
           r        radius
           quadrant quadrant
           color    color
  '''
  def fillCircleHelper(self, x, y, r, quadrant, color):
  
  '''
    draw a fill circle
    @param x        position x
           y        position y
           r        radius
           color    color
  '''
  def fillCircle(self, x, y, r, color):
  
  '''
    draw a round rectangle
    @param x        position x
           y        position y
           w        width
           h        height
           r        radius
           color    color
  '''
  def roundRect(self, x, y, w, h, r, color):
  
  '''
    draw a fill round rectangle
    @param x        position x
           y        position y
           w        width
           h        height
           color    color
  '''
  def fillRoundRect(self, x, y, w, h, r, color):
  
  '''
    draw a bitmap
    @param x            position x
           y            position y
           bitmap       bitmap data
           w            bitmap width
           h            bitmap height
           color        color for bit == 1
           background   color for bit == 0
  '''
  def bitmap(self, x, y, bitmap, w, h, color, background):
  
  '''
    draw bitmap file
    @param x        position x
           y        position y
           path     file path(support bitcounts: 1, 24)
  '''
  def bitmapFile(self, x, y, path):
  
  '''
    print one char on screen
    @param c        char that will be print
  '''
  def writeOneChar(self, c):
  
  BIN = bin
  OCT = oct
  DEC = lambda x : str(x)
  HEX = hex

  '''
    print object
    @param c        string
  '''
  def printStr(self, c):
  
  '''
    print object with new line
    @param c        object, if c is number, num can set to format
  '''
  def printStrLn(self, c, num = DEC):
  
  '''
    set default alphabet enable or disable
    @param opt        True to enable, False to disable
  '''
  def setEnableDefaultFonts(self, opt):
  
```

## examples
-----------------------------------------------
### epaper
```py
class DFRobot_Epaper_SPI:
  FULL = True
  PART = False

  '''
  class init
  @param bus        spi peripheral bus
         dev        spi peripheral device
         cs         cs pin
         cd         cd pin
         busy       busy pin
  '''
  def __init__(self, bus, dev, cs, cd, busy):
  
  '''
    device begin
  '''
  def begin(self):
  
  '''
    flush device
    @param mode       optional mode: FULL, PART
  '''
  def flush(self, mode):
  
```

## display_extension
------------------------------------------------
### Freetype_Helper

```py
class Freetype_Helper:

  '''
    class init, please note that documents cant infringe
    @param filePath       your file path
  '''
  def __init__(self, filePath):
  
  '''
    set fonts width and height
    @param width        width
           height       height
  '''
  def setFmt(self, width, height):
  
  '''
    get one font
    @param ch       
  '''
  def getOne(self, ch):
  
```

### fonts_x_x
<pre>
eg:
  import fonts_x_x
  DFRobot_Display.setFontsABC(fonts_x_x)
  DFRobot_Display.printStr("ABC")
</pre>

[top](#DFRobot_Display)
