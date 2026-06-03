import streamlit as st
from utils.api_client import add_expense, get_categories

if "token" not in st.session_state:
    st.warning("Please login first!")
    st.switch_page("pages/0_Login.py")

st.title("➕ Add Expense")

token = st.session_state["token"]

categories = get_categories(token)

amount = st.number_input("Amount (₹)", min_value=0.0)
category = st.selectbox("Category", categories)
note = st.text_input("Note (optional)")

if st.button("Add Expense"):
    result = add_expense(token, amount, category, note)
    if "message" in result:
        st.success("Expense added successfully!")
    else:
        st.error("Something went wrong!")