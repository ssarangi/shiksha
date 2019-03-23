import random
from log import logger

from models.arithmetic import SimpleArithmeticProblem


def main():
    logger.info("Initializing the Shiksha Engine....")
    for i in range(1, 10):
        complexity = random.randint(1, 4)
        problem = SimpleArithmeticProblem(complexity)
        logger.info('Complexity: %s --> %s', complexity, problem.generate())


if __name__ == '__main__':
    main()
