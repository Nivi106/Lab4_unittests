# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 19:43:55 2021

@author: Nivethitha
"""

import math
import random
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
        return self.radius
    
    def setRadius(self,radius):
        self.radius=radius
    
    def area(self):
       a= 3.142*(self.getRadius())**2
       return a
    
    def perimeter(self):
        p = 2*3.142*self.getRadius()
        return p
   
    def contains(self,Point:Point):
        d=math.sqrt((self.centerpoint.getX()-Point.getX())**2+(self.centerpoint.getY()-Point.getY())**2)
        if d < self.getRadius():
            return True
        else:
            return False    
    
    def tostring(self):
        return("Circle: center: {0},radius: {1}".format(self.centerpoint,self.radius))
