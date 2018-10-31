# -*- coding:utf-8 -*-
'''
file demo_print.py

connect epaper to your raspberryPi
print with fonts file

Copyright   [DFRobot](http://www.dfrobot.com), 2016
Copyright   GNU Lesser General Public License

version  V1.0
date  2018-10-27
'''

import sys
sys.path.append("../..") # set system path to top

from devices import dfrobot_epaper
import time

from display_extension.freetype_helper import Freetype_Helper

fontFilePath = "../../display_extension/wqydkzh.ttf" # fonts file

# peripheral params
RASPBERRY_SPI_BUS = 0
RASPBERRY_SPI_DEV = 0
RASPBERRY_PIN_CS = 27
RASPBERRY_PIN_CD = 17
RASPBERRY_PIN_BUSY = 4

epaper = dfrobot_epaper.DFRobot_Epaper_SPI(RASPBERRY_SPI_BUS, RASPBERRY_SPI_DEV, RASPBERRY_PIN_CS, RASPBERRY_PIN_CD, RASPBERRY_PIN_BUSY) # create epaper object

# clear screen
epaper.begin()
epaper.clear(epaper.WHITE)
epaper.flush(epaper.FULL)
time.sleep(1)

# config extension fonts
epaper.setExFonts(Freetype_Helper(fontFilePath)) # init with fonts file

# print test
epaper.setExFontsFmt(16, 16) # set extension fonts width and height
epaper.setTextCursor(0, 0)
epaper.printStr("df 成都极趣 epaper")
epaper.flush(epaper.PART)
time.sleep(1)

epaper.setExFontsFmt(24, 24) # set extension fonts width and height
epaper.setTextCursor(0, 20)
epaper.printStr("DF 墨水屏 EPAPER")
epaper.flush(epaper.PART)
time.sleep(1)

epaper.setExFontsFmt(32, 32) # set extension fonts width and height
epaper.setTextCursor(0, 48)
epaper.printStr("fast, safe and powerful")
epaper.flush(epaper.PART)
time.sleep(1)
