# -*- coding:utf-8 -*-
'''
file demo_graphics.py

connect epaper to your raspberryPi
basic graphics demo, such as line, rectangle, triangle, circle and pixel

Copyright   [DFRobot](http://www.dfrobot.com), 2016
Copyright   GNU Lesser General Public License

version  V1.0
date  2018-10-27
'''

import sys
sys.path.append("../..") # set system path to top

from devices import dfrobot_epaper
import time

# peripheral params
RASPBERRY_SPI_BUS = 0
RASPBERRY_SPI_DEV = 0
RASPBERRY_PIN_CS = 27
RASPBERRY_PIN_CD = 17
RASPBERRY_PIN_BUSY = 4

epaper = dfrobot_epaper.DFRobot_Epaper_SPI(RASPBERRY_SPI_BUS, RASPBERRY_SPI_DEV, RASPBERRY_PIN_CS, RASPBERRY_PIN_CD, RASPBERRY_PIN_BUSY) # create epaper object

# clear screen and set line width to 3
epaper.begin()
epaper.clear(epaper.WHITE)
epaper.flush(epaper.FULL)
epaper.setLineWidth(3)
time.sleep(1)

for i in range(10, 50):
  epaper.pixel(10, i * 2, epaper.BLACK)

epaper.line(20, 20, 20, 100, epaper.BLACK)
epaper.line(40, 20, 60, 100, epaper.BLACK)
epaper.line(60, 20, 40, 100, epaper.BLACK)

epaper.rect(80, 20, 40, 80, epaper.BLACK)
epaper.fillRect(90, 30, 20, 60, epaper.BLACK)

epaper.circle(150, 30, 20, epaper.BLACK)
epaper.fillCircle(150, 30, 15, epaper.BLACK)

epaper.roundRect(130, 60, 40, 40, 10, epaper.BLACK)
epaper.fillRoundRect(140, 70, 20, 20, 5, epaper.BLACK)

epaper.triangle(210, 20, 190, 100, 230, 100, epaper.BLACK)
epaper.fillTriangle(210, 40, 200, 90, 220, 90, epaper.BLACK)

epaper.flush(epaper.PART)
