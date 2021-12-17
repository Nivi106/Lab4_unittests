# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 19:43:31 2021

@author: Nivethitha
"""

import math
from point import Point
class Rectangle(object):
    topleftpoint: Point(10,20)
    width:float
    height: float
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getters (self):
        return self.x,self.y;
    def setters(self,x,y):
        self.x=x
        self.y=y
    def getwidth (self):
        return self.x;
    def setwidth(self,x):
        self.x=x
    def getheight (self):
        return self.y;
    def setheight(self,y):
        self.y=y
    def area(self):
        a= self.getwidth()*self.getheight()
        return a
    def perimeter(self):
        p= 2*(self.getwidth()+self.getheight()) 
        return p
    def contains(self,Point):
        
        if(Point[0]>10 and Point[0]<self.getwidth()+10 and Point[1]>20 and Point[1]<20+self.getheight() ):
            return True
       

    def centroidx(self):
        cx=self.getwidth()/2
        return cx
    def centroidy(self):
        cy=self.getheight()/2
        return cy  
    def tostring(self):
        print("Rectangle:topleftpoint: {0},{1}, width: {2},height:{3}".format(self.x,self.y,self.getwidth(),self.getheight()))