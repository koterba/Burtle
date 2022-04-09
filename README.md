# Burtle

A Better TURTLE. Makes making games easier. <br><br>
Documentation & guide: https://alannxq.github.io/burtle/

## Installation

```Py
pip install burtle
```

## Usage

```Py
from burtle import Burtle, done


frog = Burtle("frog.gif")
bad_frog = Burtle("frog.gif")

frog.go(up=50)

frog.is_hitting(bad_frog)  # Returns False, as the two objects are not touching

done()  # Make sure the window does not close

```
