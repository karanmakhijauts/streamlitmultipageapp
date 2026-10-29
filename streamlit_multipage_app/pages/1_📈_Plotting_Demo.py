import time

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo shows how to use `st.line_chart` to display a chart that
    updates progressively as data streams in. Press **Re-run** to watch again."""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
chart_slot = st.empty()

values = [float(np.random.randn())]
for i in range(1, 101):
    values.extend((values[-1] + np.random.randn(5).cumsum()).tolist())
    status_text.text("%i%% Complete" % i)
    chart_slot.line_chart(pd.DataFrame({"value": values}))
    progress_bar.progress(i)
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically re-run the script when interacted with,
# so this button simply triggers a fresh run.
st.button("Re-run")
