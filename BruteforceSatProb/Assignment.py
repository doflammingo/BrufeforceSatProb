
class Assignment:
    """
    A class used to represent the assignments of the formula
    """
    boolComb = []
    # Intialize the first assignement of booleans to false
    def __init__(self,length):
        for x in range(length):
            self.boolComb.append(False)
    #int array, 0 = false, 1= true und 2 undefined, und dann einfach höher zählen
    #Next assignemnts for booleans
    def next_assigment(self,newVarBool,g,step):
        k=str(format(step, '0'+str(g)+'b'))
        #if the the current index of the binary number is 0 it equals false and etc.
        for x in reversed(range(len(k))):
            if k[x] == '0':
                newVarBool[len(k)-1-x] = False
            else:
                newVarBool[len(k)-1-x] = True
        return newVarBool




