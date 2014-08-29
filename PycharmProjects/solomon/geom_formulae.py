__author__ = 'nii'
from math import *
import math


def rectangle_area(length, breadth):
    """
    calculate the area of a rectangle (in square units of length and breadth)
    :param length: length of the rectangle
    :param breadth: breadth of the rectangle
    :return:the area of the rectangle
    >>> rectangle_area(7,3)
    21
    """
    return length*breadth


def parallelogram_area(base, height):
    """
    calculate the area of a parallelogram given the base and height
    :param base: base length of the parallelogram
    :param height: perpendicular height of the parallelogram
    :return: the area of the parallelogram
    >>>parallelogram_area(5,8)
    40
    """
    return base*height


def equilateral_triangle_area(base, height):
    """
    evaluate the area of an equilateral triangle given the dimensions
    :param base: base of the triangle
    :param height:  perpendicular height of the triangle
    :return:the area of the triangle
    >>>equilateral_triangle_area(3,6)
    9
    """
    return 0.5*base*height


def ellipse_area(radius1, radius2):
    """
    find the area of an ellipse with the two radii given
    :param radius1: horizontal radius of the ellipse
    :param radius2: vertical radius of the ellipse
    :return: the area of the ellipse
    >>> ellipse_area(4,2)
    25.1327412287
    """
    return pi*radius1*radius2


def trapezoid_area(height, base1, base2):
    """
    this calculates the area of a trapezoid
    :param height: perpendicular height of the trapezoid
    :param base1: top length of the trapezoid
    :param base2: bottom length of the trapezoid
    :return:the area of the trapezoid
    >>>trapezoid_area(4,2,3)
    10
    """
    return height/2*(base1+base2)


def equilateral_triangle_area_alternative(side):
    """
    calculate the area of an equilateral triangle given one side
    :param side: a side of the equilateral triangle
    :return:the area of the equilateral triangle
    >>>equilateral_triangle_area_alternative(4)
    6.92820323028
    """
    return (math.sqrt(3.0)/4.0)*side*side


def cube_volume(side):
    """
    'cube volume' calculates the volume of a cube (in cubic units).
    :param side:a side of the cube
    :return:volume of the cube
    >>>cube_volume(4)
    64
    """
    return side**3


def cuboid_volume(length, breadth, height):
    """
    this calculates the volume of a cuboid
    :param length: length of the base
    :param breadth: breadth of the cuboid
    :param height: perpendicular height of the cuboid
    :return:the volume of the cuboid
    >>> cuboid_volume(4,2,5)
    40
    """
    return length*breadth*height


def sphere_volume(radius):
    """
    calculate the volume of a sphere (in unit cube)
    :param radius: the radius of the sphere
    :return:the volume of the sphere
    >>>sphere_volume(2)
    33.5103216383
    """
    return 4.0/3.0*pi*radius**3


def cylinder_volume(radius, height):
    """
    calculate the volume of a cylinder with the radius and height given (in unit cube)
    :param radius: radius of the base of the cylinder
    :param height: height of the cylinder
    :return:the volume of the cylinder
    >>> cylinder_volume(4,6)
301.592894745
    """
    return pi*radius*radius*height


def rectangle_perimeter(length, breadth):
    """
    calculate the perimeter of a rectangle
    :param length: length of a rectangle
    :param breadth: breadth of a rectangle
    :return: the perimeter of a rectangle
    >>>rectangle_perimeter(4,3)
    14
    """
    return 2*(length + breadth)