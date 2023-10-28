import streamlit as st
import requests
import json
from streamlit_echarts import st_echarts

if 'sid' not in st.session_state:
    st.session_state.sid = ''
    st.session_state.chart = None


def login():
    response = requests.post('https://www.boyastudio.top/login', json={'email': email, 'password': password})
    receive = response.json()
    st.session_state.sid = receive.get('sid')
    st.session_state.email = receive.get('email')
    st.session_state.username = receive.get('username')


def test():
    response = requests.post('https://www.boyastudio.top/test', json={'sid': sid, 'email': email, 'code': code})
    st.session_state.chart = json.loads(response.text)


if len(st.session_state.sid) == 0:
    email = st.text_input('Email:')
    password = st.text_input('Password:', type='password')
    st.button('login', on_click=login)
else:
    sid = st.session_state.sid
    email = st.session_state.email
    name = st.session_state.username
    st.write('欢迎，' + name)
    col1, col2 = st.columns(2)
    with col1:
        code = st.text_input(label='Code:', label_visibility="collapsed")
    with col2:
        st.button('test', on_click=test)
    if st.session_state.chart is not None:
        st_echarts(options=st.session_state.chart)
