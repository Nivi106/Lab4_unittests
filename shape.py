# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 22:06:16 2021

@author: Nivethitha
"""

import math
import random
from point import Point
class Shape(object):
    strokewidth: int;
    strokecolor: float;
    fillcolor: float;
    def __init__(self,strokewidth, strokecolor,fillcolor):
        self.strokewidth=strokewidth
        self.strokecolor=strokecolor
        self.fillcolor=fillcolor
    def getters(self):
        return self.strokewidth,self.strokecolor,self.fillcolor;
    def setters(self,strokewidth,strokecolor,fillcolor):
        self.strokewidth=strokewidth
        self.strokecolor=strokecolor
        self.fillcolor=fillcolor
   