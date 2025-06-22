import z3
from . import result
def satunsat(inp):
    if "(set-info :status sat)" in inp.split('\n'):
        return "sat"
    elif "(set-info :status unsat)" in inp.split('\n'):
        return "unsat"
    elif "(set-info :status unknown)" in inp.split('\n'):
        return "unknown"
    return None

class Z3():
    def __init__(self):
        pass

    def solve(self, file):
        try:
            filecontents = file.content
            ast = z3.parse_smt2_string(filecontents)
            excepted = satunsat(filecontents)
            s = z3.Solver()
            s.add(ast)
            r = s.check()
            if r == z3.unsat:
                z3result = "unsat"
            elif r == z3.unknown:
                z3result = "unknown"
            elif r == z3.sat:
                z3result = "sat"
            res = result.Result(expected=excepted, result=z3result, file=file.path)
            res.model = "z3"
            return res 
        except Exception as e:
            raise e
        # print(res)