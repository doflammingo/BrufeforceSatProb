class Exponent:
    """
    A class used to represent and calculate exponents
    """
    def exponent(self,x,y):
        """ For a number x it takes to the power y
        :param x: int
            Basis
        :param y: int
            exponent
        :return: int
            result x power y
        """
        end=x
        for m in range(1,y):
            end=end*x
        return end