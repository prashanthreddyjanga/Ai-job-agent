import streamlit as st

# Title
st.title("AI Job Application Agent")

# Inputs
resume = st.text_area("Paste Your Resume")
jd = st.text_area("Paste Job Description")

# Button
if st.button("Generate Email"):
    email = f"""
Subject: Application for AI Innovation Intern

Dear Hiring Manager,

I am excited to apply for this position.

Based on my experience:
{resume}

And your requirements:
{jd}

I believe my skills make me a strong candidate for this role.

Thank you for your consideration.

Regards,
Prashanth
"""
    st.write("match score:75%")
    st.text_area("Generated Email", email,height=300)