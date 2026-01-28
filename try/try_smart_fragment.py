import datetime as dt

import streamlit as st

import src as stu


@stu.smart_fragment
def frag_1():
    st.text(dt.datetime.now())
    stu.widgets.button("1")


@stu.smart_fragment
def frag_2():
    frag_1()
    "--"
    b2 = stu.widgets.button("2")
    b3 = stu.widgets.button("unwow")

    if b2:
        return True
    if b3:
        return False


@stu.smart_fragment
def frag_3():
    frag_2()
    "----"
    f2 = frag_2()

    if f2:
        "wow!"


frag_3()

for key, value in sorted(st.session_state.items(), key=lambda x: x[0]):
    st.code(key)
    st.code(value)
    "--"
