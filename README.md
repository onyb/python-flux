# python-flux
Event-driven state management in pure Python inspired by Facebook Flux

# Example usage

```py
from flux.dispatcher import dispatch
from flux.store import Store

class Counter(Store):
    """Custom Store containing the state and reduction logic. """
    _state = 0

    @staticmethod
    def reduce(state, action):
        """Pure function containing to return the updated state based on the action."""
        if action['type'] == 'INCREMENT':
            return state + 1
        else:
            return state

def increment():
    """Analogous to Flux action"""
    dispatch({'type': 'INCREMENT'})
    
def logger():
   """Analogous to React views"""
   print(Counter.get_state()) 

Counter.add_listener(logger)  # Bind the view to the store

print(Counter.get_state())  # 0
increment()  # 1
increment()  # 2
```
