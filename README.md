# Streamlit Unlocked (stu)

Throw away your keys! With this tool you can say goodbye to ever setting keys on streamlit widgets again.
(Unless of course you do some funky stuff and break the delicate `auto_key` logic I have made)

This is a wrapper around [Streamlit](https://github.com/streamlit/streamlit). Go ahead and use it the same way, except
using widgets from `stu`

# Warning

NOTE: This is not safe for production. I do not recommend using it anywhere important.


# Importing
```python
import streamlit_unlocked as stu
```


# Features
- `auto_key`: creates a key for you!
- auto_keyed widgets: all widgets in `stu` will have `auto_key` by default.
- `smart_fragment`: use fragments like you expect them to work! return values to rerun the app and trigger external changes.


# Examples

## Smart Fragments
```python
import streamlit as st

import src as stu


@stu.smart_fragment
def frag1() -> bool:
    "content"


@stu.smart_fragment
def frag2() -> bool:
    b1 = stu.widgets.button("click me!")

    # Note: you should only return a non-None value if you want to trigger an app rerun
    if b1:
        return b1


@stu.smart_fragment
def frag3() -> bool | None:
    # you can have multiple of the same fragment!
    frag1()
    frag1()
    frag1()
    frag1()
    
    # you can respond to fragment output
    f2 = frag2()

    if f2:
        "wow you clicked that button!"

frag3()
```