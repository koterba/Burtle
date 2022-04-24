# Burtle

A Better TURTLE. Makes making games easier. <br><br>
Documentation & guide: https://alannxq.github.io/burtle/

## Installation

```Py
pip install burtle
```

## Basic example

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

## Key press example

```Py
from burtle import Burtle, mainloop, events


frog = Burtle("frog.gif")
frog.go(up=50)


def keybinds():
  for event in events():
    if event == "w":
      frog.go(up=20)
     elif event == "s":
      frog.go(down=20)
      

while True:
  mainloop(fps=60)  # we can set any custom fps value here
  keybinds()  # here we run our keybinds function to continue getting new key presses

```

## Image manipulation example

```Py
from burtle import Burtle, mainloop


frog = Burtle("frog.gif")

frog.change_size(50)  # 100 is default, anything larger will make it bigger, e.g. 50 will half the image in size
      

while True:
  mainloop(fps=60)  # we can set any custom fps value here
```
