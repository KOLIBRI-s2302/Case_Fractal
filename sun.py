from turtle import *

import local_RU as RU


def sun():
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

    # Sun Fractal
    def sun_rec(order: int, size: float, color: str) -> None:
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
            forward(size)
        else:
            for side in range(2):
                sun_rec(order - 1, size, color)
                right(60)
                sun_rec(order - 1, size, color)
                left(120)
                sun_rec(order - 1, size, color)
                right(60)
                sun_rec(order - 1, size, color)
                right(150)
                sun_rec(order - 1, size * 3  0.5, color)
                left(120)
                sun_rec(order - 1, size * 3  0.5, color)
                right(150)

    sun_rec(order, size, color)
    update()
    exitonclick()

if name == 'main':
    sun()
