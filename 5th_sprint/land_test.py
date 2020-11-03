"""
There are 4 points (x,y) forming the land. And one random point.
Be sure that the point is inside the land or not.
"""
import unittest
from typing import List, Callable


def func_from_line(a: tuple, b: tuple) -> Callable[[int], int]:
    """
    Return a line function from two points
    """
    def f(x):
        """ the line function y = f(x)"""
        return a[1] + (b[1]-a[1])/(b[0]-a[0])*x - (b[1]-a[1])/(b[0]-a[0])*a[0]
    return f


def return_left_point(points_list: List[tuple]) -> tuple:
    """
    Returns the point, tuple such as (x,y) from points_list with minimal
    x coordinate. When there are two points it returns the bottom left point
    """
    return min(points_list)


def return_right_point(points_list: List[tuple]) -> tuple:
    """
    Returns the point, tuple such as (x,y) from points_list with maximal
    x coordinate. When there are two points it returns the upper right point
    """
    return max(points_list)


def check(land: List[tuple], point: tuple) -> bool:
    """
    Building the schema of quadrant: finding right, left, up and bottom points
    Creating the rays function from left to up and bottom function and checks
    if y coordinate of the point is between y value of ray function
    in x coordinate of the point
    """
    left_point = return_left_point(land)
    right_point = return_right_point(land)
    other_points = [p for p in land if p not in [left_point, right_point]]

    if other_points[0][1] > other_points[1][1]:
        up_point = other_points[0]
    elif other_points[0][1] < other_points[1][1]:
        up_point = other_points[1]
    elif other_points[0][1] == other_points[1][1]:
        up_point = min(other_points)  # taking the left one
    else:
        raise RuntimeError('Something going absolutely wrong')

    bottom_point = other_points[0] if other_points[0] != up_point else other_points[1]

    left_upper_line = func_from_line(left_point, up_point)
    left_bottom_line = func_from_line(left_point, bottom_point)

    right_upper_line = func_from_line(right_point, up_point)
    right_bottom_line = func_from_line(right_point, bottom_point)

    left_check = left_upper_line(point[0]) >= point[1] >= left_bottom_line(point[0])
    righ_check = right_upper_line(point[0]) >= point[1] >= right_bottom_line(point[0])
    # breakpoint()
    return left_check and righ_check


def check_data(land: List[tuple], point: tuple) -> bool:
    """
    Checking if given data is correct
    """
    if len(land) != 4:
        raise TypeError('Given data is not valid')
    if len(point) != 2 or type(point) != tuple:
        raise TypeError('Given data is not valid')
    for tuple_item in land:
        if len(tuple_item) != 2 or type(tuple_item) != tuple:
            raise TypeError('Given data is not valid')
    return True


def run(land: List[tuple], point: tuple) -> bool:
    check_data(land, point)
    return check(land, point)


class TestChecks(unittest.TestCase):
    def test_outside_simple_quadrant(self):
        call = run([(200, 200), (300, 400), (500, 300), (300, 0)], (100, 100))
        result = False
        self.assertEqual(call, result,
                         'Doesnt work with point outside simple quadrant')

    def test_inside_simple_quadrant(self):
        call = run([(200, 200), (300, 400), (500, 300), (300, 0)], (300, 200))
        result = True
        self.assertEqual(call, result,
                         'Doesnt work with point inside simple quadrant')

    def test_right_in_edge(self):
        call = run([(200, 200), (300, 400), (500, 300), (300, 0)], (250, 300))
        result = True
        self.assertEqual(call, result,
                         'Doesnt work with point right in edge')

    def test_right_in_vertex(self):
        call = run([(200, 200), (300, 400), (500, 300), (300, 0)], (300, 400))
        result = True
        self.assertEqual(call, result,
                         'Doesnt work with point right in vertex')

    def test_no_upper_and_bottom_points(self):
        call = run([(100, 100), (200, 100), (200, 200), (300, 200)], (150, 101))
        result = True
        self.assertEqual(call, result,
                         'Doesnt work with no upper and bottom point quadrant')

    def test_no_left_and_right_points(self):
        call = run([(100, 100), (100, 200), (200, 150), (200, 250)], (150, 175))
        result = True
        self.assertEqual(call, result,
                         'Doesnt work with no upper and bottom point quadrant')

    def test_specific_quadrant(self):
        call = run([(100, 100), (100, 200), (200, 200), (200, 300)], (150, 175))
        result = True
        self.assertEqual(call, result,
                         'Doesnt work with specific quadrant')

    def test_non_quadrant_points(self):
        self.assertRaises(ValueError,
                          run,
                          [(100, 100), (100, 200), (100, 300), (200, 200)],
                          (150, 150))

    def test_check_data_function(self):
        self.assertRaises(TypeError,
                          run,
                          [(100, 100), (200, 200), (300, 100), (200, 100)],
                          (5, 2, 1))


if __name__ == '__main__':
    land = [(100, 100), (200, 200), (300, 100), (200, 0)]
    point = (200, 100)
    print(run(land, point))
