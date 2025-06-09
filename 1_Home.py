import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pymysql
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import matplotlib.cm as cm
import numpy as np

#DB접속
conn = pymysql.connect(host="192.168.0.22", user='team_4', passwd='123', database='sk15_4team', port=3306)
cur = conn.cursor()

st.title('📊등록된 중고 차량 통계')
st.header('현재 국내 중고 차량 등록 현황은?')

# 햔글 폰트 적용
font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = font_name

# 쿼리 실행
query = "SELECT brandName, COUNT(*) FROM car_info GROUP BY brandName"
cur.execute(query)
data = cur.fetchall()

# 데이터 분리
labels = [row[0] for row in data]
sizes = [row[1] for row in data]

# 색상 지정 (Set3 컬러맵)
colors = cm.Set3(np.linspace(0, 1, len(labels)))

# 색상 지정
colors = cm.Set3(np.linspace(0, 1, len(labels)))

# 막대그래프 그리기
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(range(len(sizes)), sizes, color=colors)

# X축 설정
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, fontsize=12)

# 제목 및 Y축 라벨
ax.set_ylabel("등록된 차량 수", fontsize=12)

# 레이아웃 정리
plt.tight_layout()

# Streamlit에 그래프 출력
st.pyplot(fig)



