from turtle import *

import local_RU as RU


def levi():
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

    def levi_rec(order: int, size: float, color: str) -> None:
        '''
        Draws a Levi fractal of given order and size.

        Args:
            order (int): The recursion depth of the curve.
            size (float): The length of the initial line segment.
            color(str): Color of lines
        Returns:
            None
        '''

        pencolor(color)

        if order == 0:
            forward(size)
            return

        left(45)
        levi_rec(order - 1, size / 2, color)
        right(90)
        levi_rec(order - 1, size / 2, color)
        left(45)

    levi_rec(order, size, color)
    update()
    done()

if __name__ == '__main__':
    levi()