from .globals import solid_objects, burtle_keybinds, movable_objects
from .window import window
import pygame
import turtle


CLOCK = pygame.time.Clock()


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