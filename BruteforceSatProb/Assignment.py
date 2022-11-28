
class Assignment:
    """
    A class used to represent the assignments of the formula
    """

    def nextAssignment(self,currentAssignment):
        """Assigns the next Assignment for the variables
        For each call it counts the assignments up like a binary counter
        The least significant bit from currentAssignment is on the left or at index 0
        After filling currentAssignments with 1's another call of nextAssignments, sets them all to 0
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
            elif x == 1:
                currentAssignment[num] = 0
                continue
            else:
                continue


