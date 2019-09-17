#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program calculates the area and the perimeter of a circle
#     with user input


def main():
    # this function calculates area and perimeter

    # input
    Length = int(input("enter length of rectangle (mm): "))
    Width = int(input("enter width of rectangle (mm): "))

    # process
    area = Length*Width
    perimeter = 2*(Length+Width)

    # output
    print("")
    print("area is {}mm^2".format(area))
    print("perimeter is {}mm".format(perimeter))


if __name__ == "__main__":
    main()
