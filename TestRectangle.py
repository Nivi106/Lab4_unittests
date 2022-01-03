# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 19:33:55 2021

@author: Nivethitha
"""

import unittest
from point import Point
from rectangle import Rectangle
from shape import Shape
import math

class TestRectangle(unittest.TestCase):


    def test_getters(self):
        Rect =  Rectangle((15, 35),10,20)
        self.assertEqual((10,20), Rect.getter())
        
    def test_setters(self):
        
        Rectangle.setter(self, (15,20),10,20)
        self.assertEqual((10,20) , Rectangle.getter(self))    
        
    def test_get_width(self):
        Rect =  Rectangle((15, 35),10,20)
        self.assertEqual(10, Rect.getwidth())
        
    def test_set_width(self):
        
        Rectangle.setwidth(self, 15)
        self.assertEqual(15, Rectangle.getwidth(self))  
        
    def test_get_height(self):
        Rect =  Rectangle((15, 35),10,20)
        self.assertEqual(20, Rect.getheight())
        
    def test_set_height(self):
        
        Rectangle.setheight(self, 15)
        self.assertEqual(15, Rectangle.getheight(self))      
        
    def test_set_contains(self):
        x=Point(5,5)
        y=Rectangle((15, 35),10,20)
        c=y.contains(x)
        d=y.contains(x)
        self.assertEqual(c,d)
                  
        
    def test_area(self):
        Rect =  Rectangle((15, 35),10,20)
        self.assertEqual(200,Rect.area())         
        
    def test_perimeter(self):
        Rect =  Rectangle((15, 35),10,20)
        self.assertEqual(60,Rect.perimeter()) 

    def test_set_centroid(self):
        Rect =  Rectangle((15, 35),10,20)
        self.assertEqual((20.0, 45.0),Rect.centroid())         
        
               
    def test_to_string(self):
        Rect =  Rectangle((15, 35),10,20)
        c=Rect.tostring()
        d=Rect.tostring()
        self.assertEqual(c,d)

    def test_getters_shape(self):
        rect =  Rectangle((15, 35),10,20)
        rect.setters(10,'red','blue')
        self.assertEqual((10,'red', 'blue'),rect.getters())  
        
    def test_setters_shape(self):
        
        Rectangle.setters(self,20,'green','blue')
        self.assertEqual((20,'green','blue'), Rectangle.getters(self))           
        
        
        
if __name__ == '__main__':
    unittest.main()        
        