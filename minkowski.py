from turtle import *

import local_RU as RU


def minkowski():
    speed(0)
    screen = Screen()
    screen.tracer(0)

    print('=' * 40)
    order = int(input(RU.CHOOSE_DEPTH))
    print('=' * 40)
    size = int(input(RU.CHOOSE_LEN))
    print('=' * 40)
    color = input((RU.CHOOSE_COLOR))
    print('=' * 40, '\n')

    print(RU.CREATING)

    def minkowski_rec(order: int, size: float, color: str) -> None:
        '''
        Draws a minkowski fractal of given order and size
        Args:
            order(int): The recursion depth of the curve
            size(float): The length of the initial line segment
            color(str): Color of lines
        Returns:
            None
        '''

        pencolor(color)

        if order == 0:
            forward(size)
            return

        segment_length = size / 4

        minkowski_rec(order - 1, segment_length, color)
        left(90)
        minkowski_rec(order - 1, segment_length, color)
        right(90)
        minkowski_rec(order - 1, segment_length, color)
        right(90)
        minkowski_rec(order - 1, segment_length, color)
        minkowski_rec(order - 1, segment_length, color)
        left(90)
        minkowski_rec(order - 1, segment_length, color)
        left(90)
        minkowski_rec(order - 1, segment_length, color)
        right(90)
        minkowski_rec(order - 1, segment_length, color)

    minkowski_rec(order, size, color)
    update()
    done()

if __name__ == '__main__':
    minkowski()