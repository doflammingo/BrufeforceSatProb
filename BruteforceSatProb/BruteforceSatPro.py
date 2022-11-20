import itertools
import math
from BruteforceSatProb.Cnf import Cnf
from BruteforceSatProb.Assignment import Assignment


sigma =[]
clauses = 0
variables = 0
data1='aim-50-1_6-yes1-4.cnf'
data2='simple_v3_c2.cnf'
data3='quinn.cnf'
xdict =set()
satComb = 0

#Read in the CNF files
with open(data2) as f:
    for line in f:
        if 'c ' in line:
            continue
        else:
            sigma.append(line.split())
            for x in sigma:
                if 'c' in x:
                    x.remove('c')
                elif 'p' in x:
                    x.remove('p')
                elif 'cnf' in x:
                    x.remove('cnf')
                else:
                    continue
    sigma = [x for x in sigma if x]
    variables=sigma[0][0]
    clauses=sigma[0][1]
    sigma.remove(sigma[0])
f.close

#initialization of the variables
def initialization(formula):
    for x in formula:
        for y in x:
            if y =='0':
                break
            else:
                xdict.add(abs(int(y)))

#calculation of the cnf equations
def satisfactionProbability(formula, k, p):
    endResult=False
    end=[]
    #Go through all clauses in the variable
    for num1,x in enumerate(formula):
        for num2,y in enumerate(x):
            if formula[num1][num2]=='0':
                break
            else:
                #
                if int(formula[num1][num2]) < 0:
                    l= not boolAssignments.boolComb[abs(int(formula[num1][num2])) - 1]
                else:
                    l=boolAssignments.boolComb[int(formula[num1][num2]) - 1]

                endResult = endResult or l
        end.append(endResult)
    for num,x in enumerate(end):
        endResult = endResult and end[num]
    return endResult



s1 = Cnf(sigma)
print(s1.formula)
boolAssignments = Assignment(int(variables))

#For all variables in the formula
for x in range(int(math.pow(2,int(variables)))):
    #get the next combination of bools
    boolAssignments.next_assigment(boolAssignments.boolComb, int(variables), x)
    #currently has no purpose, ask about sets
    initialization(sigma)
    #get the value of the formula for this step
    satLine=satisfactionProbability(sigma,variables,1)
    #count all the satisfying assignments of the formula
    if satLine:
        satComb += 1
satProb= satComb/(math.pow(2,int(variables)))
p=1
if satProb < p:
    print("Not Satisfiable")
else:
    print("Satisfiable")

