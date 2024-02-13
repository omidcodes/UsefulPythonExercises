# needs installing module
# pip install keyboard

import keyboard

# It records all the keys until escape is pressed
rk = keyboard.record(until ='Esc')

# It replay back the all keybcdes
keyboard.play(rk, speed_factor = 1)