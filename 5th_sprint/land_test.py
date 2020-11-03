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
        # try:
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


def return_point(point_list: List[tuple], min_max: str, x_y: int) -> tuple:
    """
    Returns the point, tuple such as (x,y) from point_list
    with minimal (or maximal) x (or y) coordinate.
    Keyword arguments:
        point_list: the list of points (tuples).
        min_max: 'min' or 'max' option of returning point
        x_y: 0 or 1 as point tuple index
    """
    if min_max == 'min':
        min_point = point_list[0]  # starting from first element
        for i in range(1, len(point_list)):  # starting from second element
            if point_list[i][x_y] < min_point[x_y]:
                min_point = point_list[i]
            elif point_list[i][x_y] == min_point[x_y]:
                raise ValueError('Tho points returned')
        return min_point
    elif min_max == 'max':
        max_point = point_list[0]  # starting from first element
        for i in range(1, len(point_list)):  # starting from second element
            if point_list[i][x_y] > max_point[x_y]:
                max_point = point_list[i]
        return max_point
    else:
        raise ValueError('Second positional argument'
                         'must be "min" or "max" string')


def left_check(land: List[tuple], point: tuple) -> bool:
    """
    Building two rays from left point to upper and bottom points
    Checking that the point is between the rays
    """
    min_x = return_left_point(land)
    min_y = return_point(land, 'min', 1)  # upper point
    max_y = return_point(land, 'max', 1)  # bottom point

    left_high_line = func_from_line(min_x, max_y)  # the left upper line
    left_bottom_line = func_from_line(min_x, min_y)  # the left bottom line

    # if y coordinate of the point is between the values of line functions
    # with x argument as point x coordinate
    return left_high_line(point[0]) >= point[1] >= left_bottom_line(point[0])


def right_check(land: List[tuple], point: tuple) -> bool:
    """
    Building two rays from right point to upper and bottom points
    Checking that the point is between the rays
    """
    max_x = return_right_point(land)
    min_y = return_point(land, 'min', 1)  # upper point
    max_y = return_point(land, 'max', 1)  # bottom point

    right_high_line = func_from_line(max_x, max_y)  # the right upper line
    right_bottom_line = func_from_line(max_x, min_y)  # the right bottom line

    return right_high_line(point[0]) >= point[1] >= right_bottom_line(point[0])


def check(land: List[tuple], point: tuple) -> bool:
    left_point = return_left_point(land, point)
    pass

def check_data(land: List[tuple], point: tuple) -> bool:
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
    return left_check(land, point) and right_check(land, point)


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