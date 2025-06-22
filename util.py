import os
import stat
import os
import math

def solverFromCommand(invocation, resultfunction):
    pass

def fromFolder(path, limit=10, slot=False):
    res = []
    for root,_,files in os.walk(path):
        files.sort()
        for f in files:
            if limit <= 0:
                break
            if not f.endswith(".smt2"):
                continue
            try:
                if slot and stat.S_ISREG(os.stat("./bmslot/"+f+".slot.smt2").st_mode):
                    res.append(File(os.path.abspath("./bmslot/"+f+".slot.smt2")))
                else:
                    res.append(File(os.path.join(root, f)))
                if limit != math.inf:
                    limit -= 1
            except:
                pass
    return res

class File():
    def __init__(self, filename=None):
        if filename is None:
            return
        st = os.stat(filename)
        if stat.S_ISREG(st.st_mode):
            self.filename = os.path.basename(filename)
            self.path = os.path.abspath(filename)
            with open(filename, "r") as f:
                    self.content = f.read()
            
        else:
            print(f'Could not find file: {filename}')
            

