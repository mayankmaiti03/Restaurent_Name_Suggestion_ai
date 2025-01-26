import streamlit as st
import langchain_helper

st.title("Restaurent Name Generator")

cuisine=st.sidebar.selectbox("Pick a Cuisine",("Indian","Italian","Mexican","American","Arabic"))
    
if cuisine:
    response=langchain_helper.generate_restaurent_name_and_items(cuisine)
    st.header(response['restaurent_name'])
    menu_items=response['menu_items'].split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-",item)