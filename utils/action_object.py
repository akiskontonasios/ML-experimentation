class Action(object):
    """
    Base action for command line utilities. Each command line utility may consist of one or more actions.
    """

    def prepare_args(self, parser):
        """
        Add arguments to argument parser.
        :param parser: the argument parser to add arguments to.
        """
        pass

    @property
    def name(self):
        """
        Returns the name of the action.
        :return: the name of the action.
        """
        raise ValueError('You need to define a name for the action.')

    @property
    def skipable(self):
        """
        Whether this action can be skipped or not. Default true.
        :return: Whether this action can be skipped or not. Default true.
        """
        return True

    def run(self, args, context=None):
        """
        Runs the actual logic of the action.
        :param args: command line arguments.
        :param context: state passed between actions.
        """
        pass
