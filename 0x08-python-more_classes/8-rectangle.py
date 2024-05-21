#!/usr/bin/python3
"""A module for square"""


class Rectangle:
    """Rectangle class with a method to print a rectangle."""
    number_of_instances = 0
    rect_1 = 0
    rect_2 = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor.
        Args:
            width: width of the rectangle.
            height: height of rectangle.
            number_Of_instances: incremented during new instance instantiation
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter method."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter method."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of a rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ returns the area of a rectangle"""
        result = self.__height + self.__width
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * result)

    def __str__(self):
        """prints the rectangle with the character #"""
        result = ""
        for x in range(0, self.height):
            result += str(self.print_symbol) * self.width
            if x < self.height - 1:
                result += "\n"
        if self.height == 0:
            result += "\n"
        if self.__height == 0 or self.__width == 0:
            return ""
        return result

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """prints message when instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        """returns the biggest rectangle based on the area"""
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_2.area() > rect_2.area():
            return rect_2
