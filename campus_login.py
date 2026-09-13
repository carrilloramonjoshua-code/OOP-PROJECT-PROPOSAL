import streamlit as st


def login_screen():
    st.subheader("Login")
    role = st.radio("Login as", ["Student", "Teacher/Admin"], horizontal=True)

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Log In")

    if submitted:
        account = st.session_state.student if role == "Student" else st.session_state.teacher
        if account.login(username, password):
            logged_in_as = "student" if role == "Student" else "teacher"
            st.session_state.current_user = logged_in_as
            st.query_params["role"] = logged_in_as   # remembers login across a page refresh
            st.success(f"Welcome, {account.name}!")
            st.rerun()
        else:
            st.error("Invalid username or password.")

    st.caption("Demo accounts — Student: juan / 1234 · Teacher: admin / admin123")