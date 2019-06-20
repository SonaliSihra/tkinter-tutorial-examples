import math

from pip._vendor.distlib.compat import raw_input

count = 0
distance1 = 0

while count != 5:
    p1 = [5, 0]
    p2 = [8, 6]
    distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    distance1 = distance1 + distance
    count = count + 1
    print(" Count: ", count)
    print("Distance: ", distance)
    print("Distance1: ", distance1)
