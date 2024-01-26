# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title("AI coder with Python")

content = st.text_input('무슨 코드를 만들건지 영어로 입력해주세요.')

if st.button('코드 작성 요청하기'):
    with st.spinner('코드 작성 중...'):
        result = chat_model.predict("write a code with python:" + content)
        st.write(result)
