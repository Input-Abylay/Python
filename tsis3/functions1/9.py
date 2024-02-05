import math

def volume_of_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

radius = 5
volume = volume_of_sphere(radius)
print(volume)
