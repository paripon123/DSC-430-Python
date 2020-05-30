# Paripon Thanthong
# Date : 05/27/2020
# Honor : “I have not given or received any unauthorized assistance on this assignment.”
# Video Link : https://youtu.be/GinmMspQnOQ
import numpy as np


def numpy_practice():
    """Numpy Practice"""

    a = np.arange(100)
    b = np.linspace(0, 99, 10)
    c = np.arange(0, 10, 0.1)
    d = np.random.rand(10, 10)
    # e = a.reshape(10, 10)
    a.shape = (10, 10)
    f = a[4, 5]
    g = a[4]
    # h = d.sum()
    # i = a.max()
    # j = b.T
    # k = a + d
    l = a * d
    m = np.dot(a, d)
    return m


def main():
    print(numpy_practice())


if __name__ == '__main__':
    main()

