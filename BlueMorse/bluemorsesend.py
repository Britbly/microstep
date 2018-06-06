from microbit import *
import radio

radio.on()

while True:
    radio.on()
    if button_a.is_pressed():
        sleep(1)
        radio.send('dot')
        radio.off()
        sleep(500)
    
    if button_b.is_pressed():
        sleep(1)
        radio.send('dash')
        radio.off()
        sleep(500)