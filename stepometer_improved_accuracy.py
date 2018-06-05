from microbit import *

steps = 0
xval = 0
yval = 0


while True:

    xval = accelerometer.get_x()
    yval = accelerometer.get_y()

    
    
    if xval > 1536 or yval > 1536 or xval < -1536 or yval < -1536:

        steps += 1
        display.show(Image.HAPPY)
        sleep(500)
        display.clear()

    if button_a.is_pressed():

        string_steps = str(steps)
        display.show(string_steps)
        sleep(500)
        display.clear()
        
    if button_b.is_pressed():
        
        steps = 0
        display.clear()
        display.show("Cleared")
        
        display.clear()
        