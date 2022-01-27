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
        Rect =  Rectangle(Point(15, 35),10,20)
        center = (Rect.topleftpoint.getX(),Rect.topleftpoint.getY())
        self.assertEqual((15,35), center)
        
        
    def test_setters(self):
        rect =  Rectangle(Point(15, 35),10,20)
        rect.setting((15,20))
        self.assertEqual((15,20) , rect.getting())


    def test_get_width(self):
        Rect =  Rectangle(Point(15, 35),10,20)
        self.assertEqual(10, Rect.getwidth())
        
    def test_set_width(self):
        rect =  Rectangle(Point(15, 35),10,20)
        rect.setwidth((15))
        self.assertEqual(15, rect.getwidth())  
        
    def test_get_height(self):
        Rect =  Rectangle(Point(15, 35),10,20)
        self.assertEqual(20, Rect.getheight())
        
    def test_set_height(self):
        
        rect =  Rectangle(Point(15, 35),10,20)
        rect.setheight((15))
        self.assertEqual(15, rect.getheight())    
        
    def test_set_contains(self):
        x=Point(16,36)
        y=Rectangle(Point(15, 35),10,20)
        self.assertEqual(y.contains(x),True)
                  
        
    def test_area(self):
        Rect =  Rectangle(Point(15, 35),10,20)
        self.assertEqual(200,Rect.area())         
        
    def test_perimeter(self):
        Rect =  Rectangle(Point(15, 35),10,20)
        self.assertEqual(60,Rect.perimeter()) 

    def test_set_centroid(self):
        Rect =  Rectangle(Point(15, 35),10,20)
        x = (Rect.centroid().getX(), Rect.centroid().getY())
        self.assertTupleEqual((20.0,45.0), x) 
        
               
    def test_to_string(self):
        Rect =  Rectangle((15,35),10,20)
        self.assertEqual('Rectangle:topleftpoint: (15, 35), width: 10,height:20',Rect.tostring())

    def test_getters_shape(self):
        rect =  Rectangle((15, 35),10,20)
        rect.setters(10,'red','blue')
        self.assertEqual((10,'red', 'blue'),rect.getters())  
        
    def test_setters_shape(self):
        rect =  Rectangle((15, 35),10,20)
        rect.setters(10,'red','blue')
        self.assertEqual((10,'red','blue'), rect.getters())           
        
        
        
if __name__ == '__main__':
    unittest.main()        
        