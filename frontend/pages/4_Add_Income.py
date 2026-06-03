import streamlit as st
from utils.api_client import add_income

if "token" not in st.session_state:
    st.warning("Please login first!")
    st.switch_page("pages/0_Login.py")

st.title("💵 Add Income")

token = st.session_state["token"]

amount = st.number_input("Amount (₹)", min_value=0.0)
source = st.text_input("Source (e.g. Salary, Freelance)")

if st.button("Add Income"):
    result = add_income(token, amount, source)
    if "message" in result:
        st.success("Income added successfully!")
    else:
        st.error("Something went wrong!")