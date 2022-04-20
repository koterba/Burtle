from turtle import Turtle, Screen
import keyboard
import pygame
import turtle

CLOCK = pygame.time.Clock()


BScreen = Screen
window = BScreen()
window.tracer(0, 0)

def events():
    global window
    events = []
    window.listen()
    for new_letter in 'abcdefghijklmnopqrstuvwxyz ':
        if keyboard.is_pressed(new_letter):  # check for any keys 
            if new_letter == " ":
                new_letter = "space"  # change key name to space, so its easier for end user
            events.append(new_letter)
    print(events)

    return events

def done():
    turtle.done()

def mainloop(fps=60):
    CLOCK.tick(fps)
    window.update()
