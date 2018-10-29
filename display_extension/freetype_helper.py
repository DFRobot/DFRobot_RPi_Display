# -*- coding:utf-8 -*-

'''
depends: freetype-py
'''

import freetype

class Freetype_Helper:

  def __init__(self, filePath):
    self._face = freetype.Face(filePath)
    self._width = 0
    self._height = 0

  def setFmt(self, width, height):
    self._width = int(width)
    self._height = int(height)
    self._face.set_pixel_sizes(width, height)

  def getOne(self, ch):
    self._face.load_char(ch)
    bitmap = self._face.glyph.bitmap
    width = bitmap.width
    height = bitmap.rows
    buffer = bitmap.buffer
    oneLineDataLen = (self._width - 1) // 8 + 1
    rsltLen = oneLineDataLen * self._height
    rslt = []
    if height < self._height:
      rslt = [0] * ((self._height - height) // 2 * oneLineDataLen)
      h = height
    else:
      h = self._height
    offset = 0
    if width < self._width:
      offset = (self._width - width) // 2
    for i in range(h):
      temp = [0] * oneLineDataLen
      for j in range(width):
        if j < self._width:
          if buffer[i * width + j] > 0x7f:
            temp[(j + offset) // 8] |= (0x80 >> ((j + offset) % 8))
      rslt += temp
    if len(rslt) < rsltLen:
      rslt += [0] * (rsltLen - len(rslt))
    return (rslt, self._width, self._height, "TBMLLR")
