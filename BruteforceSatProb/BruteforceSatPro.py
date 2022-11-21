import math
from BruteforceSatProb.Cnf import Cnf


# The formula
phi = []
# Number clauses in the formula
clauses = 0
# Number of variables in the formula
variables = 0
data1 = 'aim-50-1_6-yes1-4.cnf'
data2 = 'simple_v3_c2.cnf'
data3 = 'quinn.cnf'
# A set of all different variables in the formula
xdict = set()
# Number of saturated formulas
satNum = 0
# The current assignment of the variables in the formula
currentAssignment = []
# Read in the CNF files
with open(data2) as f:
    for line in f:
        if 'c ' in line:
            continue
        else:
            phi.append(line.split())
            for x in phi:
                if 'c' in x:
                    x.remove('c')
                elif 'p' in x:
                    x.remove('p')
                elif 'cnf' in x:
                    x.remove('cnf')
                else:
                    continue
    phi = [x for x in phi if x]
    variables = phi[0][0]
    clauses = phi[0][1]
    phi.remove(phi[0])
f.close


# initialization of the variables
def initialization(formula):
    """Initializes the assignments for the variables

    Parameters
    ----------
    :param formula: list
        The formula
    :return:
    """
    global xdict
    global currentAssignment
    # Get all variables for the set
    for x in formula:
        for y in x:
            if y == '0':
                break
            else:
                xdict.add(abs(int(y)))
    for x in range(max(xdict)):
        currentAssignment.append(2)
    for x in xdict:
        currentAssignment[x - 1] = 0

p = 1
phiOne = Cnf(phi)
initialization(phiOne.formula)
# Go through all possible assignments of the variables
for i in range(int(math.pow(2, int(variables)))):
    # If the formula is satisfiable
    if phiOne.eval(currentAssignment):
        satNum += 1
    currentAssignment = phiOne.nextAssignment(currentAssignment)

# calculate the satisfaction probability
satProb = satNum / (int(math.pow(2, int(variables))))
if satProb < p:
    print("Not Satisfiable")
else:
    print("Satisfiable")
