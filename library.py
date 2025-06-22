import solvers.z3 as Z3Solver
import solvers.cvc5 as CVC5Solver
import solvers.bitwuzla as BitwzlaSolver
import solvers.gosat as GosatSolver

solvers = {
    "z3": Z3Solver.Z3().solve,
    "cvc5": CVC5Solver.CVC5().solve,
    "bitwuzla": BitwzlaSolver.Bitwuzla().solve,
    "bitwuzlaprop": BitwzlaSolver.Bitwuzla().solveprop,
    "gosat": GosatSolver.Gosat().solve
}