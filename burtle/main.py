from turtle import Turtle, Screen
from PIL import Image
import turtle


class Burtle(Turtle):
    def __init__(self, image_path=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image_path = image_path
        self.pil_image = None
        self.width = None
        self.height = None
        self.right = None
        self.left = None
        self.top = None
        self.bottom = None

        if image_path is not None:
            self.get_size()
            turtle.addshape(self.image_path)

            self.penup()
            self.shape(self.image_path)

    def get_size(self):
        self.pil_image = Image.open(self.image_path)
        self.width, self.height = self.pil_image.size
        self.top = self.height // 2
        self.bottom = self.top

        self.left = self.width // 2
        self.right = self.left

    def is_hitting(self, other):
        x_touch = False
        y_touch = False
        if self.xcor() - self.left <= other.xcor() - other.left <= self.xcor() + self.right:
            x_touch = True
        if self.xcor() - self.left <= other.xcor() + other.right <= self.xcor() + self.right:
            x_touch = True

        if self.ycor() + self.top >= other.ycor() + other.top >= self.ycor() - self.bottom:
            y_touch = True
        if self.ycor() + self.top >= other.ycor() - other.bottom >= self.ycor() - self.bottom:
            y_touch = True

        return True if x_touch and y_touch else False

    def is_clicked(self, x, y):
        x_touch = False
        y_touch = False
        if self.xcor() - self.left <= x <= self.xcor() + self.right:
            x_touch = True
        if self.xcor() - self.left <= x <= self.xcor() + self.right:
            x_touch = True

        if self.ycor() + self.top >= y >= self.ycor() - self.bottom:
            y_touch = True
        if self.ycor() + self.top >= y >= self.ycor() - self.bottom:
            y_touch = True

        return True if x_touch and y_touch else False

    def go(self, **kwargs):
        if "right" in kwargs:
            self.goto(self.xcor() + kwargs["right"], self.ycor())
        if "left" in kwargs:
            self.goto(self.xcor() - kwargs["left"], self.ycor())
        if "up" in kwargs:
            self.goto(self.xcor(), self.ycor() + kwargs["up"])
        if "down" in kwargs:
            self.goto(self.xcor(), self.ycor() - kwargs["down"])

    def look(self, direction):
        if direction == "up":
            self.seth(90)
        if direction == "down":
            self.seth(270)
        if direction == "left":
            self.seth(180)
        if direction == "right":
            self.seth(0)

    def l(self, n):
        self.seth(self.heading() + n)

    def r(self, n):
        self.seth(self.heading() + n)

    def tp(self, other):
        self.goto(other.xcor(), other.ycor())

    def draw_square(self, x=0, y=0, size=50, colour=None):
        self.seth(0)
        self.penup()
        self.goto(x,y)
        self.pendown()
        if colour is not None:
            self.fillcolor(colour)
            self.begin_fill()
        for i in range(4):
            self.forward(size)
            self.r(90)

        self.end_fill()

    def draw_grid(self, arr, size=50, special=None):
        y = (len(arr) * size) // 2
        default_x = 0 - (len(arr[0]) * size) // 2

        if special is not None:
            char = special[0]
            char_if = special[0]

        for row in arr:
            x = default_x
            for i in row:
                if special is not None and i == char:
                    self.draw_square(x, y, size, colour=special[1])
                else:
                    self.draw_square(x, y, size)
                x += size
            y -= size


BScreen = Screen


def done():
    turtle.done()


def mainloop():
    turtle.mainloop()
