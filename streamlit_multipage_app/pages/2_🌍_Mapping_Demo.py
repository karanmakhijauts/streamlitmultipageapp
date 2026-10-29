import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Mapping Demo", page_icon="🌍")

st.markdown("# Mapping Demo")
st.sidebar.header("Mapping Demo")
st.write(
    """This demo shows how to use `st.map` to display geospatial data.
    Pick a city and how many random points to scatter around it."""
)

CITIES = {
    "Sydney": (-33.8688, 151.2093),
    "San Francisco": (37.7749, -122.4194),
    "London": (51.5072, -0.1276),
    "Tokyo": (35.6762, 139.6503),
}

city = st.sidebar.selectbox("City", list(CITIES))
n_points = st.sidebar.slider("Number of points", 100, 5000, 1000, step=100)
spread = st.sidebar.slider("Spread (degrees)", 0.01, 0.20, 0.05)

lat, lon = CITIES[city]
rng = np.random.default_rng(42)
df = pd.DataFrame(
    {
        "lat": lat + rng.normal(0, spread, n_points),
        "lon": lon + rng.normal(0, spread, n_points),
    }
)

st.map(df)
st.caption(f"{n_points:,} random points around {city}.")
