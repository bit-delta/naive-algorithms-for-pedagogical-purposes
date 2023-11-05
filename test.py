import distribution
import function
import unittest


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

    def test_taylor(self):
        # 3rd degree Taylor polynomial of f(x) = x**2, at a = 1
        taylor = function.taylor(function.Function([1], [2], 'x'), 4, 1)
        self.assertTrue(isinstance(taylor, function.Function))
        self.assertEqual(str(taylor), '((1)/0!)*(x-1)**0 + ((2)/1!)*(x-1)**1 + ((2)/2!)*(x-1)**2 + ((0.0)/3!)*(x-1)**3')
        self.assertEqual(taylor.coefficients, ['((1)/0!)', '((2)/1!)', '((2)/2!)', '((0.0)/3!)'])
        self.assertEqual(taylor.exponents, [*range(4)])
        self.assertEqual(taylor.variable, 'x-1')


class TestDistributionClass(unittest.TestCase):

    def test_distribution_constructor(self):
        with self.assertRaises(TypeError):
            distribution.Distribution(3)
        with self.assertRaises(TypeError):
            distribution.Distribution('l')
        with self.assertRaises(TypeError):
            distribution.Distribution(3.0)
        with self.assertRaises(TypeError):
            distribution.Distribution(True)
        with self.assertRaises(TypeError):
            distribution.Distribution([True])
        with self.assertRaises(TypeError):
            distribution.Distribution(['string', 3])
        with self.assertRaises(TypeError):
            distribution.Distribution([])

    def test_mean(self):
        mean = distribution.Distribution([1, 2, 3]).mean
        self.assertEqual(mean, 2.0)
        mean = distribution.Distribution([1.0, 2.0, 3.0]).mean
        self.assertEqual(mean, 2.0)
        mean = distribution.Distribution([1.0, -1, 3]).mean
        self.assertEqual(mean, 1.0)


if __name__ == '__main__':
    unittest.main()
