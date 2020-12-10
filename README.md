# Matplotlib Style for Mathematica

_Where to start for Mathematica-standard publication-quality plots in python._

**(TODO: add example plots)**

Mathematica has an ever-evolving brand guide for publications, presentations, and client-deliverable products. The `mprstyle` package applies a simple stylesheet to `matplotlib` and `seaborn` plots to match, as closely as possible, the specifications in the Mathematica brand guide. It also provides helper functions for formatting axis tick labels, color maps that match the Mathematica brand color scheme, 508-compliant categorical color scales, and so on.

## Installation
Install this package directly from github using `pipenv`:
```
$ pipenv install -e "git+https://github.com/mathematica-mpr/mplstyle-mathematica@0.0.1#egg=mplstyle-mathematica"
```

## Usage
Apply the style to `matplotlib` and `seaborn` plots by importing the `mprstyle` module and calling `apply()`:
```
import mprstyle
import matplotlib.pyplot as plt

mprstyle.apply("default")  # or "508"

f, a = plt.subplots()
x = list(range(0, 6, 0.01))
y1 = [sin(_) for _ in x]
y2 = [cos(_) for _ in x]
a.plot(x, y1, x, y2)
f.show()
```

**(TODO: add example plots)**

## TODO
 * Add `with` style functionality.
 * Document fonts.
 * Document helper functions.