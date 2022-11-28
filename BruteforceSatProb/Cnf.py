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

    def eval(self,currentAssignment):
        """Evaluates the formula with the current Assignments of variables
        It evaluates each clause with the current assigned Assignments and saves the temporary result
        before evaluating all results from each clause together
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


