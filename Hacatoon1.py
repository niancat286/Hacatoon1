from turtle import *

scale_x = 40
scale_y = 60

hor_up = 1
hor_down = 2
descent = 3
ascend = 4
vert = 6

elements = {
    0: (),
    1: (hor_up,),
    2: (hor_down,),
    3: (descent,),
    4: (ascend,),
    5: (hor_up, ascend),
    6: (vert,),
    7: (hor_up, vert),
    8: (hor_down, vert),
    9: (hor_up, hor_down, vert)
}


class CisterianNumber:
    def __init__(self, number):
        if not (0 <= number <= 9999):
            raise ValueError("Number must be between 0 and 9999")
        self._number = number
        self._digits = [0] * (4 - len(str(number))) + [int(d) for d in str(number)]

    def draw_element(self, element, i):
        down()
        goto(0, scale_y)
        if i == 3:
            x = scale_x
            y1 = scale_y
            y2 = 2*scale_y/3
        if i == 2:
            x = - scale_x
            y1 = scale_y
            y2 = 2 * scale_y / 3
        if i == 1:
            x = scale_x
            y1 = 0
            y2 = 1 * scale_y / 3
        if i == 0:
            x = - scale_x
            y1 = 0
            y2 = 1 * scale_y / 3


        if element == hor_up:
            goto(0, y1)
            goto(x, y1)
            up()

        elif element == hor_down:
            goto(0, y2)
            goto(x, y2)
            up()

        elif element == descent:
            goto(0, y1)
            goto(x, y2)
            up()

        elif element == ascend:
            goto(0, y2)
            goto(x, y1)
            up()

        elif element == vert:
            up()
            goto(x, y1)
            down()
            goto(x, y2)
            up()

        penup()
        goto(0, 0)

    def draw_digit(self, digit, i):
        if digit not in elements:
            return
        penup()
        goto(0, 0)
        pendown()
        for elem in elements[digit]:
            self.draw_element(elem, i)

    def draw_number(self):
        for i, digit in enumerate(self._digits):
            self.draw_digit(digit, i)


if __name__ == '__main__':
    num1 = CisterianNumber(1993)
    num1.draw_number()
    mainloop()