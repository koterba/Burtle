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


frog = Burtle("frog.gif")
frog.go(up=50)

bad_frog = Burtle("frog.gif")


while True:
  mainloop(fps=60)  # we can set any custom fps value here
  
  if frog.is_hitting(bad_frog):
    print("Frogs collided!")

```

## Key press example

```Py
from burtle import Burtle, mainloop, events


frog = Burtle("frog.gif")
frog.go(up=50)


def keybinds():
  for event in events():
    if "w" in event:
      frog.go(up=20)
     elif "s" in event:
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
