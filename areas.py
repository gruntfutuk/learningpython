#!/usr/bin/env python

import numpy as np

widths = np.array([10, 4, 8])
lengths = ([5, 6, 6])
areas = np.array([])

for i in range(0, 3):
    areas = np.append(areas, [widths[i] * lengths[i]])

print(areas)
print(widths*lengths)
print(areas[areas > 40])
