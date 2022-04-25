from .globals import affected_by_gravity

def gravity(strength):
    for burtle in affected_by_gravity:
        burtle.go(down=strength)