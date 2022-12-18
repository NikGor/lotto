from src.generators import generate_tickets, generate_draw_balls


def game(number_of_balls, pool_of_balls, number_of_tickets):
    # generate tickets
    tickets = generate_tickets(number_of_balls, pool_of_balls, number_of_tickets)
    # simulate draws
    draw = generate_draw_balls(number_of_balls, pool_of_balls)
    return draw, tickets
