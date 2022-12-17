import math


def odds(number_of_balls, pool_of_balls, number_of_tickets):
    """
    Calculate the odds of winning the lottery.
    >>> odds(6, 49, 5)
    '1 in 13,983,816'
    """
    return f"1 in {pool_of_balls ** number_of_balls // math.factorial(number_of_balls) ** number_of_tickets}"
