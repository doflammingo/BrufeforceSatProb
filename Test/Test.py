import unittest
from Module.Cnf import Cnf
from Module.Assignment import Assignment
from IO.CnfParser import CnfParser
from Utils.Exponent import Exponent
from Module.Clause import Clause

class MyTestCase(unittest.TestCase):
    """
    A class to test the the functions
    """

    def test_nextAssignment(self):
        """
        We test the assignments of the variables if the correct boolean is assigned to it
        :return: list
            Returns the new assignment
        """
        x = Assignment(3)
        self.assertEqual([0,0,0], x.currentAssignment)
        x.nextAssignment()
        self.assertEqual([1,0,0], x.currentAssignment)
        x.nextAssignment()
        self.assertEqual([0,1,0],x.currentAssignment)
        x.nextAssignment()
        self.assertEqual([1,1,0],x.currentAssignment)
        x.nextAssignment()
        self.assertEqual([0,0,1],x.currentAssignment)
        x.nextAssignment()
        self.assertEqual([1,0,1],x.currentAssignment)
        x.nextAssignment()
        self.assertEqual([0,1,1],x.currentAssignment)
        x.nextAssignment()
        self.assertEqual([1,1,1],x.currentAssignment)
        x.nextAssignment()
        self.assertEqual([0,0,0],x.currentAssignment)


    def test_eval(self):
        """
        We test the eval function if the right booleans return, when putting the current assignment and formula in.
        :return: boolean
            Returns the boolean value of the formula depending on the assignment of the variables
        """
        data2 = '..\\IO\\simple_v3_c2.cnf'
        reader=CnfParser().ReadInputData(data2)
        self.assertEqual(True,reader.eval([0,0,0]))
        self.assertEqual(False,reader.eval([1,0,0]))
        self.assertEqual(True,reader.eval([0,1,0]))
        self.assertEqual(True,reader.eval([1,1,0]))
        self.assertEqual(False,reader.eval([0,0,1]))
        self.assertEqual(True,reader.eval([1,0,1]))
        self.assertEqual(False,reader.eval([0,1,1]))
        self.assertEqual(True,reader.eval([1,1,1]))

    def test_exponent(self):
        """
        We test the exponent function it returns the right result calculating with exponents
        :return: int
            Returns the result of the given numbers exponent and basis
        """
        calcExpo = Exponent()
        self.assertEqual(4,calcExpo.exponent(2,2))
        self.assertEqual(8,calcExpo.exponent(2,3))
        self.assertEqual(32,calcExpo.exponent(2,5))
        self.assertEqual(1024,calcExpo.exponent(4,5))
        self.assertEqual(625,calcExpo.exponent(25,2))

    def test_addLiteral(self):
        """
        We test the function, if the literals get added to the clause and no duplicates exists
        :return:
        """
        exampleClause = Clause([1,2,3])
        exampleClause.addLiteral(4)
        self.assertEqual([1,2,3,4],exampleClause.literals)
        exampleClause.addLiteral(3)
        self.assertEqual([1,2,3,4],exampleClause.literals)

    def test_addClause(self):
        """

        :return:
        """
        clause1= Clause([1,2,4])
        clause2= Clause([3,2,4])
        formula = Cnf()
        formula.addClause(clause1)
        formula.addClause(clause2)
        self.assertEqual([clause1,clause2],formula.clauses)
if __name__ == '__main__':
    unittest.main()
