import streamlit as st

from streamlit_unlocked.auto_key import enable_auto_keyed_widget

button = enable_auto_keyed_widget(st.button, key_args_index=1)
link_button = st.link_button  # note: doesn't have key parameter
download_button = enable_auto_keyed_widget(st.download_button, key_args_index=1)
pills = enable_auto_keyed_widget(st.pills, key_args_index=1)
feedback = enable_auto_keyed_widget(st.feedback)
