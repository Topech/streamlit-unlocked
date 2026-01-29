import streamlit as st

from src.auto_key import enable_auto_keyed_widget

audio_input = enable_auto_keyed_widget(st.audio_input)
camera_input = enable_auto_keyed_widget(st.camera_input)
chat_input = enable_auto_keyed_widget(st.chat_input)
date_input = enable_auto_keyed_widget(st.date_input)
datetime_input = enable_auto_keyed_widget(st.datetime_input)
number_input = enable_auto_keyed_widget(st.number_input)
text_input = enable_auto_keyed_widget(st.text_input)
time_input = enable_auto_keyed_widget(st.time_input)


checkbox = enable_auto_keyed_widget(st.checkbox)
color_picker = enable_auto_keyed_widget(st.color_picker)
file_uploader = enable_auto_keyed_widget(st.file_uploader)
multiselect = enable_auto_keyed_widget(st.multiselect)
segmented_control = enable_auto_keyed_widget(st.segmented_control)


radio = enable_auto_keyed_widget(st.radio, key_args_index=4)
selectbox = enable_auto_keyed_widget(st.selectbox, key_args_index=4)
select_slider = enable_auto_keyed_widget(st.select_slider, key_args_index=4)
slider = enable_auto_keyed_widget(st.slider, key_args_index=6)


toggle = enable_auto_keyed_widget(st.toggle)
text_area = enable_auto_keyed_widget(st.text_area)
