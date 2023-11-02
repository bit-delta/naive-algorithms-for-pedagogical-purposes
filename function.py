class Function:
    def __init__(self, coefficients: list, exponents: list, variable='x') -> None:
        if isinstance(coefficients, list):
            self.coefficients = coefficients
        else:
            raise TypeError("Function.coefficients must be a list.")
        if isinstance(exponents, list):
            self.exponents = exponents
        else:
            raise TypeError("Function.exponents must be a list.")
        self.variable = variable
        self._derivative = None

    def __str__(self):
        return ' + '.join([f'{c}*({self.variable})^{e}' for c, e in zip(self.coefficients, self.exponents)])
        # return 'f(x) = ' + ' + '.join([f'{c}{self.variable}^{e}' for c, e in zip(self.coefficients, self.exponents)])

    # Simplest form of derivative. Single-variable linear equation with no chain rule or special cases (e.g. e^x)
    @property
    def derivative(self):
        if self._derivative is None:
            if len(self.coefficients) != len(self.exponents):
                raise Exception("coefficients: list, exponents: list must be the same length.")
            new_coefficients = []
            new_exponents = []
            for i in range(len(self.coefficients)):
                new_coefficients.append(self.exponents[i] * self.coefficients[i])
                new_exponents.append(self.exponents[i] - 1)
            self._derivative = Function(new_coefficients, new_exponents, self.variable)
        return self._derivative


# Computes the first n terms of the Taylor series of a Function f centered at a
def taylor(f: Function, n, a) -> Function:
    num = 0
    coefficients = []
    exponents = []
    f_at_a = Function(f.coefficients, f.exponents, f.variable.replace('x', str(a)))
    while num < n:
        if num == 0:
            coefficients.append(f_at_a)
        else:
            coefficients.append(f_at_a.derivative)
            f_at_a = f_at_a.derivative
        exponents.append(num)
        num += 1
    coefficients = [f'(({x})/{n}!)' for x, n in zip(coefficients, range(n))]
    return Function(coefficients, exponents, f'x-{a}')


if __name__ == '__main__':
    # Initialize a Function with coefficients and exponents
    my_func = Function([10, 12, 2, 0, 1, 4], [0, 1, 2, 3, 4, 5])
    print(my_func.coefficients, my_func.exponents)
    print(f'my_func: {my_func}')

    # Accessing the derivative attribute causes a derivative to be generated
    print("my_func.derivative " + str(my_func.derivative))
    print("vars(my_func): " + str(vars(my_func)))

    # If the derivative attribute has not been accessed, it is still None
    print("vars(my_func.derivative) " + str(vars(my_func.derivative)))

    # Taylor series centered at a = 1 for x^2
    my_simple_func = Function([1], [2])
    my_taylor = taylor(my_simple_func, 4, 1)
    print(f'my_simple_func: {my_simple_func}')
    print(f'my_taylor: {my_taylor}')
    print('my_taylor.coefficients: ', *[str(f) + ', ' for f in my_taylor.coefficients])

    # Composition of functions
    my_composed = Function([1, 10], [2, 3], my_func)
    print(f'my_composed: {my_composed}')
    print(f'vars(my_composed): {vars(my_composed)}')

