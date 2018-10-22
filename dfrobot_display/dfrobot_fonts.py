# -*- coding:utf-8 -*-

import json

class Fonts:

  def __init__(self):
    self._haveFontsABC = False
    self._fontsABC = {}
    self._fontsABCWidth = 0
    self._fontsABCHeight = 0
    self._fontsABCFmt = ""

    self._haveExtensionFonts = False
    
    self._enableDefaultFonts = True

  def setFontsABC(self, fonts):
    self._haveFontsABC = True
    self._fontsABC = fonts.fonts
    self._fontsABCWidth = fonts.width
    self._fontsABCHeight = fonts.height
    self._fontsABCFmt = fonts.fmt

  def setExFonts(self, obj):
    self._haveExtensionFonts = True
    self._extensionFonts = obj
  
  def setEnableDefaultFonts(self, opt):
    if opt:
      self._enableDefaultFonts = True
    else:
      self._enableDefaultFonts = False

  def setExFontsFmt(self, width, height):
    if self._haveExtensionFonts:
      self._extensionFonts.setFmt(width, height)

  def getOneCharacter(self, c):
    w = 0
    h = 0
    fmt = "UNKNOW"
    rslt = []
    done = False
    if self._haveFontsABC and self._enableDefaultFonts:
      try:
        rslt = self._fontsABC[c]
        w = self._fontsABCWidth
        h = self._fontsABCHeight
        fmt = self._fontsABCFmt
        done = True
      except:
        # print("try get fonts ABC faild")
        pass
    if self._haveExtensionFonts and done == False:
      try:
        (rslt, w, h, fmt) = self._extensionFonts.getOne(c)
        done = True
      except:
        # print("try get unicode fonts faild")
        pass
    return (rslt, w, h, fmt)
