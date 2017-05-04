from argparse import ArgumentParser, RawDescriptionHelpFormatter


def create_parser(actions, description):

    parser = ArgumentParser(
        description=description,
        formatter_class=RawDescriptionHelpFormatter)

    for action in actions:
        action.prepare_args(parser)

    return parser