import streamlit as st

from campus_models import Student, TeacherAdmin


# st.cache_resource holds ONE shared object in the server's memory that every
# browser tab/session reads from — this is what makes data visible across
# the student tab and the admin tab at the same time. Regular st.session_state
# is private to a single browser tab, which is why reports weren't showing up.

@st.cache_resource
def get_student_account():
    return Student("Juan Dela Cruz", "juan", "1234")


@st.cache_resource
def get_teacher_account():
    return TeacherAdmin("Ms. Santos", "admin", "admin123")


@st.cache_resource
def get_shared_reports():
    return []  # shared across every tab/session, as long as the app is running


def init_session_state():
    # per-tab state (who is logged in on THIS tab)
    if "current_user" not in st.session_state:
        st.session_state.current_user = None   # "student" or "teacher"

    # shared state (same object handed to every tab)
    if "student" not in st.session_state:
        st.session_state.student = get_student_account()
    if "teacher" not in st.session_state:
        st.session_state.teacher = get_teacher_account()
    if "reports" not in st.session_state:
        st.session_state.reports = get_shared_reports()