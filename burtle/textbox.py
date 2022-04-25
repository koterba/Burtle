from .burtle import Burtle
from functools import partial

class Textbox(Burtle):
    def __init__(self, x=0, y=0, box_height=50, box_width=200, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if x != 0 or y != 0:
            self.penup()
            self.goto(x, y)
        self.og_pos = self.pos()
        self.box_height = box_height
        self.box_width = box_width
        self.text = ""
        self.hideturtle()

        self.draw_box_outline()
        self.penup()
        self.goto(self.og_pos)

        self.update_text()


    def draw_box_outline(self):
        self.go(down=self.box_height // 2, left=self.box_width // 2)
        self.pendown()
        self.look("right")
        for _ in range(2):
            self.forward(self.box_width)
            self.r(90)
            self.forward(self.box_height)
            self.r(90)

    def update_text(self, char=""):
        self.clear()
        self.penup()
        self.goto(self.og_pos)
        self.draw_box_outline()
        self.penup()
        self.goto(self.og_pos)
        self.go(down=10)
        self.text += char
        self.write(f"{self.text}", align="center", font=('Iosevka NF', 15, 'normal'))

    def remove_text(self):
        self.text = self.text[:-1]
        self.update_text()

    def get_input(self, wn):
        wn.listen()
        for new_letter in 'abcdefghijklmnopqrstuvwxyz':
            func = partial(self.update_text, new_letter)
            wn.onkeypress(func, new_letter)
            func = partial(self.update_text, new_letter.upper())
            wn.onkeypress(func, new_letter.upper())
        wn.onkeypress(lambda: self.update_text(' '), 'space')
        wn.onkeypress(self.remove_text, "BackSpace")