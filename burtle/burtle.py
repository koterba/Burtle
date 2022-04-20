from turtle import Turtle
from .main import window
from PIL import Image
import turtle
import time 
import os


image_path = os.path.join(os.path.dirname(os.path.join(__file__)), "default_images")
white_rectangle = os.path.join(image_path, "white_rectangle.gif")
black_rectangle = os.path.join(image_path, "black_rectangle.gif")
white_circle = os.path.join(image_path, "white_circle.gif")
black_circle = os.path.join(image_path, "black_circle.gif")


all_burtles = []
current_id = 0
class Burtle(Turtle):
    def __init__(self, image=None, static=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if image == "white_rectangle":  # Preset images for the user
            self.image = white_rectangle
        elif image == "black_rectangle":
            self.image = black_rectangle
        elif image == "white_circle":
            self.image = white_circle
        elif image == "black_circle":
            self.image = black_circle
        else:
            self.image = image
        
        print("THIS IS IMAG" ,self.image)

        self.pil_image = None
        self.width = None
        self.height = None
        self.right = None
        self.left = None
        self.top = None
        self.bottom = None
        self.duplicated = False

        global current_id ## if two objects have the same image, allow for different dimensions when they are changed
        self.object_id = current_id ## by assigning a unique id when the new image is saved
        current_id += 1

        if self.image is not None: ## if image is passed, make turtle into an image, else its a normal turtle
            self.process_image()

        if not static:
            self.add_to_all_burtles()
    
    def process_image(self):
        self.convert_to_gif()
        turtle.addshape(self.image)
        self.setup_hitbox()
        self.shape(self.image)
        self.penup()


    def setup_hitbox(self):
        self.pil_image = Image.open(self.image)
        self.width, self.height = self.pil_image.size

        self.top = self.height // 2
        self.bottom = self.top
        self.left = self.width // 2
        self.right = self.left


    def change_size(self, percentage=None, static_size=None):
        self.duplicate_image()
        print(self.width)
        if static_size is not None:
            self.pil_image.resize((static_size, static_size)).save(
                self.new_image_path)
        else:
            self.calc_width = (self.width * percentage) // 100
            self.calc_height = (self.height * percentage) // 100
            self.pil_image.resize((self.calc_width, self.calc_height)).save(self.new_image_path)
        self.image = self.new_image_path
        self.process_image()
        print(self.width)


    def rotate(self, degrees):
        self.duplicate_image()
        img = Image.open(self.image)
        img = img.rotate(degrees, expand=1)
        img.save(self.new_image_path)
        self.image = self.new_image_path
        self.clear()
        self.process_image()


    def change_image(self, img_path):
        self.image = img_path
        self.process_image()


    def duplicate_image(self):
        if not self.duplicated:
            if "/" in self.image:
                slash_location = self.image.rfind("/") + 1  # +1 for the correct index below
                file_name = f"{self.object_id}_{self.image[slash_location:]}"
                file_dir = self.image[:slash_location]
                self.new_image_path = f"{file_dir}{file_name}"
            if "\\" in self.image:
                slash_location = self.image.rfind("\\") + 1  # +1 for the correct index below
                file_name = f"{self.object_id}_{self.image[slash_location:]}"
                file_dir = self.image[:slash_location]
                self.new_image_path = f"{file_dir}{file_name}"
            else:
                self.new_image_path = f"{self.object_id}_{self.image}"
            self.duplicated = True
        else:
            self.new_image_path = self.image


    def convert_to_gif(self):
        if "." in self.image:
            if self.image.split(".")[-1] != "gif":
                img = Image.open(self.image)
                self.image = f"{self.image.split('.')[0]}.gif"
                img.save(self.image)


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

    def add_to_all_burtles(self):
        global all_burtles

        all_burtles.append(self)

    def jump(self, height=25, jumps=-3, speed=0.02):
        for h in range(height, 0, jumps):
            self.go(up=h)
            window.update()
            time.sleep(speed)
