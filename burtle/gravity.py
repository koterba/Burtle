from .burtle import all_burtles

def gravity(strength):
    global all_burtles
    for burtle in all_burtles:
        burtle.go(down=strength)