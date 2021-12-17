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

class TestRectangle(unittest.TestCase):


    def test_getters(self):
        circle =  Circle(15, 35)
        self.assertEqual((15,35), circle.getters())
        
    def test_setters(self):
        
        Circle.setters(self, 15,20)
        self.assertEqual((15,20) , Circle.getters(self))    
        
    def test_get_radius(self):
        circle  = Circle(15,20)
        self.assertEqual(20, circle.getradius())
        
    def test_set_radius(self):
        
        circle  = Circle(15,20)
        self.assertEqual(20, circle.getradius())  
        
           
    def test_set_contains(self):
        x=Point(30,40)
        y=Circle(5,5)
        if(x.getX()<2*y.getradius() and x.getY()<2*y.getradius() ):
           return True
        z=(x.getX()<2*y.getradius() and x.getY()<2*y.getradius() )

        self.assertEqual(False,z)        
        
    def test_area(self):
        circle  =  Circle(15, 35)
        area = 3.142*(circle.getradius())**2
        self.assertEqual(area,circle.area())         
        
    def test_perimeter(self):
        circle  =  Circle(15, 35)
        perimeter =  2*3.142*circle.getradius()
        self.assertEqual(perimeter,circle.perimeter()) 
                
            
    def test_to_string(self):
       test_cir  =  Circle(15, 35)
       self.assertEqual((15,35),test_cir.getters())
       self.assertAlmostEqual(35, test_cir.getradius())

    def test_getters_shape(self):
        test_rectangle= Shape(10,'red','blue')
        self.assertEqual((10, 'red', 'blue'),test_rectangle.getters())  
        
    def test_setters_shape(self):
        
        Shape.setters(self,20,'green','blue')
        self.assertEqual((20,'green','blue'), Shape.getters(self))           
        
        
        
if __name__ == '__main__':
    unittest.main()        
        