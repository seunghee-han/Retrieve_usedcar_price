
import pymysql
import pandas as pd
import streamlit as st

# DB 접속
conn = pymysql.connect(host="192.168.0.22", user='team_4', passwd='123', database='sk15_4team', port=3306)
cur = conn.cursor()

cur.execute("show tables")
cur.fetchall()

# FAQ 데이터 가져오기 (질문과 답변)
cur.execute("SELECT question, answer FROM faq")
faq_data = cur.fetchall()  # 질문과 답변 리스트 가져오기

# Streamlit 앱 제목
st.title('❓자주 하는 질문 FAQ')

# 각 질문과 답변을 expander로 동적으로 출력
for i, (question, answer) in enumerate(faq_data):
    # 질문을 expander 제목에 추가하고, 클릭하면 답변이 보이도록 처리
    with st.expander(f'질문 {i + 1}: {question}'):  
        st.write(f"**답변:** {answer}")  # 답변을 직접적으로 함께 표시


# DB 연결 종료
conn.close()




