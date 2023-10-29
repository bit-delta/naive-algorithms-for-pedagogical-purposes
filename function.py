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

    # Simplest form of derivative. Single-variable linear equation with no chain rule or special cases (e.g. e^x)
    def derivative(self):
        if len(self.coefficients) != len(self.exponents):
            raise Exception("coefficients: list, exponents: list must be the same length.")
        new_coefficients = []
        new_exponents = []
        for i in range(len(self.coefficients)):
            new_coefficients.append(self.exponents[i] * self.coefficients[i])
            new_exponents.append(self.exponents[i] - 1)
        return [new_coefficients, new_exponents]


my_func = Function([1, 2, 3], [4, 5, 6])
my_func_derivative = my_func.derivative()

print(my_func.coefficients,my_func.exponents)
print(my_func_derivative)
