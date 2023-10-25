import streamlit as st
import requests


with st.form('login'):
    username = st.text_input('Username:')
    password = st.text_input('Password:', type='password')
    submit = st.form_submit_button('login')

if submit:
    response = requests.post('https://www.boyastudio.top/login_temp', json={'username': username, 'password': password})
    st.write(response.json())
