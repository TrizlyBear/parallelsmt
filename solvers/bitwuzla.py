from bitwuzla import *
from .z3 import satunsat
from .result import Result

class Bitwuzla():
    def __init__(self):
        pass

    def solveprop(self, filecontents):
        expected = satunsat(filecontents.content)
        tm = TermManager()
        options = Options()
        options.set(Option.BV_SOLVER, 'prop')
        parser = Parser(tm, options)
        parser.parse(filecontents.content, True, False)
        res = parser.bitwuzla().check_sat()
        return Result(expected=expected, result=str(res), model="bitwuzla", file=filecontents.path)

    def solve(self, filecontents):
        expected = satunsat(filecontents.content)
        tm = TermManager()
        options = Options()
        parser = Parser(tm, options)
        parser.parse(filecontents.content, True, False)
        res = parser.bitwuzla().check_sat()
        return Result(expected=expected, result=str(res), model="bitwuzla", file=filecontents.path)