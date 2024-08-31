import time
import board
import neopixel
import digitalio

# Configuration des LEDs
num_pixels = 64
pixels = neopixel.NeoPixel(board.D18, num_pixels, auto_write=False)

# Configuration des boutons
buttons = {
    "onoff": digitalio.DigitalInOut(board.D2),
    "snooze": digitalio.DigitalInOut(board.D3),
    "reset": digitalio.DigitalInOut(board.D4)
}
for button in buttons.values():
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

# Variables de temps
TIMER_DURATION = 2 * 60 * 60  # 2 heures en secondes
SNOOZE_DURATION = 5 * 60  # 5 minutes en secondes
ANIMATION_DURATION = 60  # 1 minute en secondes

# Variables de contrôle
timer = 0
paused = False
animation_active = False

def reset_timer():
    global timer
    timer = time.monotonic() + TIMER_DURATION
    clear_leds()

def snooze_timer():
    global timer
    timer = time.monotonic() + SNOOZE_DURATION
    clear_leds()

def pause_system():
    global paused
    paused = not paused
    clear_leds()

def clear_leds():
    pixels.fill((0, 0, 0))
    pixels.show()

def start_animation():
    global animation_active
    animation_active = True
    start_time = time.monotonic()
    while time.monotonic() - start_time < ANIMATION_DURATION:
        for i in range(num_pixels):
            pixels[i] = (255, 0, 0)  # Animation rouge
        pixels.show()
        time.sleep(0.1)
        if not buttons["snooze"].value:
            snooze_timer()
            break
    animation_active = False
    snooze_timer()

reset_timer()

while True:
    if not buttons["reset"].value:
        reset_timer()
    if not buttons["snooze"].value and not animation_active:
        snooze_timer()
    if not buttons["onoff"].value:
        pause_system()
    
    if not paused and time.monotonic() >= timer:
        start_animation()
    
    time.sleep(0.1)