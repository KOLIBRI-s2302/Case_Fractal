from turtle import *

import local_RU as RU


def carpet():
    speed(0)
    screen = turtle.Screen()
    screen.tracer(0)

    print('=' * 40)
    depth = int(input(RU.CHOOSE_DEPTH))
    print('=' * 40)
    size = int(input(RU.CHOOSE_LEN))
    print('=' * 40)
    color = input((RU.CHOOSE_COLOR))
    print('=' * 40, '\n')

    print(RU.CREATING)

    def carp_rec(size, depth, color) -> None:
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
        if depth == 0:
            forward(size)
            return

        for i in range(4):
            carp_rec(size, depth - 1, color)

            if i < 3:
                right(90)
                carp_rec(size * 0.5, depth - 1, color)
                backward(size * 0.5)
                left(90)

            right(90)

    carp_rec(size, depth, color)
    update()
    exitonclick()

if __name__ == '__main__':
    carpet()
