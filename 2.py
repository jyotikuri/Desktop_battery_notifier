import psutil
from plyer import notification
import pyttsx3
import time

def speak_message(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def battery_notifier():
    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged

        if percent < 20 and not plugged:
            notification.notify(
                title="Low Battery Alert",
                message="Battery is below 20%. Please plug in your charger!",
                timeout=60
            )
            speak_message("Battery is below 20%. Please plug in your charger!")
        elif percent == 99 and plugged:
            notification.notify(
                title="Battery Full",
                message="Battery is fully charged. Please unplug your charger!",
                timeout=60
            )
            speak_message("Battery is fully charged. Please unplug your charger!")
        time.sleep(300)  # Check every 60 seconds

battery_notifier()