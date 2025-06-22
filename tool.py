#!/usr/bin/env python3

import argparse
import solvers.cvc5 as CVC5Solver
import solvers.z3 as Z3Solver
from solvers.result import Result
import time
import library
import logging
import asyncio

# A solver should be function that returns a Result class
def run(solver, filecontent) -> Result:
    start = time.time()
    res = solver(filecontent)
    stop = time.time()
    res.time = (stop - start)
    return res

if __name__ == '__main__':
    parser = argparse.ArgumentParser("SMT tool")
    parser.add_argument("backend", choices=library.solvers.keys())
    parser.add_argument("smtfile")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level = logging.INFO)

    with open(args.smtfile, "r") as f:
        smtfile = f.read()

    solverbackend = library.solvers[args.backend]
    res = run(solverbackend, smtfile)
    print(res)