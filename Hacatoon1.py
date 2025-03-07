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
    def draw_element(self, element):

        down()
        goto(0, scale_y)


        if element == hor_up:
            goto(0, scale_y)
            goto(scale_x, scale_y)
            up()


        elif element == hor_down:
            goto(0, 2*scale_y/3)
            goto(scale_x, 2*scale_y/3)
            up()


        elif element == descent:
            goto(0, scale_y)
            goto(scale_x, 2*scale_y/3)
            up()


        elif element == ascend:
            goto(0, 2*scale_y/3)
            goto(scale_x, scale_y)
            up()

        elif element == vert:
            up()
            goto(scale_x, scale_y)
            down()
            goto(scale_x, 2*scale_y/3)
            up()

        penup()
        goto(0, 0)

    def draw_digit(self, digit):
        if digit not in elements:
            return
        penup()
        goto(0, 0)
        pendown()
        for elem in elements[digit]:
            self.draw_element(elem)

    def draw_number(self):
        for digit in self._digits:
            self.draw_digit(digit)


num1 = CisterianNumber(6)
num1.draw_number()
mainloop()