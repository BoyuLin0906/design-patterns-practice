from __future__ import annotations

from abc import ABC, abstractmethod
from math import pi


def print_section(title):
    print(f'\n=== {title} ===')


class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: ShapeVisitor):
        raise NotImplementedError('Subclasses must implement accept().')


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor: ShapeVisitor):
        return visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor: ShapeVisitor):
        return visitor.visit_rectangle(self)


class Triangle(Shape):
    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def accept(self, visitor: ShapeVisitor):
        return visitor.visit_triangle(self)


class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: Circle):
        raise NotImplementedError('Subclasses must implement visit_circle().')

    @abstractmethod
    def visit_rectangle(self, rectangle: Rectangle):
        raise NotImplementedError('Subclasses must implement visit_rectangle().')

    @abstractmethod
    def visit_triangle(self, triangle: Triangle):
        raise NotImplementedError('Subclasses must implement visit_triangle().')


class AreaVisitor(ShapeVisitor):
    def visit_circle(self, circle):
        return pi * circle.radius**2

    def visit_rectangle(self, rectangle):
        return rectangle.width * rectangle.height

    def visit_triangle(self, triangle):
        return 0.5 * triangle.a * triangle.height


class PerimeterVisitor(ShapeVisitor):
    def visit_circle(self, circle):
        return 2 * pi * circle.radius

    def visit_rectangle(self, rectangle):
        return 2 * (rectangle.width + rectangle.height)

    def visit_triangle(self, triangle):
        return triangle.a + triangle.b + triangle.c


class DrawVisitor(ShapeVisitor):
    def visit_circle(self, circle):
        return f'Draw a circle with radius {circle.radius}.'

    def visit_rectangle(self, rectangle):
        return f'Draw a rectangle with width {rectangle.width} and height {rectangle.height}.'

    def visit_triangle(self, triangle):
        return f'Draw a triangle with sides {triangle.a}, {triangle.b}, and {triangle.c}.'


def print_shape_details(
    shape: Shape,
    area_visitor: AreaVisitor,
    perimeter_visitor: PerimeterVisitor,
    draw_visitor: DrawVisitor,
):
    print(shape.accept(draw_visitor))
    print(f'Area: {shape.accept(area_visitor):.2f}')
    print(f'Perimeter: {shape.accept(perimeter_visitor):.2f}')
    print()


if __name__ == '__main__':
    shapes = [
        Circle(3),
        Rectangle(4, 6),
        Triangle(3, 4, 5, 4),
    ]

    area_visitor = AreaVisitor()
    perimeter_visitor = PerimeterVisitor()
    draw_visitor = DrawVisitor()

    shape_sections = [
        ('Circle Details', shapes[0]),
        ('Rectangle Details', shapes[1]),
        ('Triangle Details', shapes[2]),
    ]

    for title, shape in shape_sections:
        print_section(title)
        print_shape_details(shape, area_visitor, perimeter_visitor, draw_visitor)
