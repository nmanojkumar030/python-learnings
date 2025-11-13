"""
Start at 10 seconds and count down until 1 and then print "Happy New Year! 🎉"
"""

import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("Happy New Year! 🎉")
