from functools import partial
from .globals import burtle_keybinds
from .logic import window
import keyboard



def key_events():
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


def key_binder(burtle, speed, Up, Down, Left, Right):
    for key in key_events():
        if key == Up and not burtle.top_hitting:
            burtle.go(up=speed)
        if key == Down and not burtle.bottom_hitting:
            burtle.go(down=speed)
        if key == Left and not burtle.left_hitting:
            burtle.go(left=speed)
        if key == Right and not burtle.right_hitting:
            burtle.go(right=speed)


def key_setter(burtle, Up, Down, Left, Right, speed):
    global burtle_keybinds
    func = partial(key_binder, burtle, speed, Up, Down, Left, Right)
    burtle_keybinds.append(func)
