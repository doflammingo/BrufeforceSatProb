from IO.CnfParser import CnfParser
from Module.Assignment import Assignment
from Utils.Exponent import Exponent
from fractions import Fraction

# The formula
phi = []
# Number clauses in the formula
clauses = 0
# Number of variables in the formula
variables = 0
# All example files
data1 = '..\\IO\\aim-50-1_6-yes1-4.cnf'
data2 = '..\\IO\\simple_v3_c2.cnf'
data3 = '..\\IO\\quinn.cnf'
data4 = '..\\IO\\difSimple.cnf'
# Number of satisfiable formulas
numSat = 0


readInData = CnfParser()
phi = readInData.ReadInputData(data2)
variables = readInData.getVariables()
clauses = readInData.getClauses()
p = 1

boolAssignment = Assignment(variables)
exponentClass = Exponent()

def run():
    """Runs the main code for the Bruteforce algorithm
    It goes through all the combinations of assignments for the variables and counts the satisfiable assignments before
    calculating the satisfaction probability
    """
    # Go through all possible assignments of the variables. Not assigned variables are subtracted
    global numSat
    global currentAssignment
    for i in range(exponentClass.exponent(2, variables - boolAssignment.currentAssignment.count(2))):
        # If the formula is satisfiable
        if phi.eval(boolAssignment.currentAssignment):
            numSat += 1
        boolAssignment.currentAssignment = boolAssignment.nextAssignment()
    # calculate the satisfaction probability
    satProb = Fraction(numSat, exponentClass.exponent(2, variables))
    print(satProb)

    if satProb < p:
        print("satisfaction probability is above p")
    else:
        print("satisfaction probability is not above p")

if __name__ == "__main__":
    run()