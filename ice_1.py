from turtle import *

import local_RU as RU


def ice():
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
    tracer(10)
    penup()
    goto(-200, 0)
    pendown()

    def ice_rec(order: int, size: float, color: str) -> None:
        '''
        Draws a ice fractal of given order and size
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
            ice_rec(order - 1, size / 2, color)
            left(90)
            ice_rec(order - 1, size / 4, color)
            left(180)
            ice_rec(order - 1, size / 4, color)
            left(90)
            ice_rec(order - 1, size / 2, color)

    ice_rec(order, size, color)
    update()
    exitonclick()

if __name__ == '__main__':

    ice()
