from abc import ABC

class Qubo(ABC):
    def solve(self, sampler, **kwargs):
        """Solves the qubo using the passed in sampler
        """
        self.solution_set = sampler(self.qubo, **kwargs)
