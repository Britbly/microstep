from microbit import *

times = 0

def screenflash( flash ):
	"Flashes the screen a certain number of times"
	count = 0
	fullscr = Image("99999:""99999:""99999:""99999:""99999:")
	
	while count < flash:
		sleep(100)
		display.show(fullscr)
		sleep(100)
		display.clear()
		count += 1
	return;

while True;
	if button_a.is_pressed():
		times += 1
		str_times = str(times)
		display.show(str_times)
		sleep(500)

	if button_b.is_pressed():
		times -= 1
		str_times = str(times)
		display.show(str_times)
		sleep(500)

	if pin0.is_touched():
	screenflash( flash = times )
