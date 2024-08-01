import time
import board
import neopixel
import digitalio
from adafruit_debouncer import Debouncer

# Define the pin connected to the LED matrix
PIXEL_PIN = board.GP15

# Define the number of pixels (8x8)
NUM_PIXELS = 64

# Define the order of pixel colors
ORDER = neopixel.GRB

# Create the NeoPixel object
pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, brightness=0.2, auto_write=False, pixel_order=ORDER)

# Define the pins connected to the buttons
RESET_PIN = board.GP14
SNOOZE_PIN = board.GP13
ONOFF_PIN = board.GP12

# Create the button objects
reset_button = Debouncer(digitalio.DigitalInOut(RESET_PIN), interval=0.01)
snooze_button = Debouncer(digitalio.DigitalInOut(SNOOZE_PIN), interval=0.01)
onoff_button = Debouncer(digitalio.DigitalInOut(ONOFF_PIN), interval=0.01)

# Define the timer
timer = 2 * 60 * 60  # 2 hours

# Define the system state
system_on = True

# Define the animation state
animation_on = False

# Main loop
while True:
    # Update the button states
    reset_button.update()
    snooze_button.update()
    onoff_button.update()

    # Check if the reset button was pressed
    if reset_button.fell:
        # Turn off the LEDs
        pixels.fill((0, 0, 0))
        pixels.show()

        # Start the timer for 2 hours
        timer = time.monotonic() + 2 * 60 * 60

    # Check if the snooze button was pressed
    if snooze_button.fell:
        # Turn off the LEDs
        pixels.fill((0, 0, 0))
        pixels.show()

        # Start the timer for 5 minutes
        timer = time.monotonic() + 5 * 60

    # Check if the on/off button was pressed
    if onoff_button.fell:
        # Toggle the system state
        system_on = not system_on

        # If the system is off
        if not system_on:
            # Turn off the LEDs
            pixels.fill((0, 0, 0))
            pixels.show()

    # If the system is on
    if system_on:
        # If the timer has expired
        if time.monotonic() > timer:
            # Start the animation
            animation_on = True

            # Animate the LEDs
            for i in range(NUM_PIXELS):
                pixels[i] = (255, 0, 0)
                pixels.show()
                time.sleep(1)

            # Turn off the LEDs
            pixels.fill((0, 0, 0))
            pixels.show()

            # Start the timer for 5 minutes
            timer = time.monotonic() + 5 * 60

            # Stop the animation
            animation_on = False
