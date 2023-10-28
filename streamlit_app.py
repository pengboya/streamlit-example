import streamlit as st
import requests
import json
from streamlit_echarts import st_echarts

if 'sid' not in st.session_state:
    st.session_state.sid = ''
    st.session_state.candlestick_options = None


def login():
    response = requests.post('http://127.0.0.1:5000/login', json={'email': email, 'password': password})
    receive = response.json()
    st.session_state.sid = receive.get('sid')
    st.session_state.email = receive.get('email')
    st.session_state.username = receive.get('username')


def test():
    response = requests.post('http://127.0.0.1:5000/test', json={'sid': sid, 'email': email, 'code': code})
    receive = response.json()
    st.session_state.candlestick_options = receive.get('candlestick_options')


if len(st.session_state.sid) == 0:
    email = st.text_input('邮箱：')
    password = st.text_input('密码：', type='password')
    st.button('登录', on_click=login)
else:
    sid = st.session_state.sid
    email = st.session_state.email
    name = st.session_state.username
    st.write('欢迎，' + name)
    col1, col2 = st.columns(2)
    with col1:
        code = st.text_input(label='Code:', label_visibility="collapsed")
    with col2:
        st.button('查询', on_click=test)
    if st.session_state.candlestick_options is not None:
        st_echarts(options=json.loads(st.session_state.candlestick_options))
