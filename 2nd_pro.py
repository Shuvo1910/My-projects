# # Timer:

# import time
# import sys

# my_timer = int(input("Enter time in seconds: "))


# for remaining in range(my_timer, -1, -1):
#     h = remaining // 3600
#     m = (remaining % 3600) // 60
#     s = remaining % 60
   
#     sys.stdout.write(f"\r{h:02d}:{m:02d}:{s:02d}")
#     sys.stdout.flush()
#     time.sleep(1)

# print("\nTime's up!")





import turtle
import colorsys

t = turtle.Turtle()
t.hideturtle()
turtle.Screen().bgcolor('black')
t.speed(120)

n = 70
h = 0

for i in range(360):
    r, g, b = colorsys.hsv_to_rgb(h, 1, 0.8)
    t.color(r, g, b)
    h += 1 / n
    t.left(1)
    t.fd(1)
    for j in range(1):
        t.left(2)
        t.circle(110)

turtle.done()
























