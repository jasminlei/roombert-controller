import time
from miio import ViomiVacuum
import RPi.GPIO as GPIO
import os

IP = os.environ.get("VACCUUM_IP_ADDRESS")
TOKEN = os.environ.get("VACCUUM_TOKEN")
START_GPIO_NUMBER = int(os.environ.get("START_GPIO_NUMBER", "37"))
STOP_GPIO_NUMBER = int(os.environ.get("STOP_GPIO_NUMBER", "36"))

vaccuum = ViomiVacuum(IP, TOKEN)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def start_callback(_):
    vaccuum.start()
    time.sleep(1)

def stop_callback(_):
    vaccuum.stop()
    time.sleep(1)
    vaccuum.home()
    time.sleep(1)

def setup_button_with_callback(gpio_number, callback):
    GPIO.setup(gpio_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(gpio_number, GPIO.RISING, callback=callback)

setup_button_with_callback(START_GPIO_NUMBER, start_callback)
setup_button_with_callback(STOP_GPIO_NUMBER, stop_callback)

message = input("Press enter to quit\n\n")
GPIO.cleanup()

