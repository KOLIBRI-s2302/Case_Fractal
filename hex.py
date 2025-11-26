from turtle import *

import local_RU as RU


def hex():
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

    setup(width=1200, height=800)
    penup()
    goto(-200, 0)
    pendown()

    def hexagon_fractal(order: int, size: float, color):
        '''
        Draws a Author fractal of given order and size
        Args:
            order(int): The recursion depth of the curve
            size(float): The length of the initial line segment
            color(str): Color of lines
        Returns:
            None
        '''
        pencolor(color)
        if order == 0:
            for _ in range(6):
                forward(size)
                left(60)
            return

        for _ in range(6):
            forward(size)
            left(60)

        for _ in range(6):
            forward(size)
            hexagon_fractal(order - 1, size * 0.5, color)
            backward(size)
            left(60)

    hexagon_fractal(order, size, color)
    update()
    done()

if __name__ == '__main__':

    hex()
