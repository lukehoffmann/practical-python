# bounce.py
#
# Exercise 1.5

bounce = 0
height = 60.0

while (bounce:= bounce + 1) <= 10:
    print(bounce, round(height, 4))
    height *= 3 / 5
