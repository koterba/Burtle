# Burtle

A Better TURTLE. Makes making games easier. <br><br>
Write Less Do More!<br><br>
Documentation & guide: https://alannxq.github.io/burtle/

## Installation

```Py
pip install burtle
```

## Basic example

```Py
from burtle import Burtle, mainloop


frog = Burtle("frog.gif")
frog.default_keys()  # you can specify any keys, but it will bind them to WASD by default, speed can be specified too

while True:
  mainloop()
```

## Collision detection example

```Py
from burtle import Burtle, mainloop


frog = Burtle("frog.gif")  # you will need to have a file called "frog.gif" in your current directory
frog.go(up=50)

bad_frog = Burtle("frog.gif")


while True:
  mainloop(fps=60)  # we can set any custom fps value here
  
  if frog.is_hitting(bad_frog):
    print("Frogs collided!")

```

## Gravity example

```Py
from burtle import Burtle, mainloop, gravity


frog = Burtle("frog.gif")


while True:
  mainloop(fps=60)  # we can set any custom fps value here
  gravity(1)  # thats all it is, just add the strength of the gravity
  # also important to add a floor and check for collision as it will simple fall
  # through otherwise

```

## Events example

```Py
from burtle import Burtle, mainloop, events


frog = Burtle("frog.gif")
frog.go(up=50)
      

while True:
  mainloop(fps=60)  # we can set any custom fps value here
  
  for key in events():
    if key == "w":
      frog.go(up=20)
    if key == "s":
      frog.go(down=20)

```

## Image manipulation example

```Py
from burtle import Burtle, mainloop


frog = Burtle("frog.gif")

frog.change_size(50)  # 100 is default, anything larger will make it bigger, e.g. 50 will half the image in size
      

while True:
  mainloop(fps=60)  # we can set any custom fps value here
```
