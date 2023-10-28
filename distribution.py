from functools import reduce


class Distribution:
    def __init__(self, probs: list) -> None:
        if isinstance(probs, list):
            self.discrete_probabilities = probs
        else:
            raise TypeError("Distribution.probs must be a list.")
        self.mean = self.mean()

    def mean(self):
        return reduce(lambda a, b: a + b, self.discrete_probabilities) / len(self.discrete_probabilities)


dis = Distribution([1.1, 2, 3])
print(dis.mean)

bad_dis = Distribution(3)
