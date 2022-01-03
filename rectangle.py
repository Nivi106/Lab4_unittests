# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 19:43:31 2021

@author: Nivethitha
"""

import math
from shape import Shape
from point import Point

class Rectangle(Shape):
    topleftpoint: Point
    width:float
    height: float
    def __init__(self,topleftpoint,width,height):
        self.topleftpoint = topleftpoint
        self.width=width
        self.height=height
    def getter (self):
        return self.width,self.height;
    def setter(self,topleftpoint,width,height):
        self.topleftpoint = topleftpoint
        self.width=width
        self.height=height
    def getwidth (self):
        return self.width;
    def setwidth(self,width):
        self.width=width
    def getheight (self):
        return self.height;
    def setheight(self,height):
        self.height=height
    def area(self):
        a=self.getwidth()*self.getheight()
        return a
    def perimeter(self):
        p= 2*(self.getwidth()+self.getheight()) 
        return p
    def contains(self,Point):
       
       if(Point.x>self.topleftpoint[0] and Point.x<self.getwidth()+10 and Point.y>self.topleftpoint[1] and Point.y<20+self.getheight() ):
            return True

    def centroid(self):
         return (self.topleftpoint[0]+(self.width/2), self.topleftpoint[1]+(self.height/2))  
    def tostring(self):
        print("Rectangle:topleftpoint: {0}, width: {1},height:{2}".format(self.topleftpoint,self.width,self.height))
