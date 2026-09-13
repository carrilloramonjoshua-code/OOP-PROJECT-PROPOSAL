import streamlit as st

from campus_storage import register_student, register_teacher


def registration_screen():
    st.subheader("Create an Account")
    role = st.radio("Register as", ["Student", "Teacher/Admin"], horizontal=True, key="register_role")

    with st.form("registration_form", clear_on_submit=True):
        name = st.text_input("Full Name")
        username = st.text_input("Choose a Username")
        password = st.text_input("Choose a Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submitted = st.form_submit_button("Register")

    if submitted:
        if not name or not username or not password:
            st.warning("Please fill in all fields.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        elif len(password) < 4:
            st.error("Password must be at least 4 characters.")
        else:
            if role == "Student":
                success, message = register_student(name, username, password)
            else:
                success, message = register_teacher(name, username, password)

            if success:
                st.success(message)
            else:
                st.error(message)