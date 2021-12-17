# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 18:03:53 2021

@author: Nivethitha
"""
import math

class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getX(self):
        return self.x;
    def setX(self,x):
        self.x=x
    def getY(self):
        return self.y;
    def setY(self,y):
        self.y=y
    def setPosition(self,x1,y1):
        x=x1
        y=y1
        return x,y
    def distance(self,x,y):
        distance = math.sqrt((x-self.x)**2+(y-self.y)**2)
        return distance
    def toString(self):
        return"Point ({0},{1})".format(self.x,self.y)
        
#Validation    
#p = Point()
#p.x, p.y = 10,30
#print(p.getX())
#print(p.toString())
#print(p.distance(10,20))
        
        
    
        
        