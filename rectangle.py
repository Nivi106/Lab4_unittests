# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 19:43:31 2021

@author: Nivethitha
"""


import math
import random
from point import Point
from shape import Shape
import numpy

class Rectangle(Shape):
    topleftpoint:Point
    width:float
    height:float
    
    def __init__(self,topleftpoint,width,height):
        self.topleftpoint = topleftpoint
        self.width=width
        self.height=height 
        
    def getting(self):
        return self.topleftpoint
    
    def setting(self,topleftpoint):
        self.topleftpoint = topleftpoint
           
    def getwidth(self):
        return self.width
    
    def setwidth(self,width):
        self.width=width
    
    def getheight(self):
        return self.height
    
    def setheight(self,height):
        self.height=height
    
    def area(self):
        a=self.getwidth()*self.getheight()
        return a
    
    def perimeter(self):
        p= 2*(self.getwidth()+self.getheight()) 
        return p
    
    def contains(self,point:Point):
      if(point.getX() > self.topleftpoint.getX() and point.getX() < self.topleftpoint.getX() + self.width and point.getY() > self.topleftpoint.getY() and point.getY() < self.topleftpoint.getY()+self.height):
           return True
      else:
           return False

    def centroid(self):
        x = self.topleftpoint.getX() + (self.width)/2
        y = self.topleftpoint.getY() + (self.height)/2
        return Point(x,y)
    
    def tostring(self):
        return("Rectangle:topleftpoint: {0}, width: {1},height:{2}".format(self.topleftpoint,self.width,self.height))
