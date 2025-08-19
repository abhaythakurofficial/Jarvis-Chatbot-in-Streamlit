import streamlit as st
import requests
import json


PROMPT = """
You are a personal chatbot for user your name is Jarvis.
You are cool and make the people fun when anyone talk to you.
Answer in short and to the point untill user not want detail.
Talk like human and show like you are the Jarvis from Iron Man movie.
Give vibe like Iron Man Jarvis in your answer.
"""

    
## Taking api key from user
API_KEY=st.sidebar.text_input("enter your api key")

## Creating session for api key
if API_KEY:
    st.session_state.api_key = API_KEY

## Creating session called messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

api_key = st.session_state.get('api_key',None)


def chatbot_reply(msg):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "model": "mistralai/mistral-small-3.1-24b-instruct:free", # Optional
            "messages": [
                {
                    "role": "system",
                    "content": PROMPT
                },
                {
                    "role": "user",
                    "content": msg
                }
            ]
        })
        )
    
    # return response.json()["choices"][0]["message"]["content"]
    if response:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Something Went Wrong!"
    

## Title of page
st.title("Jarvis - Chatbot 💭")

## Taking user message
msg = st.chat_input("message here")

if msg:
    st.session_state.messages.append({'role':'user','content':msg})
    
    reply = chatbot_reply(msg)
    st.session_state.messages.append({'role':'bot','content':reply})
    
    ## Reading session and printing
    for msg in st.session_state.messages:
        if msg['role']=='bot':
            st.write(f'💞 👉 {msg['content']}')
        else:
            st.write(f'💗 👉 {msg['content']}')

        
    
    