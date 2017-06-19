class Dispatcher(object):
    callbacks = []

    @classmethod
    def register(cls, callback):
        cls.callbacks.append(callback)

    @classmethod
    def unregister(cls, callback):
        cls.callbacks.remove(callback)

    @classmethod
    def dispatch(cls, action):
        for callback in cls.callbacks:
            callback(action)


dispatch = Dispatcher.dispatch
