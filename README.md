[![issues](https://img.shields.io/github/issues/Lukas0025/MOGpy)](https://github.com/Lukas0025/MOGpy/issues)
[![closed issues](https://img.shields.io/github/issues-closed-raw/Lukas0025/MOGpy)](https://github.com/Lukas0025/MOGpy/issues)
[![size](https://img.shields.io/github/repo-size/Lukas0025/MOGpy)](https://github.com/Lukas0025/MOGpy/)
[![last commit](https://img.shields.io/github/last-commit/Lukas0025/MOGpy)](https://github.com/Lukas0025/MOGpy/)

Python lib for molecular genetic

### Install from pip

```sh
pip3 install MOGpy
```

### Install from source

```
git clone https://github.com/Lukas0025/MOGpy.git
cd MOGpy
make install
```

## Getting started

### simple example

```python
import MOGpy

chromA = MOGpy.BioChromosome.fromStr("AATTCTAAACGCGAAACGGTTGACATGTGGGTTGGAGCC")
chromB = MOGpy.BioChromosome.fromStr("AA")
chromC = chromA + chromB

# show chromosome
chromC.show()

# show histogram
chromC.hist()

# calculate complement
chromD = chromC.complement()

# calculate reversed complement
chromE = chromC.reverse().complement()

# print all chromosomes
print(chromA.seq())
print(chromB.seq())
print(chromC.seq())
print(chromD.seq())
print(chromE.seq())
```

## Getting help

* Examples in examples dir
* Issues: https://github.com/Lukas0025/MOGpy/issues

## Reporting bugs and contributing

* Want to report a bug or request a feature? Please open [an issue](https://github.com/MOGpy/python-pixabay/issues/new).
* Want to help us with build? Contact me

## Licensing

MOGpy is licensed under GPL