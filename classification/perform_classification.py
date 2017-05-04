from utils.importing_functions import create_parser
from utils.action_object import Action

import pandas as pd


class LoadDataAction(Action):
    @property
    def name(self):
        return 'load'

    def prepare_args(self, parser):
        parser.add_argument('-path', '--file_path', dest='file_path',
                            help='File containing data',
                            metavar='file_path', required=True)

    def run(self, args, context=None):
        context['data'] = pd.read_csv(args.file_path)
        k = 1


class TrainModelAction(Action):
    @property
    def name(self):
        return 'model training'

    def run(self, args, context=None):
        pass


def main(argv=None):

    program_shortdesc = __import__('__main__').__doc__
    actions = [LoadDataAction(), TrainModelAction()]
    parser = create_parser(actions, program_shortdesc)
    args = parser.parse_args(argv)
    context = {}
    for action in actions:
        action.run(args, context)

if __name__ == "__main__":
    main()