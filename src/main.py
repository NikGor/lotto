from src.tools import load_tickets, save_tickets, print_and_highlight
from src.generators import generate_tickets, generate_draw_balls
from src.math import odds


def game(number_of_balls, pool_of_balls, number_of_tickets, save, load):
    # generate tickets
    if load:
        tickets = load_tickets(load)
    else:
        tickets = generate_tickets(number_of_balls, pool_of_balls, number_of_tickets)
    # save tickets
    if save:
        save_tickets(tickets, save)
    # simulate draws
    while True:
        draw = generate_draw_balls(number_of_balls, pool_of_balls)
        print("Draw: ", draw)
        print_and_highlight(draw, tickets)
        print('winning odds: ', odds(number_of_balls, pool_of_balls, number_of_tickets))
        input("Press enter to continue or ctrl+c to exit")
        print()
