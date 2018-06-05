from microbit import *
import radio

radio.on()

while True:
     sleep(10)
     income = radio.receive()
     
     if income:
         intcome = int(income)
         if intcome >= 10:
             display.scroll(income, delay=150, wait=True, loop=False, monospace=False)
             sleep(250)
             income = ""
         if intcome < 10:
             display.show(income)
             sleep(250)
             income = ""