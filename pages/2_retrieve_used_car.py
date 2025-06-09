import pymysql 
import pandas as pd
import streamlit as st

# DB 연결
conn = pymysql.connect(
    host="192.168.0.22",
    user='team_4',
    passwd='123',
    database='sk15_4team',
    port=3306,
    charset='utf8mb4'  # 한글 깨짐 방지
)
cur = conn.cursor()

# Streamlit UI
st.title('🚗나만의 중고차 찾기')
st.subheader("💡검색어를 입력하면 해당하는 중고차 정보를 불러와요!")

col1, col2, col3, col4 = st.columns(4)

with col1:
    input_brand = st.text_input(label='브랜드명', placeholder="예) 현대")
with col2:
    input_model_name = st.text_input(label="모델명", placeholder="예) 아이오닉 5")
with col3:
    input_year = st.text_input(label="연식", placeholder="예) 2022")
with col4:
    input_mile = st.text_input(label="주행거리", placeholder="예) 58817")

# 조회 버튼
if st.button("조회하기"):
    # 기본 쿼리
    query = "SELECT * FROM car_info" 

    # 조건 리스트 및 값 리스트
    conditions = []
    values = []

    # LIKE 조건 (브랜드, 모델)
    if input_brand:
        conditions.append("brandName LIKE %s")
        values.append(f"%{input_brand}%")
    if input_model_name:
        conditions.append("modelName LIKE %s")
        values.append(f"%{input_model_name}%")

    # 일치 조건 (연식, 주행거리)
    if input_year:
        conditions.append("regYear >= %s")
        values.append(input_year)
    if input_mile:
        conditions.append("mileage >= %s")
        values.append(input_mile)

    # 조건이 있으면 WHERE 절 추가
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    try:
        cur.execute(query, tuple(values))
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        df = pd.DataFrame(rows, columns=columns)

        if df.empty:
            st.warning("일치하는 차량이 없습니다.")
        else:
            st.success(f"총 {len(df)}건의 차량이 검색되었습니다.")
            st.dataframe(df)
    except Exception as e:
        st.error(f"오류 발생: {e}")
