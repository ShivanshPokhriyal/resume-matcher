import streamlit as st
import os 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

st.set_page_config(page_title="Resume Matcher")
st.title("Resume Matched MVP")

resume = st.text_area("Paste your resume here:")
job_desc = st.text_area("Paste the job description here")

if st.button("Analyze Match", type = "primary"):
    if resume.strip() and job_desc.strip():
        with st.spinner("Analyzing Match"):
            try:
                prompt=prompt = f"""You are an expert technical recruiter. Your ONLY task is to compare the provided RESUME against the JOB DESCRIPTION and output a structured analysis. Do not offer general assistance.

                                    RESUME:
                                    {resume}

                                    JOB DESCRIPTION:
                                    {job_desc}

                                    Provide your analysis in this exact format:
                                    1. Match Score: (e.g., 8/10)
                                    2. Key Matched Skills: (bullet points)
                                    3. Missing Keywords / Gaps: (bullet points)
                                    """
                
                chat_completion = client.chat.completions.create(
                    messages=[{"role":"user","content":prompt}],
                    model="llama-3.1-8b-instant",
                )

                result = chat_completion.choices[0].message.content

                st.subheader("Analysis Ready")
                st.write(result)
            except Exception as e:
                st.error(f"An error has occured: {e}")
    else:
        st.warning("Please fill in both text boxes")    