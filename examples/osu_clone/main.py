from burtle import Burtle, BScreen, done
import threading
import random
import time


score = 0
distance = 10
seconds = 0
time_start = 0
started = False

wn = BScreen()
wn.tracer(0)
wn.bgcolor("black")

eks = Burtle("eks.gif")
eks.go(up=350, left=420)

bad_frog = Burtle("frog.gif")
bad_frog.go(up=1000, right=1000)
circle = Burtle("hitcircle.gif")
text = Burtle()
text.penup()
text.pencolor("white")
text.hideturtle()
text.go(up=350)
text.write(f"Score: {score}", align="center", font=("impact", 24))

wn.listen()
wn.onkeypress(lambda dis=distance: circle.go(up=dis), "w")
wn.onkeypress(lambda dis=distance: circle.go(down=dis), "s")
wn.onkeypress(lambda dis=distance: circle.go(left=dis), "a")
wn.onkeypress(lambda dis=distance: circle.go(right=dis), "d")

running = True


def clicked(x, y):
    global score, started, time_start

    if eks.is_clicked(x, y):
        circle.tp(bad_frog)

    if circle.is_clicked(x, y):
        if not started:
            time_start = time.time()
            started = True

        score += 1
        circle.goto(random.randint(-350, 300), random.randint(-350, 300))
        text.clear()
        text.write(f"Score: {score}", align="center", font=("impact", 24))


while score < 10:
    if circle.is_hitting(bad_frog):
        quit()

    wn.onclick(clicked)

    wn.update()


time_taken = round(time.time() - time_start, 2)
print(time_taken)
quit()
