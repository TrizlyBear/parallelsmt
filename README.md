# Parallel SMT solver
This repository presents a parallel SMT solver. Solvers can be found in `solvers/`, any required binaries can be put in `bin/` (i.e. GoSAT). To run any solvers in parallel you can import the many function `import many from many`. You can run solvers like:
```py
import many from many
import solvers from library
many([solvers["bitwuzla"], solvers["gosat"]], util.fromFolder("bm/griggio",10), 60)
```
This will run Bitwuzla and GoSAT in parallel, solving the first 10 problems from the `griggio` benchmark (assuming it is present) with a timeout of 60 seconds.