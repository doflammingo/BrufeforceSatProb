
class Assignment:
    """
    A class used to represent the assignments of the variables in the formula
    """

    #currentAssignment = []
    def __init__(self,varNum):
        """
        Parameters
        ----------
        :param varNum: int
            Number of variables in the formula
        """
        # The current assignment of the variables in the formula
        self.currentAssignment = []
        # Set all to not defined
        for x in range(varNum):
            self.currentAssignment.append(2)
        # If variable is present in the formula, set to false
        for x in range(varNum):
            self.currentAssignment[x - 1] = 0
    def nextAssignment(self):
        """Assigns the next Assignment for the variables
        For each call it counts the assignments up like a binary counter
        The least significant bit from currentAssignment is on the left or at index 0
        After filling currentAssignments with just 1's another call of nextAssignments, sets them all to 0

        :return: currentAssignment
            returns the current Assignment
        """
        for num,x in enumerate(self.currentAssignment):
            if x == 0:
                self.currentAssignment[num] = 1
                return self.currentAssignment
            elif x == 1:
                self.currentAssignment[num] = 0
                continue
            else:
                continue


