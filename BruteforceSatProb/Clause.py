class Clause:
    """
    A class used to represent a clause of the formula
    """

    def __init__(self, clause):
        """
        Parameters
        ----------
        :param clause: list
            The clause of a formula

        """
        self.clause = clause


    def addLiteral(self,clause,literal):
        """Adds literals to a clause

        Parameters
        ----------
        :param clause: list
            The clause of a formula
        :param literal: char
            The variable in a clause
        :return: clause
            returns the clause with the literal
        """
        clause.append(literal)
        return clause
    # addliteral funktion, etc.