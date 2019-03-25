import random
from log import logger

from models.arithmetic import SimpleArithmeticProblem

from expr import generator


def engine_initialize():
    logger.info("Initializing the Shiksha Engine....")
    for i in range(1, 10):
        complexity = random.randint(1, 4)
        problem = SimpleArithmeticProblem(complexity)
        logger.info('Complexity: %s --> %s', complexity, problem.generate())


def main():
    expr = generator.generate_single_symbol_expr()
    print(expr)


if __name__ == "__main__":
    main()
