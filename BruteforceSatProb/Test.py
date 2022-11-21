import unittest
from BruteforceSatProb import BruteforceSatPro
from BruteforceSatProb.Cnf import Cnf

class MyTestCase(unittest.TestCase):
    """
    A class to test the the functions
    """
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_initialization(self):
        self.assertEqual(True, True)  # add assertion here

    def test_nextAssignment(self):
        x = Cnf(BruteforceSatPro.phi)
        currentAssignment = [1,2,0]
        x.nextAssignment(currentAssignment)
        print(currentAssignment)
        self.assertEqual(currentAssignment, [0,2,1])
        x.nextAssignment(currentAssignment)
        self.assertEqual(currentAssignment, [1,2,1])


if __name__ == '__main__':
    unittest.main()
