from .globals import function_events

def event(func):
    function_events.append(func)

