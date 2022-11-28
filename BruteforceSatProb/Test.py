import unittest
from BruteforceSatProb import BruteforceSatPro
from BruteforceSatProb.Cnf import Cnf
from BruteforceSatProb.Assignment import Assignment
from BruteforceSatProb.ReadIn import ReadIn
from BruteforceSatProb.Exponent import Exponent
from BruteforceSatProb.Clause import Clause

class MyTestCase(unittest.TestCase):
    """
    A class to test the the functions
    """

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_initialization(self):
        """
        We test the initialization of the assignments for the variables of the formula
        :return: list
            Returns the assignment list with 0 if variable is initialized
        """
        data2 = 'simple_v3_c2.cnf'
        data3 = 'quinn.cnf'
        reader=ReadIn()
        phi = reader.ReadInputData(data2)
        BruteforceSatPro.initialization(phi)
        self.assertEqual([0,0,0],BruteforceSatPro.currentAssignment)
        phi = reader.ReadInputData(data3)
        BruteforceSatPro.initialization(phi)
        self.assertEqual([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2],BruteforceSatPro.currentAssignment)

    def test_nextAssignment(self):
        """
        We test the assignments of the variables if the correct boolean is assigned to it
        :return: list
            Returns the new assignment
        """
        x = Assignment()
        currentAssignment = [1,2,0]
        x.nextAssignment(currentAssignment)
        self.assertEqual([0,2,1],currentAssignment )
        x.nextAssignment(currentAssignment)
        self.assertEqual([1,2,1],currentAssignment)
        x.nextAssignment(currentAssignment)
        self.assertEqual([0,2,0],currentAssignment)


    def test_eval(self):
        """
        We test the eval function if the right booleans return, when putting the current assignment and formula in.
        :return: boolean
            Returns the boolean value of the formula depending on the assignment of the variables
        """
        data2 = 'simple_v3_c2.cnf'
        reader=ReadIn()
        phi = reader.ReadInputData(data2)
        cnf = Cnf(phi)
        self.assertEqual(True,cnf.eval([0,0,0]))
        self.assertEqual(False,cnf.eval([0,0,1]))
        self.assertEqual(True,cnf.eval([0,1,0]))
        self.assertEqual(False,cnf.eval([0,1,1]))
        self.assertEqual(True,cnf.eval([1,0,0]))
        self.assertEqual(True,cnf.eval([1,0,1]))
        self.assertEqual(True,cnf.eval([1,1,0]))
        self.assertEqual(True,cnf.eval([1,1,1]))

    def test_exponent(self):
        """
        We test the exponent function it returns the right exponents of numbers
        :return: int
            Returns the result of the given numbers for exponent and basis
        """
        calcExpo = Exponent()
        self.assertEqual(4,calcExpo.exponent(2,2))
        self.assertEqual(8,calcExpo.exponent(2,3))
        self.assertEqual(32,calcExpo.exponent(2,5))
        self.assertEqual(1024,calcExpo.exponent(4,5))
        self.assertEqual(625,calcExpo.exponent(25,2))

    def test_addLiteral(self):
        """
        We test the function, if the literals get added and no duplicates exists
        :return:
        """
        exampleClause = ['a','b','c']
        clause = Clause(exampleClause)
        self.assertEqual(['a','b','c','d'],clause.addLiteral(exampleClause,'d'))
        self.assertEqual(['a','b','c','d'],clause.addLiteral(exampleClause,'a'))

if __name__ == '__main__':
    unittest.main()
