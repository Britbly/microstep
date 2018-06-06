from microbit import *

counter = 0

def numbasic( number ):
    while number == 1:
        display.set_pixel(0, 0, 9)
        sleep(200)
        display.set_pixel(1, 0, 9)
        sleep(200)
        display.set_pixel(2, 0, 9)
        sleep(200)
        display.set_pixel(2, 1, 9)
        sleep(200)
        display.set_pixel(2, 2, 9)
        sleep(200)
        display.set_pixel(2, 3, 9)
        sleep(200)
        display.set_pixel(2, 4, 9)
        sleep(200)
        display.set_pixel(1, 4, 9)
        display.set_pixel(3, 4, 9)
        sleep(200)
        display.set_pixel(0, 4, 9)
        display.set_pixel(4, 4, 9)
        sleep(1000)
        display.clear()
        number = 0
        
    while number == 2:
        display.set_pixel(0, 0, 9)
        sleep(200)
        display.set_pixel(1, 0, 9)
        sleep(200)
        display.set_pixel(2, 0, 9)
        sleep(200)
        display.set_pixel(2, 0, 9)
        sleep(200)
        display.set_pixel(4, 1, 9)
        sleep(200)
        display.set_pixel(3, 2, 9)
        sleep(200)
        display.set_pixel(2, 2, 9)
        sleep(200)
        display.set_pixel(1, 2, 9)
        sleep(200)
        display.set_pixel(0, 3, 9)
        sleep(200)
        display.set_pixel(0, 4, 9)
        sleep(200)
        display.set_pixel(1, 4, 9)
        sleep(200)
        display.set_pixel(2, 4, 9)
        sleep(200)
        display.set_pixel(3, 4, 9)
        sleep(200)
        display.set_pixel(4, 4, 9)
        sleep(1000)
        display.clear()
        number = 0
        
    while number == 3:
        display.set_pixel(0, 0, 9)
        sleep(200)
        display.set_pixel(1, 0, 9)
        sleep(200)
        display.set_pixel(2, 0, 9)
        sleep(200)
        display.set_pixel(3, 0, 9)
        sleep(200)
        display.set_pixel(4, 1, 9)
        sleep(200)
        display.set_pixel(3, 2, 9)
        display.set_pixel(2, 2, 9)
        sleep(200)
        display.set_pixel(4, 3, 9)
        sleep(200)
        display.set_pixel(3, 4, 9)
        sleep(200)
        display.set_pixel(2, 4, 9)
        sleep(200)
        display.set_pixel(1, 4, 9)
        sleep(200)
        display.set_pixel(0, 4, 9)
        sleep(200)


while True:
    numbasic( number = counter )
    if button_a.is_pressed():
        counter += 1
        
    if button_b.is_pressed():
        counter -= 1