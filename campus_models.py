import streamlit as st


class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password


class Student(User):
    def __init__(self, name, username, password):
        super().__init__(name, username, password)
        self.reports = []


class TeacherAdmin(User):
    def __init__(self, name, username, password):
        super().__init__(name, username, password)


class Report:
    def __init__(self, student_name, problem, location, photo):
        self.student_name = student_name
        self.problem = problem
        self.location = location
        self.photo = photo
        self.status = "Pending"

    def display(self):
        st.write(f"**Student:** {self.student_name}")
        st.write(f"**Problem:** {self.problem}")
        st.write(f"**Location:** {self.location}")
        if self.photo is not None:
            st.image(self.photo, caption="Attached photo", width=250)
        else:
            st.write("**Photo:** None")
        status_color = {
            "Pending": "orange",
            "Approved": "blue",
            "Rejected": "red",
            "In Progress": "violet",
            "Resolved": "green",
        }.get(self.status, "gray")
        st.markdown(f"**Status:** :{status_color}[{self.status}]")