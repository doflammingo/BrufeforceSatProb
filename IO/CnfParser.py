from Module.Clause import Clause
from Module.Cnf import Cnf

class CnfParser:
    """
    A class used to read in the Cnf files
    """
    # Number of variables in the formula
    variables = 0
    # Number of clauses in the formula
    clauses = 0

    def ReadInputData(self, data):
        """Reads in the input data of a file

        :param data:
            The file name to be read in
        :return: formula
            returns the a instance from formula containing all the clauses
        """

        global variables
        global clauses

        #create instance of formula
        phi=Cnf()

        with open(data) as file:
            for line in file:
                # ignore comment lines
                if line[0] == 'c':
                    continue
                else:
                    # Gather all the information about the formula
                    if 'p' in line:
                        formulaInfo = line.split()
                        formulaInfo.remove('p')
                        formulaInfo.remove('cnf')
                        variables = int(formulaInfo[0])
                        clauses = int(formulaInfo[1])
                    else:
                        phi.addClause(Clause(line.split()))
        return phi


    def getVariables(self):
        """The getter for the variables

        :return: int
            returns the number of variables in the formula
        """
        return variables


    def getClauses(self):
        """The getter for number of clauses

        :return: int
            returns the number of clauses in the formula
        """
        return clauses
