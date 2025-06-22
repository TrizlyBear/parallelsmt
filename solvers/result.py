class Result():
    def __init__(self, done=True, expected="unknown", result=None,error=None, model=None, file=""):
        self.done = done
        self.expected = expected
        self.result = result
        self.error = error
        self.time = None
        self.solver = None
        self.model = model
        self.file = file

    def correct(self):
        return self.expected == self.result
    def __str__(self):
        res = ""
        res += f'{self.file if self.file != None else ""}'
        res += f'{"Correct" if self.correct() else ("Correct?" if self.expected == "unknown" else "Incorrect")}:\n\tExpected: {self.expected}\n\tResult: {self.result}'
        res += (("\n\tError: " + self.error) if self.error != None else "")
        res += (f'\n\tTook: {self.time}s' if self.time != None else "")
        res += (f'\n\tModel: {self.model}' if self.model != None else "")
        return res
