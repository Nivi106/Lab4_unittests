# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 21:23:00 2021

@author: Nivethitha
"""

import unittest
from point import Point
from shape import Shape
import math

class TestPoint(unittest.TestCase):


    def test_get_X(self):
        test_point  =  Point(15, 35)
        self.assertEqual(15, test_point.getX())
        
    def test_set_X(self):
        test_point  =  Point(15, 35)
        test_point.setX(15)
        self.assertEqual(15,test_point.getX())    
        
    def test_get_Y(self):
        test_point  =  Point(15, 35)
        self.assertEqual(35, test_point.getY())
        
    def test_set_Y(self):
        test_point  =  Point(15, 35)
        test_point.setY(15)
        self.assertEqual(15, test_point.getY())       
        
    def test_set_position(self):
        test_point = Point(15, 35)
        x=5
        y=10
        self.assertEqual((5,10),test_point.setPosition(x,y))           
        
    def test_set_distance(self):
        test_point  =  Point(15, 35)
        self.assertEqual(15.811388300841896,test_point.distance(10,20))         
        
    def test_to_string(self):
        test_point  =  Point(15, 35)
        self.assertEqual('Point (15,35)',test_point.toString())  

    def test_getters(self):
        test_point  =  Point(15, 35)
        test_point.setters(10, 'red', 'blue')
        self.assertEqual((10, 'red', 'blue'),test_point.getters())  
        
    def test_setters(self):
        test_point  =  Point(15, 35)
        test_point.setters(20,'green','blue')
        self.assertEqual((20,'green','blue'), test_point.getters())  
        
        
if __name__ == '__main__':
    unittest.main()        
        