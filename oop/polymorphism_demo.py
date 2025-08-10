import math


class Shape:
    """Base class for shapes. Subclasses should override area()."""

    def area(self):
        """Return the area of the shape.

        Subclasses must override this method.
        """
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    """Rectangle shape defined by length and width."""

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        """Return the area of the rectangle (length * width)."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape defined by its radius."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Return the area of the circle (pi * r^2)."""
        return math.pi * (self.radius ** 2)