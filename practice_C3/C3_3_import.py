import math
import time

print(math.trunc(math.fmod(math.fabs(-10000000), 55)+0.3))

print(time.gmtime(time.time()))

print(time.strftime("%X"))

i=10
while i !=0:
    print(i)
    time.sleep(1)
    i -=1