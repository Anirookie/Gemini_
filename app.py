from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini pro and get response
model=genai.GenerativeModel('gemini-pro')
def get_response(question):
    response=model.generate_content(question)
    return response.text

##Initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLm Application")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

#When clicked

if submit:
    response=get_response(input)
    st.write("The response is")
    st.write(response)

