import streamlit as st

import src as stu


@stu.smart_fragment
def frag_1():
    stu.widgets.button("1")


@stu.smart_fragment
def frag_2():
    frag_1()
    "--"
    stu.widgets.button("1")
    stu.widgets.button("2")


@stu.smart_fragment
def frag_3():
    frag_2()
    "----"
    frag_2()


frag_3()


st.session_state
