import streamlit as st
import google.generativeai as genai
import os

# 1. Fetch API Key securely
api_key = os.environ.get(AIzaSyAkyKEF0rLlG1fhVkXxiR4X9mIaUnbxg7M)
if not api_key:
    st.error("API Key missing! Please set the GEMINI_API_KEY secret/environment variable.")
    st.stop()

genai.configure(api_key=api_key) 

# 2. Feed the College Data
college_knowledge = """
You are the official AI assistant for DVR & Dr. HS MIC College of Technology.
Be welcoming, helpful, and polite. 
Use the following information to answer questions:

- Name: DVR & Dr. HS MIC College of Technology
- Location: NH 9, Vijayawada - Hyderabad Highway, Kanchikacherla, N.T.R District, Andhra Pradesh 521180.
- Established: 2002
- Accreditations: NBA Accredited (Twice), NAAC "A+" Grade, ISO Certification.
- B.Tech Programs: Electronics & Communications (ECE), Computer Science (CSE), Electrical & Electronics (EEE), Mechanical (ME), Civil (CE), Information Technology (IT), Artificial Intelligence & Data Science (AI & DS), Artificial Intelligence & Machine Learning (AI & ML).
- Postgraduate Programs: MCA, MBA, M.Tech.
- Contact Details: Email: office@mictech.ac.in | Phone: +91 7382616824.
"""

model = genai.GenerativeModel('gemini-2.5-flash', system_instruction=college_knowledge)

# 3. Web UI Layout
st.set_page_config(page_title="MIC College Chatbot", page_icon="🎓")
st.title("MIC College AI Chatbot 🎓")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

for message in st.session_state.chat.history:
    role = "assistant" if message.role == "model" else "user"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

if prompt := st.chat_input("Ask me about MIC College..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = st.session_state.chat.send_message(prompt)
        st.markdown(response.text)