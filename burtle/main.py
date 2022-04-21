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
    possible_keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','left','right','up','down']
    window.listen()
    for new_letter in possible_keys:
        if keyboard.is_pressed(new_letter):  # check for any keys 
            if new_letter == " ":
                new_letter = "space"  # change key name to space, so its easier for end user
            events.append(new_letter)

    return events

def done():
    turtle.done()

def mainloop(fps=60):
    CLOCK.tick(fps)
    window.update()
