import psutil
import time
import sys
platform_is_windows = sys.platform.startswith('win')
if platform_is_windows:
	from win10toast import ToastNotifier
else:
	import subprocess as sc

if platform_is_windows:
	def notify(title, msg):
		noti = ToastNotifier()
		noti.show_toast(title, msg, duration=10)
else:
	def notify(title, msg):
		sc.call(['notify-send', title, msg])

while True:
	batt = psutil.sensors_battery()

	if batt.percent <= 40 and batt.power_plugged is False:
		notify('Battery Low', 'Please plug-in a charger Sir')
	elif batt.percent >=80 and batt.power_plugged is True	:
		notify('Battery charged', 'Please remove the charger Sir')
	
	for __ in range(600):
		time.sleep(1)
