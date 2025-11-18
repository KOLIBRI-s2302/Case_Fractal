from turtle import *

import local_RU as RU

INNER_ANGLE = 60
OUTER_ANGLE = 120
FRACTAL_SIDES = 3
HORIZONTAL_CENTERING_FACTOR = 2
VERTICAL_CENTERING_FACTOR = 4


def koch(order: int, size: float) -> None:
    '''
    Draws a Koch curve with specified
    recursion depth and size.
    Args:
        order: Recursion depth for the fractal.
        size: Length of the initial segment.
    '''
    if order == 0:
        forward(size)
    else:
        koch(order - 1, size / 3)
        left(INNER_ANGLE)
        koch(order - 1, size / 3)
        right(OUTER_ANGLE)
        koch(order - 1, size / 3)
        left(INNER_ANGLE)
        koch(order - 1, size / 3)


def draw_koch_snowflake() -> None:
    '''
    Handles user input and draws
    the Koch snowflake.
    '''
    try:
        print('=' * 40)
        recursion_depth = int(input(RU.CHOOSE_DEPTH))
        if recursion_depth < 0:
            print(RU.INVALID_DEPTH)
            return
        print('=' * 40)
        side_length = float(input(RU.CHOOSE_LEN))
        print('=' * 40)
        if side_length <= 0:
            print(RU.INVALID_LEN)
            return

    except ValueError:
        print(RU.INVALID_ENTER)
        return
    print(RU.CREATING)

    setup_screen()
    up()
    goto(-side_length / HORIZONTAL_CENTERING_FACTOR, side_length / VERTICAL_CENTERING_FACTOR)
    down()

    for _ in range(FRACTAL_SIDES):
        koch(recursion_depth, side_length)
        right(360 / FRACTAL_SIDES)

    update()
    done()


def setup_screen() -> None:
    '''
    Initializes the turtle graphics window.
    '''
    reset()
    speed(0)
    tracer(0, 0)


if __name__ == '__main__':
    draw_koch_snowflake()
