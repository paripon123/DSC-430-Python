# Paripon Thanthong
# Date : 05/23/2020
# Honor : “I have not given or received any unauthorized assistance on this assignment.”
# Video Link : https://youtu.be/wXhZRHrmYOM

# Ellipse

from Hw7_1 import *
import math


class Point:
    """Take Point from Users!!"""

    def __init__(self, x_coord=0, y_coord=0):
        """Initiate Point"""
        self.x_coord = x_coord
        self.y_coord = y_coord

    def setx(self, x_coord):
        """Store Point X"""
        self.x_coord = x_coord

    def sety(self, y_coord):
        """Store Point Y"""
        self.y_coord = y_coord

    def distance(self, point):
        """Distance from  Coordinate x and Coordinate y"""
        return math.sqrt((self.x_coord - point.x_coord) ** 2 + (self.y_coord - point.y_coord) ** 2)

    def get(self):
        return (self.x_coord, self.y_coord)


class Ellipse:
    """Create Ellipse and indicate x and y axis from focal point given from user"""

    def __init__(self, point_1, point_2, width):
        self.p1 = point_1
        self.p2 = point_2
        self.x1, self.y1 = point_1.get()  # Point1 from Class point (unpack)
        self.x2, self.y2 = point_2.get()  # Point2 from Class point (unpack)

        self.major_axis = width  # Major Axis 2a

    def ellipse_val(self):
        """Calculation of Value for further computation"""

        self.dist_e = ((self.y2 - self.y1) ** 2 + (self.x2 - self.x1) ** 2) ** (1 / 2)  # Distance from 2 focal point

        self.half_major_axis = self.major_axis / 2  # Major axis each side (half width)
        self.half_dis = self.dist_e / 2

        self.minor_axis = math.sqrt((self.major_axis ** 2) - (self.dist_e ** 2))
        self.half_minor_axis = self.minor_axis / 2

    def dist_focal(self):
        return self.dist_e

    def boundingbox(self):
        """Generate a bounding box for one ellipse"""
        return self.major_axis * self.half_minor_axis

    def inellipse(self, point):
        """Check Point in Ellispe"""

        # Still in Doubt whether or not this is the right way
        dist = point.distance(self.p1) + point.distance(self.p2)
        return dist <= self.major_axis


class box:
    """Define box for 2 Ellipse"""

    def __init__(self, e1, e2):
        """Initiate With 2 Ellipses"""

        self.e1 = e1
        self.e2 = e2

    def x_val(self):
        """Get X Coordinate from 2 Ellipses for Generating Box"""

        max_width = max(self.e1.major_axis, self.e2.major_axis)
        x_coor = [self.e1.x1, self.e1.x2, self.e2.x1, self.e2.x2]
        self.x_min = min(x_coor) - max_width / 2
        self.x_max = max(x_coor) + max_width / 2

    def y_val(self):
        """Get Y Coordinate from 2 Ellipses for Generating Box"""

        max_width = max(self.e1.major_axis, self.e2.major_axis)
        y_coor = [self.e1.y1, self.e1.y2, self.e2.y1, self.e2.y2]
        self.y_min = min(y_coor) - max_width / 2
        self.y_max = max(y_coor) + max_width / 2

    def get_val(self):
        """Get Value from Coordinates X and Y"""
        return self.x_min, self.x_max, self.y_min, self.y_max

    def area_box(self):
        """Area of Box for 2 Ellipses"""
        return (self.x_max - self.x_min) * (self.y_max - self.y_min)


def simulation(seed, x_max, x_min, y_max, y_min, e1, e2, rand_point):
    """MonteCarlo Simulation"""

    count_in_ellipse = 0  # To Count if the point is in the Ellipse
    prng = WarAndPeacePseudoRandomNumberGenerator(seed)  # Take Seed number
    for num in range(rand_point):
        x_cor = (x_max - x_min) * prng.random() + x_min
        y_cor = (y_max - y_min) * prng.random() + y_min
        point_rand = Point(x_cor, y_cor)
        if e1.inellipse(point_rand) and e2.inellipse(point_rand):
            count_in_ellipse += 1
    return count_in_ellipse


def intro():
    """Introduction"""

    print("""
    Welcome!! To the Ellipse.
    
    'Now, There is light, so enjoy it because Winter is coming!!!!'
    
    This Program will ask you to input points and width which will report 
    the area that of overlap Ellipses
    
    Best of Luck!
    
    """)


def computeOverlapOfEllipses(e1, e2, rand_point, seed):
    """Compute The overlap"""

    # In doubt of the method

    bounding_box = box(e1, e2)
    x_val = bounding_box.x_val()  # To store value for function .get_val()
    y_val = bounding_box.y_val()  # To store value for function .get_val()

    x_min, x_max, y_min, y_max = bounding_box.get_val()
    point = simulation(seed, x_max, x_min, y_max, y_min, e1, e2, rand_point)

    return point / (rand_point * bounding_box.area_box())


def user_input():
    """ User Input"""

    point1_e1_x = int(input('Select Point1 X for Ellipse 1: '))
    point1_e1_y = int(input('Select Point1 Y for Ellipse 1: '))
    point2_e1_x = int(input('Select Point2 X for Ellipse 1: '))
    point2_e1_y = int(input('Select Point2 Y for Ellipse 1: '))

    point1_e2_x = int(input('Select Point1 X for Ellipse 2: '))
    point1_e2_y = int(input('Select Point1 Y for Ellipse 2: '))
    point2_e2_x = int(input('Select Point2 X for Ellipse 2: '))
    point2_e2_y = int(input('Select Point2 Y for Ellipse 2: '))

    #### Error Handling

    point_1_e1 = Point(point1_e1_x, point1_e1_y)
    point_2_e1 = Point(point2_e1_x, point2_e1_y)

    point_1_e2 = Point(point1_e2_x, point1_e2_y)
    point_2_e2 = Point(point2_e2_x, point2_e2_y)
    while True:
        try:
            width_e1 = int(input('Select Width for Ellipse 1:'))
            width_e2 = int(input('Select Width for Ellipse 2: '))
            e1 = Ellipse(point_1_e1, point_2_e1, width_e1)
            e2 = Ellipse(point_1_e2, point_2_e2, width_e2)
            e1_val = e1.ellipse_val()  # To compute value
            e2_val = e2.ellipse_val()  # To compute value
            if width_e1 < e1.dist_focal() or width_e2 < e2.dist_focal():
                print('This Width is not wide enough! Try Higher value')
            else:
                return point1_e1_x, point1_e1_y, point2_e1_x, point2_e1_y, point1_e2_x, point1_e2_y, point2_e2_x, point2_e2_y, width_e1, width_e2
        except ValueError:
            print('This is not the right Value.')


def main():
    """Test overlapping area of 2 ellipses"""

    intro()
    px1_e1, px2_e1, py1_e1, py2_e1, px1_e2, px2_e2, py1_e2, py2_e2, w_e1, w_e2 = user_input()
    p1_e1 = Point(px1_e1, py1_e1)
    p2_e1 = Point(px2_e1, py2_e1)

    p1_e2 = Point(px1_e2, py1_e2)
    p2_e2 = Point(px2_e2, py2_e2)

    e1 = Ellipse(p1_e1, p2_e1, w_e1)
    e2 = Ellipse(p1_e2, p2_e2, w_e2)

    seed = int(input('Seed Number :'))
    num_rand = int(input('Number of Random Point: '))

    print('Area of overlapping Ellipses', computeOverlapOfEllipses(e1, e2, num_rand, seed))


if __name__ == '__main__':
    main()
