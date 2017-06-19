from .dispatcher import Dispatcher


class Store(object):
    _state = None
    __listeners = []

    @classmethod
    def get_state(cls):
        return cls._state

    @classmethod
    def add_listener(cls, callback):
        cls.__listeners.append(callback)

    @classmethod
    def emit_change_event(cls):
        for listener in cls.__listeners:
            listener()

    @classmethod
    def remove_listener(cls, callback):
        cls.__listeners.remove(callback)

    @staticmethod
    def reduce(state, action):
        return state

    @classmethod
    def get_update_hook(cls):
        def f(action):
            new_state = cls.reduce(cls._state, action)

            if new_state != cls._state:
                cls._state = new_state
                cls.emit_change_event()

        return f


class Counter(Store):
    _state = 0

    @staticmethod
    def reduce(state, action):
        if action.type == 'INCREMENT':
            return state + 1
        else:
            return state


for store in Store.__subclasses__():
    Dispatcher.register(
        store.get_update_hook()
    )
