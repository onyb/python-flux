class Dispatcher(object):
    callbacks = set()

    @classmethod
    def register(cls, callback):
        if callback not in cls.callbacks:
            cls.callbacks.add(callback)

    @classmethod
    def unregister(cls, callback):
        cls.callbacks.remove(callback)

    @classmethod
    def dispatch(cls, action):
        for callback in cls.callbacks:
            callback.get_update_hook()(action)

dispatch = Dispatcher.dispatch
