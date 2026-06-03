import streamlit as st
from utils.api_client import login, register

st.title("💰 Expense Tracker")

tab1, tab2 = st.tabs(["Login", "Register"])

with tab1:
    st.subheader("Login")
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")
    if st.button("Login"):
        result = login(username, password)
        if "access_token" in result:
            st.session_state["token"] = result["access_token"]
            st.session_state["username"] = username
            st.success(f"Welcome {username}!")
            st.switch_page("pages/1_Dashboard.py")
        else:
            st.error("Invalid credentials!")

with tab2:
    st.subheader("Register")
    new_username = st.text_input("Username", key="reg_user")
    new_password = st.text_input("Password", type="password", key="reg_pass")
    if st.button("Register"):
        result = register(new_username, new_password)
        st.success("Account created! Please login.")