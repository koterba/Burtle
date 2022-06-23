# Burtle 

A Better Turtle. Makes making games easier. <br><br>
Documentation & guide: https://alannxq.github.io/burtle/

## Installation

```Py
pip install burtle
```

## Basic example

```Py
from burtle import Burtle, run


ball = Burtle("black_circle")
ball.default_keys()  # WASD is used by default to move the burtle. Parameters include: Up, Down, Left, Right, speed

run()
```

## Event example

```Py
from burtle import Burtle, run, event


ball = Burtle("black_circle")  # this image is provided by default


@event  # any function with the "@event" decorator will be ran every frame
def move():
  ball.go(up=2)


run()  # fps can be specificed here, defaults to 60
```

## Collision detection example

```Py
from burtle import Burtle, run, event


frog = Burtle("frog.gif")  # you will need to have a file called "frog.gif" in your current directory
frog.go(up=50)

bad_frog = Burtle("frog.gif")

@event
def collision(): ## functions using the event decorator can have any name
  if frog.is_hitting(bad_frog):
    print("Frogs have collided!")


run()
```

## Gravity example

```Py
from burtle import Burtle, run, event


frog = Burtle("frog.gif")

@event
def grav():
  gravity(1)

run()
```

## Events example

```Py
from burtle import Burtle, run, event, key_events


frog = Burtle("frog.gif")
frog.go(up=50)
      
@event
def key_bindings():
  for key in key_events():
    if key == "w":
      frog.go(up=20)
    if key == "s":
      frog.go(down=20)

run()
```

## Image manipulation example

```Py
from burtle import Burtle, run


frog = Burtle("frog.gif")

frog.change_size(50)  # 100 is default, anything larger will make it bigger, e.g. 50 will half the image in size
      
run()
```

