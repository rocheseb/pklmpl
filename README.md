# README

## Installation

```
    git clone https://github.com/rocheseb/pklmpl
    python -m pip install pklmpl
```

OR

    pip install git+https://github.com/rocheseb/pklmpl

## Usage

### Save figure

```
import pklmpl
from matplotlib import pylab

fig, ax = pylab.subplots()
    
pklmpl.pickle_mpl_figure(fig,"matplotlib_figure.pickle")
```

### Open saved figure

#### within a python script

```
import pklmpl
    
pklmpl.open_pickled_mpl_figure("matplotlib_figure.pickle")
```

#### with the console entry point

    pklmpl /path/to/matplotlib_figure.pickle

