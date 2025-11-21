import streamlit as st

st.title("SmartStudy Scheduler")

st.write("Welcome to the AI-powered study & lesson planning application!")

mode = st.selectbox("Select user type:", ["Student", "Teacher"])

if mode == "Student":
    st.header("Student Study Planner")

    subjects = st.text_input("Enter subjects (comma separated)")
    hours = st.number_input("How many study hours per day?", min_value=1, max_value=12)
    plan = st.selectbox("Select plan type", ["Weekly", "Monthly", "Yearly"])

    if st.button("Generate Study Plan"):
        st.success(f"Study Plan for {plan} generated successfully!")

elif mode == "Teacher":
    st.header("Teacher Lesson Planner")

    grade = st.text_input("Enter class (e.g., Class 8)")
    subject = st.text_input("Enter subject name")
    plan = st.selectbox("Select plan type", ["Weekly Lesson Plan", "Monthly Scheme", "Yearly Scheme"])

    if st.button("Generate Lesson Plan"):
        st.success(f"{plan} generated successfully!")
