class Function:
    def __init__(self, coefficients: list, exponents: list) -> None:
        if isinstance(coefficients, list):
            self.coefficients = coefficients
        else:
            raise TypeError("Function.coefficients must be a list.")
        if isinstance(exponents, list):
            self.exponents = exponents
        else:
            raise TypeError("Function.exponents must be a list.")
        self._derivative = None

    def __str__(self):
        return 'f(x) = ' + ' + '.join([str(c) + "x^" + str(e) for c, e in zip(self.coefficients, self.exponents)])

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
            self._derivative = Function(new_coefficients, new_exponents)
        return self._derivative


my_func = Function([10, 12, 2, 0, 1, 4], [0, 1, 2, 3, 4, 5])
print(my_func.coefficients, my_func.exponents)
print("my_func: " + str(my_func))

# Accessing the derivative attribute causes a derivative to be generated
print("my_func.derivative " + str(my_func.derivative))
print("vars(my_func): " + str(vars(my_func)))

# If the derivative attribute has not been accessed, it is still None
print("vars(my_func.derivative) " + str(vars(my_func.derivative)))


# TODO: Taylor Series function like taylor(function, n) returns nth degree Taylor series