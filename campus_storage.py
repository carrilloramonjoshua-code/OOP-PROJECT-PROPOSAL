import streamlit as st

from campus_models import Student, TeacherAdmin


# st.cache_resource holds ONE shared object in the server's memory that every
# browser tab/session reads from — this is what makes data visible across
# the student tab and the admin tab at the same time. Regular st.session_state
# is private to a single browser tab, which is why reports weren't showing up.

@st.cache_resource
def get_student_accounts():
    return [
        Student("Juan Dela Cruz", "juan", "1234"),
        Student("Liaw", "liaw", "liaw123"),
        Student("Carrillo", "carrillo", "carrillo123"),
    ]


@st.cache_resource
def get_teacher_accounts():
    return [
        TeacherAdmin("Ms. Santos", "admin", "admin123"),
        TeacherAdmin("Mr. Reyes", "reyes", "reyes123"),
        TeacherAdmin("Mrs. Dela Cruz", "delacruz", "delacruz123"),
    ]


@st.cache_resource
def get_shared_reports():
    return []  # shared across every tab/session, as long as the app is running


def register_student(name, username, password):
    """Add a new student account. Returns (success, message)."""
    accounts = st.session_state.student_accounts
    if any(acc.username == username for acc in accounts):
        return False, "That username is already taken."
    accounts.append(Student(name, username, password))
    return True, "Account created! You can now log in."


def register_teacher(name, username, password):
    """Add a new teacher/admin account. Returns (success, message)."""
    accounts = st.session_state.teacher_accounts
    if any(acc.username == username for acc in accounts):
        return False, "That username is already taken."
    accounts.append(TeacherAdmin(name, username, password))
    return True, "Account created! You can now log in."


def init_session_state():
    # per-tab state (who is logged in on THIS tab)
    if "current_user" not in st.session_state:
        st.session_state.current_user = None   # "student" or "teacher"

    # shared list of valid accounts (same list handed to every tab)
    if "student_accounts" not in st.session_state:
        st.session_state.student_accounts = get_student_accounts()
    if "teacher_accounts" not in st.session_state:
        st.session_state.teacher_accounts = get_teacher_accounts()

    # the SPECIFIC account logged in on this tab, set at login time
    if "student" not in st.session_state:
        st.session_state.student = None
    if "teacher" not in st.session_state:
        st.session_state.teacher = None

    if "reports" not in st.session_state:
        st.session_state.reports = get_shared_reports()