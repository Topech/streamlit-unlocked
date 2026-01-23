import streamlit as st

import src as stu


@stu.smart_fragment
def frag_1():
    stu.widgets.button("1")


@stu.smart_fragment
def frag_2():
    # frag_1()
    # "--"
    stu.widgets.button("1")
    stu.widgets.button("2")

    # st.session_state
    for key, value in sorted(st.session_state.items(), key=lambda x: x[0]):
        st.code(key)
        st.code(value)
        "--"

    return True


@stu.smart_fragment
def frag_3():
    frag_2()
    "----"
    frag_2()


frag_3()
