# This program computes an approximation of π
# !I could not figure out how to use the precision command!

import random

in_circle = 0
out_circle = 0

for i in range(0, 1000000):
    x = random.random()
    y = random.random()
    d = x**2 + y**2
    if d <= 1:
        in_circle += 1
    out_circle += 1


def estimate_pi(precision):
    pi_value = 4 * (in_circle / out_circle)
    return pi_value


print(estimate_pi(precision=10))
