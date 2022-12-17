from src.cli import parse_args


def test_parse_args():
    args = parse_args()
    assert args.balls == 6
    assert args.pool == 49
    assert args.tickets == 5
    assert args.save is None
    assert args.load is None
