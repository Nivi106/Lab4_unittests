# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 19:43:55 2021

@author: Nivethitha
"""

import math
from shape import Shape
from point import Point
class Circle(Shape):
    centerpoint: Point
    radius:float
    def __init__(self,centerpoint,radius):
        self.centerpoint=centerpoint
        self.radius=radius
    def getCenterPoint(self):
        return self.centerpoint
    def setCenterPoint(self,centerpoint):
        self.centerpoint=centerpoint
    def getRadius(self):
        return self.radius;
    def setRadius(self,radius):
        self.radius=radius
    def area(self):
       a= 3.142*(self.getRadius())**2
       return a
    def perimeter(self):
        p = 2*3.142*self.getRadius()
        return p
    def contains(self,Point):
        if(Point.x<2*self.getRadius() and Point.y<2*self.getRadius()):
            return True
    def tostring(self):
        print("Circle: center: {0},{1},radius: {2}".format(self.centerpoint,self.radius,self.getRadius()))
