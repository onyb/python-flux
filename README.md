# python-flux
Event-driven state management in pure Python inspired by Facebook Flux

# Example usage

```py
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
    dispatch({'type': 'INCREMENT'})
    
def logger():
   print(Counter.get_state()) 

Counter.add_listener(logger)

print(Counter.get_state())  # 0
increment()  # 1
increment()  # 2
```
