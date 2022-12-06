class Clause:
    """
    A class used to represent a clause of the formula
    """

    def __init__(self, literals):
        """
        Parameters
        ----------
        :param literals: list
            A list of literals

        """
        #Literals are made into a list, which is the clause
        self.literals = list(map(int,literals))

        #We remove the end marker of the list of literals
        if 0 in self.literals:
            self.literals.remove(0)

    def addLiteral(self,literal):
        """Adds literals to a clause
        It adds a literal to the given clause, if it contains that literal
        already, it will do nothing
        Parameters
        ----------
        :param literal: char
            The variable in a clause
        :return: literal
            returns the clause with the literal
        """
        if self.literals.count(literal):
            return self
        else:
            self.literals.append(literal)
            return self
