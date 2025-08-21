# test_module.py
import unittest
import mean_var_std as mv

class TestMeanVarianceStd(unittest.TestCase):
    def test_example_0_to_8(self):
        expected = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0],
                         [0.6666666666666666, 0.6666666666666666, 0.6666666666666666],
                         6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178],
                                   [0.816496580927726, 0.816496580927726, 0.816496580927726],
                                   2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        self.assertEqual(mv.calculate([0,1,2,3,4,5,6,7,8]), expected)

    def test_raises_with_less_than_9_numbers(self):
        with self.assertRaises(ValueError):
            mv.calculate([1,2,3,4,5,6,7,8])  # só 8 números

    def test_types(self):
        result = mv.calculate([0,1,2,3,4,5,6,7,8])
        # verificar que todas as listas são Python lists
        for key in ['mean','variance','standard deviation','max','min','sum']:
            self.assertIsInstance(result[key][0], list)
            self.assertIsInstance(result[key][1], list)
        # verificar que flattened é float ou int
        self.assertIsInstance(result['mean'][2], float)
        self.assertIsInstance(result['max'][2], int)

if __name__ == "__main__":
    unittest.main()
