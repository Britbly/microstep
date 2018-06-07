from microbit import *

counter = -1

def numbasic( number ):
    if number == 0:
        display.set_pixel(2, 0, 9)
        display.set_pixel(1, 0, 9)
        display.set_pixel(3, 0, 9)
        display.set_pixel(0, 1, 9)
        display.set_pixel(4, 1, 9)
        display.set_pixel(0, 2, 9)
        display.set_pixel(4, 2, 9)
        display.set_pixel(0, 3, 9)
        display.set_pixel(4, 3, 9)
        display.set_pixel(1, 4, 9)
        display.set_pixel(3, 4, 9)
        display.set_pixel(2, 4, 9)
        sleep(1000)
        display.clear()
        number = -1
    
    if number == 1:
        display.set_pixel(0, 0, 9)
        display.set_pixel(1, 0, 9)
        display.set_pixel(2, 0, 9)
        display.set_pixel(2, 1, 9)
        display.set_pixel(2, 2, 9)
        display.set_pixel(2, 3, 9)
        display.set_pixel(2, 4, 9)
        display.set_pixel(1, 4, 9)
        display.set_pixel(3, 4, 9)
        display.set_pixel(0, 4, 9)
        display.set_pixel(4, 4, 9)
        sleep(1000)
        display.clear()
        number = -1
        
    if number == 2:
        display.set_pixel(0, 0, 9)
        display.set_pixel(1, 0, 9)
        display.set_pixel(2, 0, 9)
        display.set_pixel(2, 0, 9)
        display.set_pixel(4, 1, 9)
        display.set_pixel(3, 2, 9)
        display.set_pixel(2, 2, 9)
        display.set_pixel(1, 2, 9)
        display.set_pixel(0, 3, 9)
        display.set_pixel(0, 4, 9)
        display.set_pixel(1, 4, 9)
        display.set_pixel(2, 4, 9)
        display.set_pixel(3, 4, 9)
        display.set_pixel(4, 4, 9)
        sleep(1000)
        display.clear()
        number = -1
        
    if number == 3:
        display.set_pixel(0, 0, 9)
        display.set_pixel(1, 0, 9)
        display.set_pixel(2, 0, 9)
        display.set_pixel(3, 0, 9)
        display.set_pixel(4, 1, 9)
        display.set_pixel(3, 2, 9)
        display.set_pixel(2, 2, 9)
        display.set_pixel(4, 3, 9)
        display.set_pixel(3, 4, 9)
        display.set_pixel(2, 4, 9)
        display.set_pixel(1, 4, 9)
        display.set_pixel(0, 4, 9)
        sleep(1000)
        display.clear()
        number = -1

    if number == 4:
        display.set_pixel(0, 0, 9)
        display.set_pixel(3, 0, 9)
        display.set_pixel(0, 1, 9)
        display.set_pixel(3, 1, 9)
        display.set_pixel(0, 2, 9)
        display.set_pixel(3, 2, 9)
        display.set_pixel(0, 3, 9)
        display.set_pixel(1, 3, 9)
        display.set_pixel(2, 3, 9)
        display.set_pixel(3, 3, 9)
        display.set_pixel(4, 3, 9)
        display.set_pixel(3, 4, 9)
        sleep(1000)
        display.clear()
        number = -1
        
    if number == 5:
        display.set_pixel(4, 0, 9)
        display.set_pixel(3, 0, 9)
        display.set_pixel(2, 0, 9)
        display.set_pixel(1, 0, 9)
        display.set_pixel(0, 1, 9)
        display.set_pixel(0, 2, 9)
        display.set_pixel(1, 2, 9)
        display.set_pixel(2, 2, 9)
        display.set_pixel(3, 2, 9)
        display.set_pixel(4, 3, 9)
        display.set_pixel(3, 4, 9)
        display.set_pixel(2, 4, 9)
        display.set_pixel(1, 4, 9)
        display.set_pixel(0, 4, 9)
        display.clear()
        number = -1
        
    if number == 6:
        display.set_pixel(4, 0, 9)
        display.set_pixel(3, 0, 9)
        display.set_pixel(2, 0, 9)
        display.set_pixel(1, 0, 9)
        display.set_pixel(0, 1, 9)
        display.set_pixel(0, 2, 9)
        display.set_pixel(1, 2, 9)
        display.set_pixel(2, 2, 9)
        display.set_pixel(3, 2, 9)
        display.set_pixel(0, 3, 9)
        display.set_pixel(4, 3, 9)
        display.set_pixel(1, 4, 9)
        display.set_pixel(3, 4, 9)
        display.set_pixel(2, 4, 9)
        sleep(1000)
        display.clear()
        number = -1
        
    if number == 7:
        display.set_pixel(0, 0, 9)
        display.set_pixel(1, 0, 9)
        display.set_pixel(2, 0, 9)
        display.set_pixel(3, 0, 9)
        display.set_pixel(4, 0, 9)
        display.set_pixel(4, 1, 9)
        display.set_pixel(3, 2, 9)
        display.set_pixel(2, 3, 9)
        display.set_pixel(2, 4, 9)
        sleep(1000)
        display.clear()
        number = -1
        
    if number == 8:
        display.set_pixel(2, 0, 9)
        display.set_pixel(3, 0, 9)
        display.set_pixel(1, 0, 9)
        display.set_pixel(0, 1, 9)
        display.set_pixel(4, 1, 9)
        display.set_pixel(3, 2, 9)
        display.set_pixel(1, 2, 9)
        display.set_pixel(2, 2, 9)
        display.set_pixel(0, 3, 9)
        display.set_pixel(4, 3, 9)
        display.set_pixel(3, 4, 9)
        display.set_pixel(1, 4, 9)
        display.set_pixel(2, 4, 9)
        sleep(1000)
        display.clear()
        number = -1
        
    if number == 9:
        display.set_pixel(2, 0, 9)
        display.set_pixel(1, 0, 9)
        display.set_pixel(3, 0, 9)
        display.set_pixel(0, 1, 9)
        display.set_pixel(4, 1, 9)
        display.set_pixel(1, 2, 9)
        display.set_pixel(2, 2, 9)
        display.set_pixel(3, 2, 9)
        display.set_pixel(3, 2, 9)
        display.set_pixel(4, 2, 9)
        display.set_pixel(4, 3, 9)
        display.set_pixel(3, 4, 9)
        display.set_pixel(2, 4, 9)
        display.set_pixel(1, 4, 9)
        display.set_pixel(0, 4, 9)
        sleep(1000)
        display.clear()
        number = -1

    while number > 9:
		strnumber = str(number)
		for ch in strnumber:
			normalnumber = int(ch)
			numbasic(normalnumber)
		number = -1

while True:
    if button_b.is_pressed():
        counter += 1
        numbasic( number = counter )
        
    if button_a.is_pressed():
        counter -= 1
        numbasic( number = counter )