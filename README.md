# Streamlit Unlocked (stu)

Throw away your keys!

With this tool you can say goodbye to setting keys on streamlit widgets.
(Unless of course you do some funky stuff and break the delicate `auto_key` logic I have made)

This is a wrapper around [Streamlit](https://github.com/streamlit/streamlit).
Streamlit Unlocked (`stu`) provides widgets that automatically handle keys.

## Warning

NOTE: This is not safe for production. I do not recommend using it anywhere important.


## Importing
```python
import streamlit_unlocked as stu
```


## Features
- `auto_key`: creates a key for you!
- auto_keyed widgets: all widgets in `stu` will have `key=auto_key()` by default.
- `smart_fragment`: use fragments more like normal functions!

### Smart Fragments
Smart fragments provide:
- Nested smart fragments 'just work'
- use return value outside of fragments (they are accessible on next app-wide rerun)
- configure `on_return_strategy` to trigger app-wide rerun based on return value)

## Examples

### Nested Smart Fragments

You can use smart fragments to enhance streamlit fragments.

```python
import streamlit as st

import streamlit_unlocked as stu


@stu.smart_fragment
def frag1() -> bool:
    "content"


@stu.smart_fragment
def frag2() -> bool:
    t1 = stu.widgets.toggle("click me!")

    return t1


@stu.smart_fragment
def frag3() -> bool | None:
    # you can have multiple of the same fragment!
    frag1()
    frag1()
    frag1()
    frag1()
    
    # you can respond to fragment output
    f2 = frag2()

    # with default smart_fragments, you must trigger a rerun to access fragment return values
    # (in streamlit, buttons and input will trigger a rerun of an app or current fragment)
    saved = stu.widgets.button("save")
    if saved and f2:
        "wow you clicked that button!"

frag3()
```