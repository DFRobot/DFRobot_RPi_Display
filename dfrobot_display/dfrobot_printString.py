# -*- coding:utf-8 -*-

import sys

class PrintString:

  BIN = bin
  OCT = oct
  DEC = lambda x : str(x)
  HEX = hex

  def __init__(self):
    pass

  def writeOneChar(self, ch):
    pass
  
  def writeStr(self, ch, num):
    pass

  def printStr(self, c, num = DEC):
    if type(c) == type(1):
      c = num(c)
    if sys.version_info.major == 2:
      c = c.decode("utf-8")
    else:
      try:
        c = str(c)
      except:
        return
    for i in c:
      self.writeOneChar(i)

  def printStrLn(self, c, num = DEC):
    self.writeStr(c, num)
    self.writeOneChar("\n")
