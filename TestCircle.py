# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 21:07:30 2021

@author: Nivethitha
"""

import unittest
from point import Point
from rectangle import Rectangle
from circle import Circle
from shape import Shape
import math

class TestCircle(unittest.TestCase):


    def test_getters(self):
        circle =  Circle((15, 35),10)
        self.assertEqual((15,35), circle.getCenterPoint())
        
    def test_setters(self):
    
        Circle.setCenterPoint(self, (15,20))
        self.assertEqual((15,20) , Circle.getCenterPoint(self))    
        
    def test_get_radius(self):
        circle =  Circle((15, 35),10)
        self.assertEqual(10, circle.getRadius())
        
    def test_set_radius(self):
        
        Circle.setRadius(self, 10)
        self.assertEqual(10, Circle.getRadius(self))
        
           
    def test_set_contains(self):
        x=Point(5,5)
        y =  Circle((15, 35),10)
        self.assertEqual(True,y.contains(x))        
        
    def test_area(self):
        circle =  Circle((15, 35),10)
        self.assertEqual(314.2,circle.area())         
        
    def test_perimeter(self):
        circle =  Circle((15, 35),10)
        self.assertEqual(62.839999999999996,circle.perimeter()) 
                
            
    def test_to_string(self):
        circle =  Circle((15, 35),10)
        c=circle.tostring()
        d=circle.tostring()
        self.assertEqual(c,d)

    def test_getters_shape(self):
        circle =  Circle((15, 35),10)
        circle.setters(10, 'red', 'blue')
        self.assertEqual((10, 'red', 'blue'),circle.getters())  
        
    def test_setters_shape(self):
        Circle.setters(self,20,'green','blue')
        self.assertEqual((20,'green','blue'), Circle.getters(self))  
        
        
if __name__ == '__main__':
    unittest.main()        
        