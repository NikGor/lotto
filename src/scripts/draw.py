#!/usr/bin/env python3
from src.main import game
from src.cli import parse_args


def main():
    args = parse_args()
    game(args.balls, args.pool, args.tickets, args.save, args.load)


if __name__ == "__main__":
    main()
