import streamlit as st
import pandas as pd
from utils.api_client import get_expenses, get_income

if "token" not in st.session_state:
    st.warning("Please login first!")
    st.switch_page("pages/0_Login.py")

st.title("📜 History")

token = st.session_state["token"]

tab1, tab2 = st.tabs(["Expenses", "Income"])

with tab1:
    expenses = get_expenses(token)
    if expenses and "error" not in expenses:
        df = pd.DataFrame(expenses)
        if not df.empty:
            st.dataframe(df[["id", "date", "category", "amount", "note"]])
        else:
            st.info("No expenses yet!")
    else:
        st.error("Could not load expenses!")

with tab2:
    income = get_income(token)
    if income and "error" not in income:
        df = pd.DataFrame(income)
        if not df.empty:
            st.dataframe(df[["id", "date", "source", "amount"]])
        else:
            st.info("No income yet!")
    else:
        st.error("Could not load income!")