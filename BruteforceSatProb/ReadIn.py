class ReadIn:

    variables =0
    clauses = 0

    def ReadInputData(self,data):
        """Reads in the input data of a file

        :param data:
            The file name to be read in
        :return: list
            returns a list of clauses. The list itself can also be considered the formula
        """

        global variables
        global clauses
        phi = []
        with open(data) as f:
            for line in f:
                # ignore comment lines
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
        return phi
        f.close

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
