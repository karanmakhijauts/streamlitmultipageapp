import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """This demo shows how to use `st.dataframe` and `st.bar_chart` to
    explore a table. Choose which groups to compare."""
)


@st.cache_data
def get_data() -> pd.DataFrame:
    rng = np.random.default_rng(7)
    years = list(range(2015, 2026))
    regions = ["North", "South", "East", "West", "Central"]
    data = {r: rng.integers(50, 500, len(years)) for r in regions}
    return pd.DataFrame(data, index=pd.Index(years, name="Year"))


df = get_data()
choices = st.multiselect("Choose regions", list(df.columns), ["North", "South"])

if not choices:
    st.error("Please select at least one region.")
else:
    data = df[choices]
    st.write("### Sales by year (units)", data.sort_index())
    st.bar_chart(data)
    st.download_button(
        "Download CSV", data.to_csv().encode("utf-8"), "sales.csv", "text/csv"
    )
