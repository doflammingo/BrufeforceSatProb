import itertools
import math

sigma =[]
clauses = 0
variables = 0
data1='aim-50-1_6-yes1-4.cnf'
data2='simple_v3_c2.cnf'
data3='quinn.cnf'
xdict ={}
by={}
l=[False, True]
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
def initialization(formula,varBool):
    for x in formula:
        for y in x:
            if y =='0':
                break
            elif int(y) < 0:
                xdict[y] = not varBool[abs(int(y))]
            else:
                xdict[y] = varBool[int(y)]

#calculation of the cnf equations
def satisfactionProbability(formula, k, p):
    endResult=False
    end=[]
    for x in range(int(clauses)):
        for y in range(int(k)):
            if formula[x][y]=='0':
                break
            else:
                endResult = endResult or xdict[formula[x][y]]
        end.append(endResult)
    for num,x in enumerate(end):
        endResult = endResult and end[num]
    return endResult



print(sigma)

boolComb=[list(i) for i in itertools.product(l, repeat=int(variables))]
for x in boolComb:
    for num,y in enumerate(x):
        by[num+1]=y
    initialization(sigma,by)
    satLine=satisfactionProbability(sigma,variables,1)
    print(satLine)
    if satLine:
        satComb += 1
satProb= satComb/(math.pow(2,int(variables)))
print(satProb)

