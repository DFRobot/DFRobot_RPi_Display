# -*- coding:utf-8 -*-

'''
depends: freetype-py
'''

import freetype
import math

class Freetype_Helper:

  def __init__(self, filePath):
    self._face = freetype.Face(filePath)
    self._width = 0
    self._height = 0
    self._fade = 96

  def setFmt(self, width, height):
    self._width = int(width)
    self._height = int(height)
    self._face.set_pixel_sizes(width, height)
  
  def setDisLowerLimite(self, limite):
    self._fade = limite

  def getOne(self, ch):
    self._face.load_char(ch)
    bitmap = self._face.glyph.bitmap
    originY = self._face.glyph.bitmap_top
    width = bitmap.width
    height = bitmap.rows
    buffer = bitmap.buffer
    oneLineDataLen = (width - 1) // 8 + 1
    rslt = []
    heightOffset = 0
    needAdd = False
    if (ord(ch) >= ord(" ") and ord(ch) <= ord("~")) or height < (self._height // 2):
      # heightOffset = math.floor(self._height * 4 / 5) - originY
      heightOffset = int((self._height * 8 + 5) // 10) - originY
      if heightOffset < 0:
        heightOffset = 0
      rslt += [0] * oneLineDataLen * heightOffset
      needAdd = True
    h = self._height
    if h > height:
      h = height
    for i in range(h):
      temp = [0] * oneLineDataLen
      for j in range(width):
        if buffer[i * width + j] > self._fade:
          needAdd = True
          temp[j // 8] |= 0x80 >> (j % 8)
      if needAdd:
        rslt += temp
    return (rslt, width, h + heightOffset, "TBMLLR")
