import unittest
import function


class TestFunctionClass(unittest.TestCase):

    def test_function_constructor(self):
        # Construct a Function f(x) = x
        self.assertEqual(str(function.Function([1], [1], 'x')), '1*(x)^1')
        self.assertEqual(function.Function([1], [1], 'x').coefficients, [1])
        self.assertEqual(function.Function([1], [1], 'x').exponents, [1])
        self.assertEqual(function.Function([1], [1], 'x').variable, 'x')

        # Construct a Function f(x) = x^2
        self.assertEqual(str(function.Function([1], [2], 'x')), '1*(x)^2')
        self.assertEqual(function.Function([1], [2], 'x').coefficients, [1])
        self.assertEqual(function.Function([1], [2], 'x').exponents, [2])
        self.assertEqual(function.Function([1], [2], 'x').variable, 'x')

        # Construct a Function f(x) = x+1
        self.assertEqual(str(function.Function([1], [1], 'x+1')), '1*(x+1)^1')
        self.assertEqual(function.Function([1], [1], 'x+1').coefficients, [1])
        self.assertEqual(function.Function([1], [1], 'x+1').exponents, [1])
        self.assertEqual(function.Function([1], [1], 'x+1').variable, 'x+1')

        # Construct a Function f(x) = (x+1)^2
        self.assertEqual(str(function.Function([1], [2], 'x+1')), '1*(x+1)^2')
        self.assertEqual(function.Function([1], [2], 'x+1').coefficients, [1])
        self.assertEqual(function.Function([1], [2], 'x+1').exponents, [2])
        self.assertEqual(function.Function([1], [2], 'x+1').variable, 'x+1')

    def test_derivative(self):
        self.assertEqual(str(function.Function([1], [1], 'x').derivative), '1*(x)^0')
        self.assertEqual(str(function.Function([1], [2], 'x').derivative), '2*(x)^1')
        self.assertEqual(str(function.Function([1], [1], 'x+1').derivative), '1*(x+1)^0')
        self.assertEqual(str(function.Function([1], [2], 'x+1').derivative), '2*(x+1)^1')


if __name__ == '__main__':
    unittest.main()
