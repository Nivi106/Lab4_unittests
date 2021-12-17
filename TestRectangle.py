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
        Rect =  Rectangle(15, 35)
        self.assertEqual((15,35), Rect.getters())
        
    def test_setters(self):
        
        Rectangle.setters(self, 15,20)
        self.assertEqual((15,20) , Rectangle.getters(self))    
        
    def test_get_width(self):
        Rect  = Rectangle(15,20)
        self.assertEqual(15, Rect.getwidth())
        
    def test_set_width(self):
        
        Rectangle.setwidth(self, 15)
        self.assertEqual(15, Rectangle.getwidth(self))  
        
    def test_get_height(self):
        Rect  = Rectangle(15,20)
        self.assertEqual(20, Rect.getheight())
        
    def test_set_height(self):
        
        Rectangle.setheight(self, 15)
        self.assertEqual(15, Rectangle.getheight(self))      
        
    def test_set_contains(self):
        x=Point(30,40)
        y=Rectangle(5,5)
        if(x.getX()>10 and x.getX()<y.getwidth()+10 and x.getY()>20 and x.getY()<20+y.getheight() ):
           return True
        z=(x.getX()>10 and x.getX()<y.getwidth()+10 and x.getY()>20 and x.getY()<20+y.getheight())

        self.assertEqual(False,z)           
        
    def test_area(self):
        Rect  =  Rectangle(15, 35)
        area = Rect.getwidth()*Rect.getheight()
        self.assertEqual(area,Rect.area())         
        
    def test_perimeter(self):
        Rect  =  Rectangle(15, 35)
        perimeter = 2*(Rect.getwidth()+Rect.getheight())
        self.assertEqual(perimeter,Rect.perimeter()) 

    def test_set_centroidx(self):
        Rect  =  Rectangle(15, 35)
        cx = Rect.getwidth()/2
        self.assertEqual(cx,Rect.centroidx())         
        
    def test_set_centroidy(self):
        Rect  =  Rectangle(15, 35)
        cy = Rect.getheight()/2
        self.assertEqual(cy,Rect.centroidy())         
                
            
    def test_to_string(self):
       test_rect  =  Rectangle(15, 35)
       self.assertEqual((15,35),test_rect.getters())
       self.assertAlmostEqual(15, test_rect.getwidth())
       self.assertAlmostEqual(35, test_rect.getheight())

    def test_getters_shape(self):
        test_rectangle= Shape(10,'red','blue')
        self.assertEqual((10, 'red', 'blue'),test_rectangle.getters())  
        
    def test_setters_shape(self):
        
        Shape.setters(self,20,'green','blue')
        self.assertEqual((20,'green','blue'), Shape.getters(self))           
        
        
        
if __name__ == '__main__':
    unittest.main()        
        