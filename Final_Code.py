#!/usr/bin/env python
####TeCoEd - Pi HAT light sensor hack###

import unicornhat as UH
import time
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
 
TRIG = 23
ECHO = 24
UH.clear()

global distance

def measure():
    global distance
    print "Distance Measurement In Progress"
     
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
     
    GPIO.output(TRIG, False)
    print "Waiting For Sensor To Settle"
    time.sleep(0.5)
     
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
     
    while GPIO.input(ECHO)==0:
      pulse_start = time.time()
     
    while GPIO.input(ECHO)==1:
      pulse_end = time.time()
     
    pulse_duration = pulse_end - pulse_start
     
    distance = pulse_duration * 17150
     
    distance = round(distance, 2)
     
    print "Distance:",distance,"cm"

    print distance

    
def LED_response():
   global distance
   print ""
   distance = 400 - distance
   distance = distance / 400
   print distance
   #time.sleep(0.2)###test
   
   #distance = distance / 4
   print distance
   #time.sleep(0.3)
   
   bright = distance 
   print bright
   print "brightness", bright
   time.sleep(0.1) 
   GPIO.cleanup()
   #bright =  0.10
   UH.brightness(bright)

   for y in range(8):
     for x in range(8):
       UH.set_pixel(x,y, 255, 255, 255)
       UH.show()
       time.sleep(0.02)

UH.clear()

def LED_response_zero():
   GPIO.cleanup()
   bright =  0
   UH.brightness(bright)

   for y in range(8):
     for x in range(8):
       UH.set_pixel(x,y, 0, 0, 0)
       UH.show()
       time.sleep(0.01)

UH.clear()

while True:
  measure()
  if distance > 400:
      LED_response_zero()
      time.sleep(0.1)
      pass
  elif distance < 400:
      LED_response()
      time.sleep(0.1)      




