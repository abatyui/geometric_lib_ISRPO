import unittest
import math
import circle
import square
import rectangle
import triangle


class GeometricLibTestCase(unittest.TestCase):

    # --- Тесты для круга (Circle) ---
    def test_circle_area(self):
        # Проверяем площадь при радиусе 3
        res = circle.area(3)
        self.assertEqual(res, math.pi * 3 * 3)

    def test_circle_perimeter(self):
        res = circle.perimeter(3)
        self.assertEqual(res, 2 * math.pi * 3)

    # --- Тесты для квадрата (Square) ---
    def test_square_area(self):
        res = square.area(5)
        self.assertEqual(res, 25)

    def test_square_perimeter(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

    # --- Тесты для прямоугольника (Rectangle) ---
    def test_rectangle_area(self):
        res = rectangle.area(10, 5)
        self.assertEqual(res, 50)

    def test_rectangle_perimeter(self):
        res = rectangle.perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_zero_area(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    # --- Тесты для треугольника (Triangle) ---
    def test_triangle_area(self):
        res = triangle.area(10, 5)
        self.assertEqual(res, 25)

    def test_triangle_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    def test_triangle_perimeter2(self):
        res = triangle.perimeter(10, 5, 5)
        self.assertEqual(res, 2)
