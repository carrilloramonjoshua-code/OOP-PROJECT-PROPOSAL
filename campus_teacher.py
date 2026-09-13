import streamlit as st

STATUS_OPTIONS = ["Pending", "Approved", "Rejected", "In Progress", "Resolved"]


def teacher_view():
    teacher = st.session_state.teacher
    st.subheader(f"Welcome, {teacher.name} (Teacher/Admin)")

    if st.button("🔄 Refresh"):
        st.rerun()

    tab_view, tab_update = st.tabs(["View Reports", "Update Report"])

    with tab_view:
        view_reports()

    with tab_update:
        update_report()

    if st.button("Log Out"):
        st.session_state.current_user = None
        st.query_params.clear()
        st.rerun()


def view_reports():
    st.markdown("##### Submitted Reports")
    if not st.session_state.reports:
        st.info("No reports available.")
    else:
        for i, report in enumerate(st.session_state.reports, 1):
            with st.expander(f"Report #{i} — {report.status}"):
                report.display()


def update_report():
    st.markdown("##### Update Report")
    if not st.session_state.reports:
        st.info("No reports available.")
        return

    options = [
        f"Report #{i} — {r.student_name} ({r.status})"
        for i, r in enumerate(st.session_state.reports, 1)
    ]
    choice = st.selectbox("Select a report", options)
    index = options.index(choice)
    report = st.session_state.reports[index]
    report.display()

    new_status = st.selectbox(
        "New status",
        STATUS_OPTIONS,
        index=STATUS_OPTIONS.index(report.status),
    )
    if st.button("Update Status"):
        report.status = new_status
        st.success("Report status updated successfully.")
        st.rerun()