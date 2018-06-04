from microbit import *

steps = 0


while True:

	if accelerometer.was_gesture('shake'):
		steps += 1
		display.show(Image.YES)
		sleep(500)
		display.clear()

	if button_a.is_pressed():
		string_steps = str(steps)
		display.show(string_steps)
		sleep(500)
		display.clear()

	if button_b.is_pressed():
		steps = 0
		display.show("Cleared")
		display.clear()
