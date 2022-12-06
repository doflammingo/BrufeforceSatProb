class Exponent:
    """
    A class used to represent and calculate exponents
    """
    def exponent(self,x,y):
        """ For a number x it takes to the power y
        Parameters
        ----------
        :param x: int
            Basis
        :param y: int
            exponent
        :return: int
            result x power y
        """
        result=x
        for m in range(1,y):
            result=result*x
        return result