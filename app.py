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
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

st.title("AI Lesson Plan Generator")

grade = st.selectbox("Select Class", ["Class 5", "Class 6", "Class 7", "Class 8", "Class 9", "Class 10"])
subject = st.text_input("Subject")
topic = st.text_input("Topic")
duration = st.selectbox("Duration", ["30 minutes", "40 minutes", "1 hour"])

if st.button("Generate Lesson Plan"):
    prompt = f"""
    Create a complete lesson plan based on:
    Class: {grade}
    Subject: {subject}
    Topic: {topic}
    Duration: {duration}
    
    Include:
    - Learning objectives
    - Introduction
    - Classroom activities
    - Bloom's taxonomy application
    - Assessment tasks
    - Homework
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )

    st.subheader("Generated Lesson Plan")
    st.write(response.choices[0].message.content)
