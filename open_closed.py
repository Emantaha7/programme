# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 15:10:41 2024

@author: EMAN
"""

from abc import ABC, abstractmethod
from math import pi

# صنف مجرد يحدد واجهة الأشكال
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# تنفيذ الشكل الدائري
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

# تنفيذ الشكل المستطيل
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
