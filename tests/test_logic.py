import unittest
from src.logic.arithmetization import arithmetize_formula
from src.logic.fixed_point import compute_fixed_point

class TestResonanceLogic(unittest.TestCase):
    def test_arithmetization(self):
        formula = "EXISTS x (P(x) AND Q(x))"
        result = arithmetize_formula(formula)
        self.assertIsNotNone(result)

    def test_fixed_point(self):
        def sample_operator(x):
            return x
        fp = compute_fixed_point(sample_operator)
        self.assertIsNotNone(fp)

if __name__ == '__main__':
    unittest.main()
