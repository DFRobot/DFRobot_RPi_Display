# -*- coding:utf-8 -*-

import sys

class PrintString:

  def __init__(self):
    pass

  def writeOneChar(self, ch):
    pass

  def printStr(self, c):
    if sys.version_info.major == 2:
      c = c.decode("utf-8")
    else:
      try:
        c = str(c)
      except:
        return
    for i in c:
      self.writeOneChar(i)

  def printStrLn(self, c):
    self.printStr(c)
    self.writeOneChar("\n")
