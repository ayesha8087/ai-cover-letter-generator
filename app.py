import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Cover Letter Generator",
    page_icon="✉️",
    layout="centered"
)

# ---------------- TITLE ----------------
st.title("✉️ AI Cover Letter Generator")

st.caption(
    "Generate professional cover letters using resumes and job descriptions."
)

st.markdown("---")

# ---------------- INPUT FIELDS ----------------
candidate_name = st.text_input(
    "👤 Enter Your Name"
)

job_role = st.text_input(
    "💼 Enter Job Role"
)

resume = st.text_area(
    "📄 Paste Resume",
    height=200
)

job_description = st.text_area(
    "📝 Paste Job Description",
    height=200
)

# ---------------- BUTTON ----------------
if st.button("🚀 Generate Cover Letter"):

    # ---------------- VALIDATION ----------------
    if candidate_name and job_role and resume and job_description:

        # ---------------- COVER LETTER ----------------
        cover_letter = f"""
Dear Hiring Manager,

I am excited to apply for the position of {job_role}.

My skills and background align closely with the requirements mentioned in the job description. I have experience working on relevant projects and I am passionate about learning, problem-solving, and contributing to successful teams.

With my technical knowledge and dedication, I believe I can add value to your organization and grow professionally in this role.

Thank you for considering my application. I would welcome the opportunity to discuss my qualifications further.

Sincerely,

{candidate_name}
"""

        # ---------------- OUTPUT ----------------
        st.success("✅ Cover Letter Generated Successfully")

        st.subheader("📨 Generated Cover Letter")

        st.write(cover_letter)

        # ---------------- DOWNLOAD BUTTON ----------------
        st.download_button(
            label="📥 Download Cover Letter",
            data=cover_letter,
            file_name="cover_letter.txt",
            mime="text/plain"
        )

    else:
        st.warning("⚠️ Please fill all fields.")