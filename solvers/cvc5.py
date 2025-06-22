
import cvc5
from . import result

class CVC5():

    def __init__(self):
        pass

    def solve(self, file):
        filecontents = file.content
        self.solver = cvc5.Solver()
        self.solver.setOption("input-language", "smtlib")
        self.parser = cvc5.InputParser(self.solver)
        self.parser.setStringInput(cvc5.InputLanguage.SMT_LIB_2_6, filecontents, "CVC5 Solver")
        while True:
            cmd = self.parser.nextCommand()
            if cmd.isNull():
                break
            elif str(cmd) == "(set-info :status sat)":
                expected = "sat"
            elif str(cmd) == "(set-info :status unsat)":
                expected = "unsat" 
            elif str(cmd) == "(set-info :status unknown)":
                expected = "unknown" 
            res = cmd.invoke(self.solver, self.parser.getSymbolManager())
            if res == "sat\n":
                cvcresult = "sat"
            elif res == "unsat\n":
                cvcresult = "unsat"
            elif res == "unknown\n":
                cvcresult = "unknown"
        return result.Result(expected=expected, result=cvcresult, model="cvc5", file = file.path)
            

        