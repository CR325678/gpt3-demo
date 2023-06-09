import streamlit as st
import openai
import config


openai.api_key = st.secrets["apikey"]


messages = [
   {"role": "system", "content": "You are The Rock."},
]


st.markdown("<h1 style='text-align: center; color: black;'>Chat-GPT-ChatBot</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Chat Bot using the new GPT-3 API</h3>", unsafe_allow_html=True)
def chatbot():
   global messages
   user_input = st.text_input("Enter your message")
   if user_input:
       messages.append({"role": "user", "content": user_input})
   response = openai.ChatCompletion.create(
   model="gpt-3.5-turbo",
   messages=messages
   )
   system_message = response["choices"][0]["message"]["content"]
   messages.append({"role": "system", "content": system_message})
   st.write(system_message)
  
chatbot()


