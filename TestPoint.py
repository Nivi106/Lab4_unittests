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
        
        Point.setX(self, 15)
        self.assertEqual(15, Point.getX(self))    
        
    def test_get_Y(self):
        test_point  =  Point(15, 35)
        self.assertEqual(35, test_point.getY())
        
    def test_set_Y(self):
        
        Point.setY(self, 15)
        self.assertEqual(15, Point.getY(self))       
        
    def test_set_position(self):
        x=5
        y=10
        self.assertEqual((5,10),Point.setPosition(self,x,y))           
        
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
        
        Point.setters(self,20,'green','blue')
        self.assertEqual((20,'green','blue'), Point.getters(self))  
        
        
if __name__ == '__main__':
    unittest.main()        
        