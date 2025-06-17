import streamlit as st


st.title("🚗 전국 중고차 정보 확인 서비스")
st.divider()
st.image("pages/images/image5.jpg", use_container_width=True)

st.divider()
st.header("🚗 나를 위한 중고차, 어디 없을까?")
st.markdown("#### 키워드 검색으로 간편하게 나만의 중고차를 찾을 수 있어요!")

st.image("pages/images/image4.jpg", use_container_width=True)

st.divider()
st.markdown("### 📌 주요 기능")
st.markdown("""
- 📊 **브랜드 분포 통계**: 등록 차량의 브랜드별 등록 현황 통계 그래프를 확인할 수 있습니다.
- 🗒️ **현재 판매중인 중고차 현황** : 데이터 프레임을 통해 등록된 모든 차량을 확인할 수 있습니다.
- 🚗 **나만의 중고차 찾기** : 키워드 검색을 통해 원하는 스펙의 중고 차량을 조회할 수 있습니다.
- ❓ **FAQ** : 중고차 구매 및 판매와 관련된 FAQ들을 확인할 수 있습니다.
""")


st.divider()
st.markdown("""
- 🔗**참고한 사이트**
- 롯데 렌터카 마이카 사이트 : https://mycarsave.lotterentacar.net/
- 엔카 사이트 매매 가이드 : http://www.encar.com/sg/sg_sellguide.do
""")