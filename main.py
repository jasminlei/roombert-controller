import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
def button_callback(channel):
    print("Button was pushed!")
def button_callback2(channel):
    print("iik!")
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 36 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(36,GPIO.RISING,callback=button_callback) # Setup event on pin 36 rising edge
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 36 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(37,GPIO.RISING,callback=button_callback2) # Setup event on pin 36 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up