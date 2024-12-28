# st_tools
Streamlit tools

## Install
```requirements.txt
git+https://github.com/Hu-Wentao/st_tools.git
```
or
```sh
pip install git+https://github.com/Hu-Wentao/st_tools.git
```

## State Management: `tool_s_state`

```python
import streamlit as st

from st_tools import tool_s_state


# 0. Define
def s_count(update: int = None, init=lambda: 2) -> int:
    return tool_s_state(
        update, 's_count',
        init=init
    )


# 1. setter
s_count(1)

# 2. getter
value = s_count()
# show
st.write(value)
```

## Path(File/Folder)Selector: `st_path_selector`

```python
import streamlit
from st_tools.widgets import st_path_selector

_path = st_path_selector(path='./')
streamlit.write(f"You Selected# {_path}")
```
