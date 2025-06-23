import streamlit as st
from agent import agent

st.title("Chanakya Niti Bot 🤖")
query = st.text_input("Ask Chanakya something about life, success, politics, or strategy:")

if query:
    response = agent.run(query)
    st.markdown("### 🧠 Chanakya Says:")
    st.write(response)
