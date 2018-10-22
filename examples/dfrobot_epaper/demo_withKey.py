# -*- coding:utf-8 -*-
'''
file demo_withKey.py

connect epaper to your raspberryPi
after clear screen, click keyA or keyB, you can see "A" or "B" printed on your device

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

# get gpio interface
GPIO = dfrobot_epaper.GPIO
EPAPER_KEY_A = 21
EPAPER_KEY_B = 20
haveKeyA = False # key A down flag
haveKeyB = False # key B down flag

# GPIO output test
'''
GPIO_OUT_PIN = 16
pinOut = GPIO(GPIO_OUT_PIN, GPIO.OUT)
pinOut.setOut(GPIO.LOW)
pinOut.setOut(GPIO.HIGH)
'''

epaper = dfrobot_epaper.DFRobot_Epaper_SPI(RASPBERRY_SPI_BUS, RASPBERRY_SPI_DEV, RASPBERRY_PIN_CS, RASPBERRY_PIN_CD, RASPBERRY_PIN_BUSY) # create epaper object

# key A callback
def keyACallBack():
  global haveKeyA
  haveKeyA = True

# key B callback
def keyBCallBack():
  global haveKeyB
  haveKeyB = True 

# config keyA and keyB
keyA = GPIO(EPAPER_KEY_A, GPIO.IN) # set key to input
keyB = GPIO(EPAPER_KEY_B, GPIO.IN) # set key to input
keyA.setInterrupt(GPIO.FALLING, keyACallBack) # set key interrupt callback
keyB.setInterrupt(GPIO.FALLING, keyBCallBack) # set key interrupt callback

# clear screen
epaper.begin()
epaper.clear(epaper.WHITE)
epaper.flush(epaper.FULL)
time.sleep(1)

epaper.setText(2, epaper.BLACK, epaper.WHITE, 0, 0) # set text size, color, background, interval row, interval col

keyCount = 0
# key test
while True:
  if haveKeyA:
    keyCount += 1
    haveKeyA = False
    epaper.printStr("A")
    epaper.flush(epaper.PART)
  if haveKeyB:
    keyCount += 1
    haveKeyB = False
    epaper.printStr("B")
    epaper.flush(epaper.PART)
  if keyCount >= 16:
    keyCount = 0
    epaper.clear(epaper.WHITE)
    epaper.flush(epaper.PART)
    epaper.setTextCursor(0, 0) # set text cursor to origin
  time.sleep(0.01)
