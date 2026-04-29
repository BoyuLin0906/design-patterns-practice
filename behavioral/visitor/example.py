from abc import ABC, abstractmethod
from math import pi


def print_section(title):
    print(f'\n=== {title} ===')


class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        return visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        return visitor.visit_rectangle(self)


class Triangle(Shape):
    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def accept(self, visitor):
        return visitor.visit_triangle(self)


class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass

    @abstractmethod
    def visit_triangle(self, triangle):
        pass


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


def print_shape_details(shape, area_visitor, perimeter_visitor, draw_visitor):
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
