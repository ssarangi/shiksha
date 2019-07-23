"""
generator.py: This is the main file which should be used by other api's to generate
various math expressions. Other files in this directory are not meant to be exported.
"""

from abc import ABC
import numpy as np
# from . import algebra
from . import operators


# def generate_single_symbol_expr():
#     return algebra.generate_single_symbol_multi_power_expr(algebra.x, 2)

class Generator(ABC):
    def generate(self):
        raise NotImplementedError("generate method has not been implemented")

class ConstantGenerator(Generator):
    def __init__(self, constant_range_start, constant_range_end):
        self._constant_range_start = constant_range_start
        self._constant_range_end = constant_range_end

    def generate(self):
        return np.random.randint(self._constant_range_start, self._constant_range_end + 1)

class SingleSymbolTermGenerator(Generator):
    """Class generates a single symbol based term. 
    For example, 2x or log(x) or x^2 or exp(x) etc
    """
    def __init__(self, num_terms_to_generate):
        self._num_terms_to_generate = num_terms_to_generate

    def generate(self):
        pass

class OperationsGenerator(Generator):
    def __init__(self, symbol):
        self._symbol = symbol
    
    def generate(self):
        operation = np.random.choice(operators.Operations)

    def _add_constant(self):
        pass
    
    def _subtract_constant(self):
        pass

    def _multiply_constant(self):
        pass

    def _divide_constant(self):
        pass

    