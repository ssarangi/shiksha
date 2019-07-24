"""
generator.py: This is the main file which should be used by other api's to generate
various math expressions. Other files in this directory are not meant to be exported.
"""

from abc import ABC
import numpy as np
import sympy
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
        self._constant_generator = ConstantGenerator(0, 10)

    def _method_name_from_operation(self, operation: operators.Operations):
        method_name = "_" + operation.name.lower()
        print(OperationsGenerator.__dict__.keys())
        if method_name not in OperationsGenerator.__dict__.keys():
            raise Exception("Method %s not implemented" % method_name)
        return method_name

    def generate(self):
        operation = np.random.choice(operators.Operations)
        method_name = self._method_name_from_operation(operation)
        method_to_call = getattr(self, method_name)
        return method_to_call()

    def _add_constant(self):
        constant = self._constant_generator.generate()
        return self._symbol + constant
    
    def _subtract_constant(self):
        constant = self._constant_generator.generate()
        return self._symbol - constant

    def _multiply_constant(self):
        constant = self._constant_generator.generate()
        return self._symbol * constant

    def _divide_constant(self):
        constant = self._constant_generator.generate()
        return self._symbol / constant

    def _raise_to_the_power(self):
        constant = self._constant_generator.generate()
        return self._symbol ** constant

    def _take_log(self):
        return sympy.log(self._symbol)

    def _add_expr(self, expr):
        return self._symbol + expr

    def _subtract_expr(self, expr):
        return self._symbol - expr

    def _multiply_expr(self, expr):
        return self._symbol * expr

    def _divide_expr(self, expr):
        return self._symbol / expr

    def _invert(self):
        return 1 / self._symbol

    def _cos(self):
        return sympy.cos(self._symbol)

    def _sin(self):
        return sympy.sin(self._symbol)

    def _tan(self):
        return sympy.tan(self._symbol)

    def _cosh(self):
        return sympy.cosh(self._symbol)

    def _acosh(self):
        return sympy.acosh(self._symbol)

    def _sinh(self):
        return sympy.sinh(self._symbol)

    def _asinh(self):
        return sympy.asinh(self._symbol)

    def _tanh(self):
        return sympy.tanh(self._symbol)

    def _atanh(self):
        return sympy.atanh(self._symbol)

    def _atan2(self):
        return sympy.atan2(self._symbol)

    def _cot(self):
        return sympy.cot(self._symbol)

    def _coth(self):
        return sympy.coth(self._symbol)

    