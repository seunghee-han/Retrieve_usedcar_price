import pandas as pd
import streamlit as st
from search_car import search_car,car_info
st.title('중고차 차량등록 정보')
st.header("차량 시세 조회")

col1, col2, col3,  = st.columns(3)

with col1:
    brandName = st.text_input(label='브랜드명 입력해주세요',
                           placeholder="예) 현대")
with col2:
    year =  st.text_input(label="최소 연식 입력해주세요",
                           placeholder="예) 2022")
with col3:
    km = st.text_input(label="최소 주행거리(km) 입력해주세요",
                           placeholder="예) 50000")
if st.button("조회"):
    rt = search_car(brandName, int(year), int(km))
    st.write(rt)
    
