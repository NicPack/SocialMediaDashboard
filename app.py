import streamlit as st
from st_pages import add_page_title, get_nav_from_toml

from scripts.load_data import load_dataset_to_df

st.set_page_config(layout="wide")
# Load the dataset into a DataFrame
data = load_dataset_to_df()

nav = get_nav_from_toml(".streamlit/pages.toml")

st.logo("assets/reddit-logo.png", size="large")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()
