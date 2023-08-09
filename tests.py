import unittest
from bayes_pendulum.tuesdaytask  import period_time, locate_root

class TestMethods(unittest.TestCase):

    def test_period_time(self):
        """Tests the implementation of period_time"""
        # Generate example input from ODE solver
        sol = [-1, 1, -1, 1]
        sol_time = [0, 1, 2, 3]
        period = period_time(sol, sol_time)
        self.assertAlmostEqual(period, 2)

    def test_locate_root(self):
        """Tests the implementation of locate_root"""
        # Generate example input from ODE solver
        sol = [-1, 0, 1]
        sol_time = [0, 1, 2]
        index = 0
        indexes =[1, 1, 1] 
        root = locate_root(index, sol_time, sol, indexes)
        self.assertAlmostEqual(root, 1)
