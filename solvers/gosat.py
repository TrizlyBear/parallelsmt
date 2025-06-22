from .result import Result
import subprocess
import threading
from .z3 import satunsat
import os

class Gosat():
    def __init__(self):
        pass
    def solve(self, file) -> Result:
        res = {}
        def runner():
            try:
                expected = satunsat(file.content)
                result = subprocess.run(
                    ["./bin/gosat", "-f", file.path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    check=True,
                )
                ress = result.stdout.split(",")
                if ress[1] == "sat" and (expected == "sat" or expected == "unknown"):
                    res["res"] = Result(done=True, expected="sat", result="sat", model="gosat", file=file.path)
                elif ress[1] == "unknown" and expected == "unsat":
                    res["res"] = Result(done=True, expected="unsat", result="unsat", model="gosat", file=file.path)
                else:
                    res["res"] = Result(done=True, expected=expected, result="unknown", error="Stochastic err", model="gosat", file=file.path)
            except subprocess.CalledProcessError as e:
                # print(e.output)
                res["res"] = Result(done=False, error=e.stderr)
        thread = threading.Thread(target=runner)
        thread.start()
        thread.join()
        return res["res"]
