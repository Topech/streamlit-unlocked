from typing import Callable

from src.auto_key import auto_key_layer

# inputs -> go in


def smart_fragment(fn: Callable):
    def _decorated_fragment(*args, **kwargs):
        with auto_key_layer(fn.__name__):
            fn()

    return _decorated_fragment


# output -> None, only callbacks?
