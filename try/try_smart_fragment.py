import datetime as dt

import streamlit as st

import src as stu


@stu.smart_fragment
def frag1() -> bool:
    "content"
    st.write(dt.datetime.now().isoformat())


@stu.smart_fragment(on_return_strategy="rerun_on_change")
def frag2() -> bool:
    t1 = stu.toggle("toggle me!")

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

    if f2:
        "wow you activated that toggle!"


frag3()
