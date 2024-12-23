# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:12:53 2024

@author: EMAN
"""

from abc import ABC, abstractmethod

# صنف أساسي يمثل الأشكال
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# صنف المستطيل
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# صنف المربع
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2
