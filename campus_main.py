import streamlit as st

from campus_storage import init_session_state
from campus_login import login_screen
from campus_student import student_view
from campus_teacher import teacher_view

st.set_page_config(page_title="Campus Care", page_icon="🏫", layout="wide")

init_session_state()

# Restore login after a page refresh: a fresh refresh starts a brand-new
# session, so we check the URL for the role we stashed there at login time.
if st.session_state.current_user is None and st.query_params.get("role") in ("student", "teacher"):
    st.session_state.current_user = st.query_params.get("role")

st.title("🏫 Campus Care")
st.write("Student Problem Reporting & Tracking System")
st.divider()

if st.session_state.current_user is None:
    login_screen()
elif st.session_state.current_user == "student":
    student_view()
elif st.session_state.current_user == "teacher":
    teacher_view()