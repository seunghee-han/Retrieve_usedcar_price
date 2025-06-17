import pandas as pd
import streamlit as st
import pymysql



conn = pymysql.connect(host="192.168.0.22", user='team_4', passwd='123', database='sk15_4team', port=3306)
cur = conn.cursor()

st.title("🗒️중고 차량 정보")
query = "SELECT * FROM vehicle_info"
cur.execute(query)
data = cur.fetchall()

df = pd.DataFrame(data)

# # 열 이름 알아보기 쉽게 수정
df.columns = ['이미지','기업명', '모델명', '등록 연도','주행거리','신차 가격','등록 가격']
column_config = {

    "이미지": st.column_config.ImageColumn()


}
st.dataframe(df,column_config=column_config, use_container_width=True)


# st.write(df)
