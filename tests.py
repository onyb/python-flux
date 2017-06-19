from unittest import TestCase, main
from unittest.mock import MagicMock

from flux.dispatcher import dispatch
from flux.store import Store


class Counter(Store):
    _state = 0

    @staticmethod
    def reduce(state, action):
        if action['type'] == 'INCREMENT':
            return state + 1
        else:
            return state


def increment():
    dispatch({
        'type': 'INCREMENT'
    })


class TestFlux(TestCase):
    def test_state_change(self):
        view = MagicMock()
        Counter.add_listener(view)

        increment()
        increment()

        self.assertTrue(view.called)
        self.assertEqual(view.call_count, 2)


if __name__ == '__main__':
    main()