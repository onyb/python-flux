from .dispatcher import Dispatcher


class Store(object):
    _state = None
    _listeners = set()

    @classmethod
    def get_state(cls):
        return cls._state

    @classmethod
    def add_listener(cls, callback):
        if callback not in cls._listeners:
            cls._listeners.add(callback)

            Dispatcher.register(cls)

    @classmethod
    def emit_change_event(cls):
        for listener in cls._listeners:
            listener()

    @classmethod
    def remove_listener(cls, callback):
        cls._listeners.remove(callback)

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
