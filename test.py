import unittest
import function


class TestStringMethods(unittest.TestCase):

    def test_function_constructor(self):
        self.assertEqual(str(function.Function([1], [1], 'x')), '1*(x)^1')
        self.assertEqual(str(function.Function([1], [2], 'x')), '1*(x)^2')
        self.assertEqual(str(function.Function([1], [1], 'x+1')), '1*(x+1)^1')
        self.assertEqual(str(function.Function([1], [2], 'x+1')), '1*(x+1)^2')

    def test_derivative(self):
        self.assertEqual(str(function.Function([1], [1], 'x').derivative), '1*(x)^0')
        self.assertEqual(str(function.Function([1], [2], 'x').derivative), '2*(x)^1')
        self.assertEqual(str(function.Function([1], [1], 'x+1').derivative), '1*(x+1)^0')
        self.assertEqual(str(function.Function([1], [2], 'x+1').derivative), '2*(x+1)^1')


if __name__ == '__main__':
    unittest.main()
