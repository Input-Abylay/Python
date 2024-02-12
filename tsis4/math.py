# # ex1
# import math
# a = int(input())
# print(round(math.radians(a),6))

# # ex2
# height,bs1,bs2 = map(float,input().split())
# print((bs1+bs2)/2*height)

# # ex3
# import math
# def regular_polygon_area(n, s):
#     area = (n * s ** 2) / (4 * math.tan(math.pi / n))
#     return area
#
# n = int(input("Input number of sides: "))
# s = float(input("Input the length of a side: "))
#
# area = regular_polygon_area(n, s)
# print(f"The area of the polygon is: {round(area)}")

# # ex4
# def parallelogram_area(b, h):
#     return b * h
# b = float(input("Length of base: "))
# h = float(input("Height of parallelogram: "))
#
# area = parallelogram_area(b, h)
# print(f"Expected Output: {area}")