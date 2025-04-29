from turtle import *

scale_x = 40
scale_y = 60
offset_x = 200

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
        if not isinstance(number, int):
            raise TypeError("Число має бути цілим")
        if not (0 <= number <= 9999):
            raise ValueError("Число має бути від 0 до 9999")
        self._number = number
        self._digits = [int(d) for d in f"{number:04d}"]

    def __add__(self, other):
        return CisterianNumber(self._number + other._number)

    def __sub__(self, other):
        result = self._number - other._number
        if result < 0:
            raise ValueError("Результат віднімання не може бути від'ємним")
        return CisterianNumber(result)

    def draw_element(self, element, i, base_x, base_y):
        if i == 3:  # Одиниці
            x = base_x + scale_x
            y1 = base_y + scale_y
            y2 = base_y + 2 * scale_y / 3
        elif i == 2:  # Десятки
            x = base_x - scale_x
            y1 = base_y + scale_y
            y2 = base_y + 2 * scale_y / 3
        elif i == 1:  # Сотні
            x = base_x + scale_x
            y1 = base_y
            y2 = base_y + 1 * scale_y / 3
        elif i == 0:  # Тисячі
            x = base_x - scale_x
            y1 = base_y
            y2 = base_y + 1 * scale_y / 3
        else:
            return

        if element == hor_up:
            penup()
            goto(base_x, y1)
            pendown()
            goto(x, y1)
        elif element == hor_down:
            penup()
            goto(base_x, y2)
            pendown()
            goto(x, y2)
        elif element == descent:
            penup()
            goto(base_x, y1)
            pendown()
            goto(x, y2)
        elif element == ascend:
            penup()
            goto(base_x, y2)
            pendown()
            goto(x, y1)
        elif element == vert:
            penup()
            goto(x, y1)
            pendown()
            goto(x, y2)
        penup()

    def draw_digit(self, digit, i, base_x, base_y):
        if digit not in elements:
            return
        for elem in elements[digit]:
            self.draw_element(elem, i, base_x, base_y)

    def draw_number(self, base_x=0, base_y=0, label=None):
        penup()
        goto(base_x, base_y)
        pendown()
        goto(base_x, base_y + scale_y)
        penup()

        for i, digit in enumerate(self._digits):
            self.draw_digit(digit, i, base_x, base_y)
        if label:
            penup()
            goto(base_x, base_y - 50)
            write(label, align="center", font=("Arial", 12, "normal"))


def display_operation(num1, num2, operation):
    reset()
    hideturtle()
    speed(0)
    setup(width=1000, height=400)
    setworldcoordinates(-500, -200, 500, 200)

    num1.draw_number(base_x=-offset_x * 1.5, label=f"Число 1: {num1._number}")
    num2.draw_number(base_x=0, label=f"Число 2: {num2._number}")

    try:
        if operation == '+':
            result = num1 + num2
            result.draw_number(base_x=offset_x * 1.5, label=f"Сума: {result._number}")
        elif operation == '-':
            result = num1 - num2
            result.draw_number(base_x=offset_x * 1.5, label=f"Різниця: {result._number}")
    except ValueError as e:
        penup()
        goto(0, -100)
        write(str(e), align="center", font=("Arial", 12, "normal"))

    mainloop()


if __name__ == '__main__':
    num1 = CisterianNumber(6666)
    num2 = CisterianNumber(22)
    display_operation(num1, num2, '+')