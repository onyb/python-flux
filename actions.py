from .dispatcher import dispatch


class Action(object):
    def __init__(self, **kwargs):
        self.__dict__ = kwargs


def increment():
    dispatch(
        Action(type='INCREMENT')
    )
