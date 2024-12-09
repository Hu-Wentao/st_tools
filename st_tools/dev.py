import streamlit as st
# === DEV UI Widget
def dev_ui_session_state(show_on: tuple[str] = ('dev', 'test')):
    if st.secrets['env'] not in show_on:
        return
    with st.expander("DEV_状态"):
        st.json(st.session_state)


def dev_ui_container(show_on: tuple[str] = ('dev', 'test')):
    if st.secrets['env'] not in show_on:
        return
    return st.expander
