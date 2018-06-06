from microbit import *
import radio

radio.on()

dot = Image("00000:"
            "00000:"
            "99999:"
            "00000:"
            "00000")

dash = Image("00000:"
            "09990:"
            "09990:"
            "09990:"
            "00000")

while True:
     sleep(10)
     income = radio.receive()
     
     if income == 'dot':
         display.show(dot)
         sleep(500)
         display.clear()
         income = " "
         
     if income == 'dash':
         display.show(dash)
         sleep(500)
         display.clear()
         income = " "