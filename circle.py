# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 19:43:55 2021

@author: Nivethitha
"""

import math
from point import Point
class Circle():
    
    centerpoint: Point(20,30)
    radius:float
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getters (self):
        return self.x,self.y;
    def setters(self,x,y):
        self.x=x
        self.y=y
    def getradius(self):
        return self.y;
    def setradius(self,y):
        self.y=y
    def area(self):
       a= 3.142*(self.getradius())**2
       return a
    def perimeter(self):
        p = 2*3.142*self.getradius()
        return p
    def contains(self,Point):
        if(Point[0]<2*self.getradius() and Point[1]<2*self.getradius()):
            return True
    def tostring(self):
        print("Circle: center: {0},{1},radius: {2}".format(self.x,self.y,self.getradius()))