#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import numpy as np

AC = int(input("Enemy's Armor Class: "))
mod = int(input("Your attack modifier: "))
adv = int(input("1=Advantage. 0=Normal attack. -1=Disadvantage: "))

dist = np.arange(1, 0, -1/20)
gain = ((dist*dist)-((dist-0.05)*(dist-0.05)))
if adv == 1:
    print('Rolling with Advantage')
elif adv == -1:
    print('Rolling with Disadvantage')
    gain = gain[::-1]
elif adv == 0:
    print('Rolling without Advantage')
    gain = [0.05] * len(dist)

higher_than = gain
for i in np.arange(len(dist)):
    if i == 0:
        higher_than[i] = gain[i]
    else:
        higher_than[i] = gain[i]+higher_than[i-1]
higher_than = higher_than[::-1]

print("Chance of hitting: "+"{:.1%}".format(higher_than[AC-1-mod]))