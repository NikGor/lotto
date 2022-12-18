import random


def generate_draw_balls(number_of_balls, pool_of_balls):
    return sorted(random.sample(range(1, pool_of_balls + 1), number_of_balls))


def generate_tickets(number_of_balls, pool_of_balls, number_of_tickets):
    return [sorted(random.sample(range(1, pool_of_balls + 1), number_of_balls)) for _ in range(number_of_tickets)]
