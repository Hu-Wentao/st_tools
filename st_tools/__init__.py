from typing import Callable, Any

import streamlit as st


def tool_s_state(update, k: str, init: Callable[[], Any] | Any = None,
                 force_update=False, force_init=False):
    """
    :param force_init: force init value, ignore key in st.session_state
    :param force_update: force update value, ignore `update` is or not None
    :param update: update state value
    :param k: st.state_session state key
    :param init: init state value or init function
    :return: state
    """
    if update is not None or force_update:  # 有新值(或强制刷新)
        st.session_state[k] = update
    elif k not in st.session_state or force_init:  # 无值,且未注册key (或强制更新为init)
        if isinstance(init, Callable):
            _value = init()
        else:
            _value = init
        st.session_state[k] = _value
    return st.session_state[k]
