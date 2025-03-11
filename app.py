import streamlit as st
from main import main_workflow 

st.title("LinkedIn Post Generator")

user_input = st.text_area("Enter your topic:")

if st.button("Generate Post"):
    if user_input:
        with st.spinner("Generating post..."):
            final_post = main_workflow(user_input)
        
        st.write(final_post)
    else:
        st.warning("Please enter a topic.")