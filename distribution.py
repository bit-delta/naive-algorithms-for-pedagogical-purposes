from functools import reduce


class Distribution:
    def __init__(self, probs: list) -> None:
        if len(probs) > 0 and isinstance(probs, list) and all([type(p) in (int, float) for p in probs]):
            self.discrete_probabilities = probs
        else:
            raise TypeError("Distribution.probs must be a non-empty list of int or float values.")
        self.mean = self.mean()

    def mean(self):
        return reduce(lambda a, b: a + b, self.discrete_probabilities) / len(self.discrete_probabilities)


if __name__ == '__main__':
    dis = Distribution([1, 2, 3])
    print(dis.mean)
    dis = Distribution([1.0, 2.0, 3.0])
    print(dis.mean)
    dis = Distribution([1.0, -1, 3])
    print(dis.mean)
