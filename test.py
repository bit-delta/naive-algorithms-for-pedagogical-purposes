import unittest
import function


class TestFunctionClass(unittest.TestCase):

    def test_function_constructor(self):
        # Construct a Function f(x) = x
        f = function.Function([1], [1], 'x')
        self.assertEqual(str(f), '1*(x)**1')
        self.assertEqual(f.coefficients, [1])
        self.assertEqual(f.exponents, [1])
        self.assertEqual(f.variable, 'x')

        # Construct a Function f(x) = x**2
        f = function.Function([1], [2], 'x')
        self.assertEqual(str(f), '1*(x)**2')
        self.assertEqual(f.coefficients, [1])
        self.assertEqual(f.exponents, [2])
        self.assertEqual(f.variable, 'x')

        # Construct a Function f(x) = x+1
        f = function.Function([1], [1], 'x+1')
        self.assertEqual(str(f), '1*(x+1)**1')
        self.assertEqual(f.coefficients, [1])
        self.assertEqual(f.exponents, [1])
        self.assertEqual(f.variable, 'x+1')

        # Construct a Function f(x) = (x+1)**2
        f = function.Function([1], [2], 'x+1')
        self.assertEqual(str(f), '1*(x+1)**2')
        self.assertEqual(f.coefficients, [1])
        self.assertEqual(f.exponents, [2])
        self.assertEqual(f.variable, 'x+1')

    def test_derivative(self):
        # Derivative of f(x) = x
        df_dx = function.Function([1], [1], 'x').derivative
        self.assertEqual(str(df_dx), '1*(x)**0')
        self.assertEqual(df_dx.coefficients, [1])
        self.assertEqual(df_dx.exponents, [0])
        self.assertEqual(df_dx.variable, 'x')

        # Derivative of f(x) = x**2
        df_dx = function.Function([1], [2], 'x').derivative
        self.assertEqual(str(df_dx), '2*(x)**1')
        self.assertEqual(df_dx.coefficients, [2])
        self.assertEqual(df_dx.exponents, [1])
        self.assertEqual(df_dx.variable, 'x')

        # Derivative of f(x) = x+1
        df_dx = function.Function([1], [1], 'x+1').derivative
        self.assertEqual(str(df_dx), '1*(x+1)**0')
        self.assertEqual(df_dx.coefficients, [1])
        self.assertEqual(df_dx.exponents, [0])
        self.assertEqual(df_dx.variable, 'x+1')

        # Derivative of f(x) = (x+1)**2
        df_dx = function.Function([1], [2], 'x+1').derivative
        self.assertEqual(str(df_dx), '2*(x+1)**1')
        self.assertEqual(df_dx.coefficients, [2])
        self.assertEqual(df_dx.exponents, [1])
        self.assertEqual(df_dx.variable, 'x+1')


if __name__ == '__main__':
    unittest.main()
