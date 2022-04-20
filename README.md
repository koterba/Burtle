# Burtle

A Better TURTLE. Makes making games easier. <br><br>
Documentation & guide: https://alannxq.github.io/burtle/

## Installation

```Py
pip install burtle
```

## Usage

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
