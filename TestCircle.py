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
        circle =  Circle(Point(15, 35),10)
        center = (circle.getCenterPoint().getX(),circle.getCenterPoint().getY())
        self.assertTupleEqual((15,35), center)
        
        
    def test_setters(self):
        circle =  Circle(Point(15, 35),10)
        circle.setCenterPoint((15,20))
        center = (circle.getCenterPoint())
        self.assertTupleEqual((15,20),center)
            
        
    def test_get_radius(self):
        circle =  Circle(Point(15, 35),10)
        self.assertEqual(10, circle.getRadius())
        
    def test_set_radius(self):
        circle =  Circle(Point(15, 35),10)
        circle.setRadius(20)
        self.assertEqual(20, circle.getRadius())
        
           
    def test_set_contains(self):
        x=Point(20,36)
        y =  Circle(Point(15, 35),10)
        self.assertEqual(y.contains(x),True)        
        
    def test_area(self):
        circle =  Circle(Point(15, 35),10)
        self.assertEqual(314.2,circle.area())         
        
    def test_perimeter(self):
        circle =  Circle(Point(15, 35),10)
        self.assertEqual(62.839999999999996,circle.perimeter()) 
                
            
    def test_to_string(self):
        circle = Circle((15,35),10)
        x = circle.tostring()
        self.assertEqual('Circle: center: (15, 35),radius: 10',x)

    def test_getters_shape(self):
        circle =  Circle(Point(15, 35),10)
        circle.setters(10, 'red', 'blue')
        self.assertEqual((10, 'red', 'blue'),circle.getters())  
        
    def test_setters_shape(self):
        circle =  Circle(Point(15, 35),10)
        circle.setters(10, 'red', 'blue')
        self.assertEqual((10,'red','blue'), circle.getters())  
        
        
if __name__ == '__main__':
    unittest.main()        
        