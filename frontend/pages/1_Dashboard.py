import streamlit as st
import plotly.express as px
import pandas as pd
from utils.api_client import get_summary, get_expenses
from datetime import datetime

if "token" not in st.session_state:
    st.warning("Please login first!")
    st.switch_page("pages/0_Login.py")

st.title("📊 Dashboard")

token = st.session_state["token"]
month = st.text_input("Month (YYYY-MM)", value=datetime.now().strftime("%Y-%m"))
summary = get_summary(token, month)
st.write(summary)

if "total_income" in summary:
    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Income", f"₹{summary['total_income']}")
    col2.metric("💸 Expenses", f"₹{summary['total_expenses']}")
    col3.metric("✅ Net Balance", f"₹{summary['net_balance']}")

    expenses = get_expenses(token)
    if expenses and "error" not in expenses:
        df = pd.DataFrame(expenses)
        if not df.empty:
            fig = px.pie(df, values="amount", names="category", title="Expenses by Category")
            st.plotly_chart(fig)
else:
    st.error("Could not load summary!")