from microbit import *
import radio

radio.on()

steps = 0
xval = 0
yval = 0

while True:
    radio.on()
    xval = accelerometer.get_x()
    yval = accelerometer.get_y()

    
    
    if xval > 1536 or yval > 1536 or xval < -1536 or yval < -1536:

        steps += 1
        string_steps = str(steps)
        display.show(string_steps)
        sleep(1)
        radio.send(string_steps)
        radio.off()
        sleep(500)
        
    if button_b.is_pressed():
        
        steps = 0
        display.clear()
        display.show("Cleared")
        
        display.clear()
        