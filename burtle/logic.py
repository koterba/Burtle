from .globals import solid_objects, burtle_keybinds, movable_objects, function_events
from .window import window
import pygame
import turtle


CLOCK = pygame.time.Clock()
burtle_playing = True


def done():
    turtle.done()


def mainloop(fps=60):
    CLOCK.tick(fps)
    window.update()

    for key_presets in burtle_keybinds:
        key_presets()
    
    for obstacle in solid_objects:
        for burtle in movable_objects:
            burtle.is_hitting(obstacle)

def run(fps=60):
    while burtle_playing:
        mainloop(fps)

        for func in function_events:
            func()
