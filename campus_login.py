import streamlit as st


def login_screen():
    st.subheader("Login")
    role = st.radio("Login as", ["Student", "Teacher/Admin"], horizontal=True)

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Log In")

    if submitted:
        accounts = (
            st.session_state.student_accounts
            if role == "Student"
            else st.session_state.teacher_accounts
        )
        matched = next((acc for acc in accounts if acc.login(username, password)), None)

        if matched:
            logged_in_as = "student" if role == "Student" else "teacher"
            st.session_state.current_user = logged_in_as
            if role == "Student":
                st.session_state.student = matched
            else:
                st.session_state.teacher = matched

            # remembers login across a page refresh
            st.query_params["role"] = logged_in_as
            st.query_params["user"] = matched.username

            st.success(f"Welcome, {matched.name}!")
            st.rerun()
        else:
            st.error("Invalid username or password.")

    st.caption(
        "Demo accounts — Students: juan/1234, liaw/liaw123, carrillo/carrillo123 · "
        "Admins: admin/admin123, reyes/reyes123, delacruz/delacruz123"
    )