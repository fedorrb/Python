# -*- coding: utf-8 -*-
class Sphere(object):
    import math
    polePi = math.pi

    def __init__(self, radius = None, x = None, y = None, z = None):
        self.radius = 1.0
        self.x = float(0)
        self.y = float(0)
        self.z = float(0)
        if radius:
            self.radius = float(radius)
        if x and y and z:
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)

    def get_volume(self):
        volume = 4.0 / 3.0 * self.polePi * self.radius ** 3
        return volume

    def get_square(self):
        square = 4.0 * self.polePi * self.radius ** 2
        return square

    def get_radius(self):
        return self.radius

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, radius):
        self.radius = float(radius)

    def set_center(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def is_point_inside(self, x, y, z):
        result = False
        if ((self.x - x)**2 + (self.y - y)**2 + (self.z - z)**2) <= self.radius**2:
            result = True
        return result
#*******************************

import math

class Sphere1(object):
    center = {'x':0, 'y':0, 'z':0}
    radius = 1

    def __init__(self, r = 1, x = 0, y = 0, z = 0):
        self.set_radius(r)
        self.set_center(x, y, z)

    def get_volume(self):
        return 4.0 / 3 * math.pi * self.radius ** 3

    def get_square(self):
        return 4.0 * math.pi * self.radius ** 2

    def set_radius(self, r):
        self.radius = r

    def set_center(self, x = 0, y = 0, z = 0):
        self.center['x'] = x
        self.center['y'] = y
        self.center['z'] = z

    def get_radius(self):
        return self.radius * 1.0

    def get_center(self):
        return (self.center['x'] * 1.0, self.center['y'] * 1.0, self.center['z'] * 1.0)

    def is_point_inside(self, x = 0, y = 0, z = 0):
        distance = math.sqrt((self.center['x'] - x)**2 +
                            (self.center['y'] - y)**2 +
                            (self.center['z'] - z)**2)
        return distance < self.radius
#***************************
s1 = Sphere()
s1.get_center()
s1.get_radius()
s1.get_volume()
s1.get_square()
s1.is_point_inside(0, 0.99, 0)
s1.is_point_inside(0.99, 0, 0)
s1.is_point_inside(0, 0, 0.99)
s1.set_radius(1.1)

s1.set_center(0.5, 1, 0)