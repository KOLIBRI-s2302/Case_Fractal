import time

import carpet as carp
import flower
import hex
import ice_1 as ice_1
import ice_2
import koch_curve
import koch_snow
import levi
import minkowski
import square
import sun
import tree
import local_RU as RU

print('=' * 40)

print(RU.GREETINGS, '\n')
time.sleep(1)
print(RU.CHOICES)
print(RU.CHOICES_1)

print('=' * 40)

print(RU.ICE_1)
print(RU.SQUARE)
print(RU.SUN)
print(RU.CARPET)
print(RU.FLOWER)
print(RU.KOCH_CURVE)
print(RU.KOCH_SNOW)
print(RU.HEXAGON)
print(RU.MINKOWSKI)
print(RU.LEVI)
print(RU.ICE_2)
print(RU.TREE)

print('=' * 40)

choice = int(input(RU.USER))
if choice == 1:
    ice_1.ice()
if choice == 2:
    square.square()
if choice == 3:
    sun.sun()
if choice == 4:
    carp.carpet()
if choice == 5:
    flower.draw_fractal_flower()
if choice == 6:
    koch_curve.draw_koch_curve()
if choice == 7:
    koch_snow.draw_koch_snowflake()
if choice == 8:
    hex.hex()
if choice == 9:
    minkowski.minkowski()
if choice == 10:
    levi.levi()
if choice == 11:
    ice_2.ice_2()
if choice == 12:
    tree.tree()
