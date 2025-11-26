from turtle import *

import local_RU as RU

def tree():
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

    def tree_drawing(order: int, size: float, color: str) -> None:
        '''
        Draws a binar tree fractal of given order and size
        Args:
            order(int): The recursion depth of the curve
            size(float): The length of the initial line segment
            color(str): Color of lines
        Returns:
            None
        '''
        pencolor(color)

        if size > 5:
            # Рисуем ветку
            forward(size)

            # Поворачиваем направо и рисуем правую ветку
            right(20)
            tree_drawing(order, size - 15, color)

            # Поворачиваем налево и рисуем левую ветку
            left(40)
            tree_drawing(order, size - 15, color)

            # Возвращаемся в исходное положение
            right(20)
            backward(size)


    left(90)
    penup()
    goto(0, -100)
    pendown()

    tree_drawing(order, size, color)
    update()
    exitonclick()


if __name__ == '__main__':
    tree()

