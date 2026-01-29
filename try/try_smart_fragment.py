import datetime as dt

import streamlit as st

import src as stu


@stu.smart_fragment
def frag1() -> bool:
    "content"
    st.write(dt.datetime.now().isoformat())


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
