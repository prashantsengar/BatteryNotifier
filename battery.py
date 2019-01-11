import psutil
import time
#notify the thing

from win10toast import ToastNotifier

def notify(title, msg):
    noti = ToastNotifier()
    noti.show_toast(title, msg, duration=10)

while True:
	batt = psutil.sensors_battery()

	if batt.percent <= 40:
		notify('Battery Low', 'Please plug-in a charger Sir')
	elif batt.percent >=80 and batt.power_plugged is True	:
		notify('Battery charged', 'Please remove the charger Sir')
	
	for i in range(600):
		time.sleep(1)
