class Dispatcher(object):
    callbacks = []

    @classmethod
    def register(cls, callback):
        if callback not in cls.callbacks:
            cls.callbacks.append(callback)

    @classmethod
    def unregister(cls, callback):
        cls.callbacks.remove(callback)

    @classmethod
    def dispatch(cls, action):
        for callback in cls.callbacks:
            print(cls.callbacks)
            callback(action)



dispatch = Dispatcher.dispatch
