import streamlit as st

from streamlit_unlocked.auto_key import enable_auto_keyed_widget

data_editor = enable_auto_keyed_widget(st.data_editor)
