from contextlib import contextmanager


class Suppressor:
    """Class Suppressor suppress passed error

    Attributes:
        error: Exception
    """

    def __init__(self, error):
        """
        Sets all required attributes for the object

        Parameters:
            error: Exception
        """
        self.error = error

    def __enter__(self):
        """ """
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Suppress the error if type of the error equal passed error
        Parameters:
            exc_type: Exception, error occurred
            exc_val: value of the error
            exc_tb: traceback of the error
        Return:
            boolean (True if type of the error equal passed error, else False)
        """
        return exc_type is not None and issubclass(exc_type, self.error)


@contextmanager
def suppressor(error):
    """
    Function suppress passed error
    :param error: Exception, passed error
    :return: boolean(True if type of the error equal passed error, else False)
    """
    try:
        yield
    except error:
        return
