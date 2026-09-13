import streamlit as st

from campus_storage import init_session_state
from campus_login import login_screen
from campus_registration import registration_screen
from campus_student import student_view
from campus_teacher import teacher_view

st.set_page_config(page_title="Campus Care", page_icon="🏫", layout="wide")

init_session_state()

# Restore login after a page refresh: a refresh starts a brand-new session,
# so we look up the account by the username we stashed in the URL at login time.
if st.session_state.current_user is None:
    role = st.query_params.get("role")
    username = st.query_params.get("user")
    if role in ("student", "teacher") and username:
        accounts = (
            st.session_state.student_accounts if role == "student" else st.session_state.teacher_accounts
        )
        matched = next((acc for acc in accounts if acc.username == username), None)
        if matched:
            st.session_state.current_user = role
            if role == "student":
                st.session_state.student = matched
            else:
                st.session_state.teacher = matched

st.title("🏫 Campus Care")
st.write("Student Problem Reporting & Tracking System")
st.divider()

if st.session_state.current_user is None:
    tab_login, tab_register = st.tabs(["Log In", "Register"])
    with tab_login:
        login_screen()
    with tab_register:
        registration_screen()
elif st.session_state.current_user == "student":
    student_view()
elif st.session_state.current_user == "teacher":
    teacher_view()