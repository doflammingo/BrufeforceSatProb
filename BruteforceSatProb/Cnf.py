class Cnf:
    """
    A class used to represent a formula
    """
    def __init__(self, formula):
        """

        :param formula:
            The formula
        """
        self.formula = formula
        #eval funktion implementieren

    def eval(self,currentAssignment):
        """Evaluates the formula with the current Assignments of variables

        Parameters
        ----------
        :param currentAssignment: int Array
            the currentAssignment of for the x_n values of the formula
        :return: boolean
            Boolean if it
        """
        formulaResult =[]
        clauseResult = False

        for x in self.formula:
            for y in x:
                if y == '0':
                    break
                else:
                    #Case if assignemnt is false and variable is positive
                    if currentAssignment[abs(int(y))-1] == 0 and int(y) > 0:
                        clauseResult = clauseResult or False
                    #Case if assignemnt is false and variable is negative
                    elif currentAssignment[abs(int(y))-1] == 0 and int(y) < 0:
                        clauseResult = clauseResult or not False
                    #Case if assignemnt is true and variable is positive
                    elif currentAssignment[abs(int(y))-1] == 1 and int(y) > 0:
                        clauseResult = clauseResult or True
                    #Case if assignemnt is true and variable is negative
                    elif currentAssignment[abs(int(y))-1] == 1 and int(y) < 0:
                        clauseResult = clauseResult or not True
                    #Case if nothing of that applies
                    else:
                        clauseResult = clauseResult or None

            formulaResult.append(clauseResult)
        #And all results from the clauses
        for num,x in enumerate(formulaResult):
            if num == 0:
                endResult = x
            else:
                endResult = endResult and x
        return endResult

    def nextAssignment(self,currentAssignment):
        """Assigns the next Assignment for the variables

        Parameters
        ----------
        :param currentAssignment: list
            The current assignment of the variables
        :return: currentAssignment
            returns the current Assignment
        """
        for num,x in enumerate(currentAssignment):
            if x == 0:
                currentAssignment[num] = 1
                return currentAssignment
            elif x==1:
                currentAssignment[num] = 0
                continue
            else:
                continue


