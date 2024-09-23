import streamlit as st

import langchain_helper
from langchain_helper import generate_restaurant_name_and_items



st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")
    st.write("**Menu Header**")
    for item in menu_items:
        st.write("-", item)
