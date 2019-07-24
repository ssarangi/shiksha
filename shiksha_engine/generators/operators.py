import sympy
from enum import Enum

OPERATORS = [
    '+',
    '-',
    '*',
    '/'
]

SIMPLE_TRIG_OPERATORS = [
    sympy.cos,
    sympy.sin,
    sympy.tan
]

COMPLEX_TRIG_OPERATORS = [
    sympy.cosh,
    sympy.acosh,
    sympy.sinh,
    sympy.asinh,
    sympy.tanh,
    sympy.atanh,
    sympy.atan2,
    sympy.cot,
    sympy.coth,
]

class Operations(Enum):
    # Assume x is the symbol being manipulated.
    ADD_CONSTANT = 1         # x + 2
    SUBTRACT_CONSTANT = 2    # x - 2
    MULTIPLY_CONSTANT = 3    # x * 2
    DIVIDE_CONSTANT = 4      # x / 2
    RAISE_TO_THE_POWER = 5   # x ^ 2
    TAKE_LOG = 6             # log(x)
    ADD_EXPR = 7             # x + x^2
    SUBTRACT_EXPR = 8        # x - x^2
    MULTIPLY_EXPR = 9        # x * x^2
    DIVIDE_EXPR = 10         # x / x^2
    INVERT_EXPR = 11         # 1 / x
    COS = 12         # cos(x)
    SIN = 13         # sin(x)
    TAN = 14         # tan(x)
    COSH = 15        # cosh(x)
    ACOSH = 16       # acosh(x)
    SINH = 17        # sinh(x)
    ASINH = 18       # asinh(x)
    TANH = 19        # tanh(x)
    ATANH = 20       # atanh(x)
    ATAN2 = 21       # atan2(x)
    COT = 22         # cot(x)
    COTH = 23        # acoth(x)

