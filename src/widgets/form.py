import streamlit as st

from src.auto_key import enable_auto_keyed_widget

form = enable_auto_keyed_widget(st.form, key_args_index=0)
form_submit_button = enable_auto_keyed_widget(st.form_submit_button)
