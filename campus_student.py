import streamlit as st

from campus_models import Report


def student_view():
    student = st.session_state.student
    st.subheader(f"Welcome, {student.name} (Student)")

    tab_report, tab_myreports = st.tabs(["Report a Problem", "My Reports"])

    with tab_report:
        submit_report(student)

    with tab_myreports:
        view_my_reports(student)

    if st.button("Log Out"):
        st.session_state.current_user = None
        st.query_params.clear()
        st.rerun()


def submit_report(student):
    st.markdown("##### Report a Problem")
    with st.form("report_form", clear_on_submit=True):
        problem = st.text_area("Problem")
        location = st.text_input("Location")
        photo = st.file_uploader("Photo (optional)", type=["png", "jpg", "jpeg"])
        submit = st.form_submit_button("Submit Report")

    if submit:
        if not problem or not location:
            st.warning("Please fill in the problem and location.")
        else:
            report = Report(student.name, problem, location, photo)
            student.reports.append(report)
            st.session_state.reports.append(report)
            st.success("Report submitted successfully!")


def view_my_reports(student):
    st.markdown("##### My Reports")
    if not student.reports:
        st.info("You have no reports.")
    else:
        for i, report in enumerate(student.reports, 1):
            with st.expander(f"Report #{i} — {report.status}"):
                report.display()