class Variable:
    def __init__(self, name, lower_bound, upper_bound, lower_exclusive=False, upper_exclusive=False) -> None:
        super().__init__()
        self.name = name

        self.lower_bound = lower_bound + 1 if lower_exclusive else lower_bound
        self.upper_bound = upper_bound + 1 if upper_exclusive else upper_bound

    def get_nominal_value(self):
        return round(((self.upper_bound - self.lower_bound) / 2) + self.lower_bound)

    def get_nbv_values(self):
        return [self.lower_bound, self.lower_bound + 1, self.get_nominal_value(), self.upper_bound - 1,
                self.upper_bound]

    def get_robust_values(self):
        return [self.lower_bound - 1, self.lower_bound, self.lower_bound + 1, self.get_nominal_value(),
                self.upper_bound - 1, self.upper_bound, self.upper_bound + 1]
