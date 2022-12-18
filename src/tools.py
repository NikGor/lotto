def load_tickets(filename):
    with open(filename, "r") as f:
        return [set(map(int, line.split())) for line in f.readlines()]


def save_tickets(tickets, filename):
    with open(filename, "w") as f:
        for ticket in tickets:
            f.write(" ".join(map(str, ticket)) + "\n")


def print_and_highlight(draw, tickets):
    for ticket in tickets:
        print("Ticket: ")
        for number in ticket:
            if number in draw:
                print(f"\033[32m{number}\033[0m", end=" ")
            else:
                print(number, end=" ")
        print()
