# # Timer:

import time
import sys

my_timer = int(input("Enter time in seconds: "))


for remaining in range(my_timer, -1, -1):
    h = remaining // 3600
    m = (remaining % 3600) // 60
    s = remaining % 60
   
    sys.stdout.write(f"\r{h:02d}:{m:02d}:{s:02d}")
    sys.stdout.flush()
    time.sleep(1)

print("\nTime's up!")





























