import streamlit as st;

st.logo("workzia_inc_logo.jpg", size="large", link="https://www.google.com", icon_image="workzia_inc_logo.jpg")

def page2():
    st.title("Page 2")

pages = {
    "Program" : [
        st.Page("programs.py", title="Select Program"),
        st.Page("enroll.py", title="Enroll Now")
    ],
    "Calculator":[
        st.Page("age_calculator.py", title="Age Calculator")
    ]
}

pg = st.navigation(pages, position="sidebar")
pg.run()