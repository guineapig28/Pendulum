import unittest
from bayes_pendulum.tuesdaytask  import locate_root

class TestMethods(unittest.TestCase):

    def test_locate_root(self):
        """Tests the implementation of locate_root"""
        # Generate example input from ODE solver
        sol = [-1, 0, 1]
        sol_time = [0, 1, 2]
        index = 0
        indexes =[1, 1, 1] 
        root = locate_root(index, sol_time, sol, indexes)
        self.assertAlmostEqual(root, 1)
