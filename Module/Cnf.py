class Cnf:
    """
    A class used to represent a formula
    """

    def __init__(self):
        self.clauses =[]

    def addClause(self,clause):
        """Adds a clause to the formula
        Parameters
        ----------
        :param clause: Clause
            A clause instance from the class Clause
        :return: formula
            returns the formula with the added clause
        """
        self.clauses.append(clause)

    def eval(self, assignment):
        """Evaluates the formula with the current Assignments of variables
        It evaluates each clause with the current assigned Assignments and saves the temporary result
        before evaluating all results from each clause together
        Parameters
        ----------
        :param assignment: int Array
            the currentAssignment of for the x_n values of the formula
        :return: boolean
            Boolean if it
        """
        formulaResult = []

        clauseResult = False
        #Go through all clauses in the formula
        for clause in self.clauses:
            #Go through all literals in the clause
            for literal in clause.literals:
                # Case if assignment is false and variable is negative
                if assignment[abs(literal)-1] == 0 and literal < 0:
                    clauseResult = True
                    break
                # Case if assignment is true and variable is positive
                elif assignment[abs(literal)-1] == 1 and literal > 0:
                    clauseResult = True
                    break
                # Case if nothing of that applies
                else:
                    continue
            formulaResult.append(clauseResult)
            clauseResult = False
        # And all results from the clauses
        for num, x in enumerate(formulaResult):
            if x:
                continue
            else:
                return x
        return True
