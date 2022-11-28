from BruteforceSatProb.Cnf import Cnf
from BruteforceSatProb.ReadIn import ReadIn
from BruteforceSatProb.Assignment import Assignment
from BruteforceSatProb.Exponent import Exponent
from fractions import Fraction

# The formula
phi = []
# Number clauses in the formula
clauses = 0
# Number of variables in the formula
variables = 0
# All example files
data1 = 'aim-50-1_6-yes1-4.cnf'
data2 = 'simple_v3_c2.cnf'
data3 = 'quinn.cnf'
data4 = 'difSimple.cnf'
# A set of all different variables in the formula
varDict = set()
# Number of saturated formulas
numSat = 0
# The current assignment of the variables in the formula
currentAssignment = []

readInData = ReadIn()
phi = readInData.ReadInputData(data2)
variables = readInData.getVariables()
clauses = readInData.getClauses()

p = 1
phiOne = Cnf(phi)
boolAssignment = Assignment()
exponentClass = Exponent()

def main():
    # initialize the current Assignment
    initialization(phiOne.formula)
    # Go through all possible assignments of the variables. Not assigned variables are subtracted
    global numSat
    global currentAssignment
    for i in range(exponentClass.exponent(2, int(variables) - currentAssignment.count(2))):
        # If the formula is satisfiable
        if phiOne.eval(currentAssignment):
            numSat += 1
        currentAssignment = boolAssignment.nextAssignment(currentAssignment)
    # calculate the satisfaction probability
    satProb = Fraction(numSat, exponentClass.exponent(2, int(variables)))
    print(satProb)
    if satProb < p:
        print("Not Satisfiable")
    else:
        print("Satisfiable")

def initialization(formula):
    """Initializes the assignments for the variables
    It takes all the variables of the formula and then initializes them in to a int array,
    to assign them "bool"(in that case number 1,0) values

    Parameters
    ----------
    :param formula: list
        The formula
    """

    # Get all variables for the set
    for x in formula:
        for y in x:
            if y == '0':
                break
            else:
                varDict.add(abs(int(y)))
    # Set all to not defined
    for x in range(max(varDict)):
        currentAssignment.append(2)
    # If variable is present in the formula, set to false
    for x in varDict:
        currentAssignment[x - 1] = 0








if __name__ == "__main__":
    main()