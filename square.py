from turtle import *

import local_RU as RU


def square():
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

    def sqr_rec(order: int, size: float, color: str) -> None:
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
            return
        for i in range(0, 4):
            down()
            forward(size)
            right(90)
        up()
        forward(size * 0.1)
        right(15)
        down()
        sqr_rec(order - 1, size * 0.9, color)

    sqr_rec(order, size, color)
    update()
    exitonclick()

if __name__ == '__main__':
    square()