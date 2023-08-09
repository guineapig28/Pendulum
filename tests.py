import unittest
from bayes_pendulum.tuesdaytask  import period_time

class TestMethods(unittest.TestCase):

    def test_period_time(self):
        """Tests the implementation of period_time"""
        # Generate example input from ODE solver
        sol = [-1, 1, -1, 1]
        sol_time = [0, 1, 2, 3]
        period = period_time(sol, sol_time)
        self.assertAlmostEqual(period, 2)
