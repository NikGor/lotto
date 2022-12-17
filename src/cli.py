import argparse


def parse_args():
    """
    Parse command line arguments.
    >>> args = parse_args()
    >>> args.balls
    6
    >>> args.pool
    49
    >>> args.tickets
    5
    >>> args.save
    >>> args.load
    """
    parser = argparse.ArgumentParser(description="lotto 6/49 simulator")
    parser.add_argument("-b", "--balls", type=int, default=6, help="number of balls to draw")
    parser.add_argument("-p", "--pool", type=int, default=49, help="pool of balls")
    parser.add_argument("-t", "--tickets", type=int, default=5, help="number of tickets to generate")
    parser.add_argument("-s", "--save", type=str, help="save tickets to a file")
    parser.add_argument("-l", "--load", type=str, help="load tickets from a file")
    return parser.parse_args()
