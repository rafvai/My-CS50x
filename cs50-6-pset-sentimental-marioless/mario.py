# TODO
from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height < 9 and height > 0:
        break
for i in range(height):
    for j in range(height):
        if(i + j) >= height - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()