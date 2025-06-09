import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pymysql
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

#DB접속
conn = pymysql.connect(host="192.168.0.22", user='team_4', passwd='123', database='sk15_4team', port=3306)
cur = conn.cursor()

st.title('등록 차량 통계')

# 햔글 폰트 적용
font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = font_name

# 쿼리 실행
query = "SELECT brandName, COUNT(*) FROM car_info GROUP BY brandName"
cur.execute(query)
data = cur.fetchall()

#데이터 분리
labels = [row[0] for row in data]
sizes = [row[1] for row in data]


# 파이차트 그리기
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
ax.set_title("브랜드별 차량 분포")
ax.axis('equal')

# Streamlit에 그래프 출력
st.pyplot(fig)




