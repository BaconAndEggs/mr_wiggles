from pynput.mouse import Button, Controller
import time

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

# Set pointer position
mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(
    mouse.position))

mouse.move(30, 0)

print('Doin my wiggles!')

while True:
    # Move pointer relative to current position
    mouse.move(-1, 0)
    time.sleep(1)
    mouse.move(1, 0)
    time.sleep(1)
