import os

import streamlit as st

from st_tools import tool_s_state


def st_path_selector(
        label='选择文件/文件夹', key='st_path_selector', path: str = '.', help: str = None,
        on_sort_dir=sorted,  # or use: from natsort import natsorted
) -> str:
    def s_path(update: str = None, navi_to: str = None) -> str:  # 核心状态, 选中的path, 可能是文件/文件夹
        if update:  # 当path以`/`结尾, 修复路径,移除`/`
            update = os.path.normpath(update)
        if navi_to is not None:
            update = os.path.abspath(os.path.join(s_path_dir(), navi_to))
        return tool_s_state(update, key, init=os.path.abspath(path))

    def s_path_dir() -> str:  # 选中路径所在的文件夹(如果选中文件夹则返回文件夹)
        _p = s_path()
        return _p if os.path.isdir(_p) else os.path.dirname(_p)

    def s_path_navi(update: str = None) -> str:  # 路径导航, 当前路径到 .. 或到 /foo 等...
        return tool_s_state(update, f"{key}.s_path_navi", init=os.path.abspath(path))

    def _dir_options():
        try:
            ls = os.listdir(s_path_dir())
        except FileNotFoundError:  # 用户输入了不存在的路径
            ls = []
        return ['.', '..', *on_sort_dir(ls)]

    # ==
    s_path()
    c1, c2 = st.columns([3, 1])
    c1.text_input('路径', key=key, placeholder='在此处粘贴或在右侧选择 文件/文件夹', help=help)
    c2.selectbox(
        key=f"{key}.s_path_navi",
        label=label,
        options=_dir_options(),
        format_func=lambda
            x: f"{'🗂️' if os.path.isdir(os.path.join(s_path_dir(), x)) else '🗒️'}  {
        ".\t(当前路径)" if x == '.' else
        "..\t(上级路径)" if x == '..' else
        x}",
        on_change=lambda: s_path(navi_to=s_path_navi())
    )
    return s_path()


# === st.dataframe / st.data_editor
def adp_data_editor_height(df_len: int, reserve=1, least_len=2, max_len: int = None) -> int:
    if df_len < least_len:
        df_len = least_len
    if max_len is not None and df_len > max_len:
        df_len = max_len
    return 2 + (df_len + 1 + reserve) * 35
