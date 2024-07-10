import streamlit as st
st.set_page_config(page_title="2022 교사교육과정 및 학급교육과정 개발 도우미", layout="wide")

import standard
import SEED8_ver2

st.write(dir(SEED8_ver2))

def main():
    st.sidebar.title("SEED가 준비한 도움들😄")
    menu = ["도움 설명서", "성취기준 검색기", "교사교육과정 및 학급교육과정 개발 도우미"]
    choice = st.sidebar.selectbox("1조의 2가지 선물🎁", menu)

    if choice == "도움 설명서":
        st.subheader("도움 설명서")
        st.write("""
        이 웹 애플리케이션은 2022 교사교육과정 및 학급교육과정 개발 도우미와 성취기준 검색기를 제공합니다.
        
        사이드바에서 원하는 기능을 선택하세요:
        - **성취기준 검색기**: 2022 개정 교육과정 성취기준을 검색할 수 있는 기능을 제공합니다.
        - **교사교육과정 및 학급교육과정 개발 도우미**: 2022 개정 교육과정의 교사교육과정과 학급교육과정을 짤 때 드는 막막함을 도와줍니다.
        """)

    elif choice == "성취기준 검색기":
        standard.standard_function()
    
    elif choice == "교사교육과정 및 학급교육과정 개발 도우미":
        SEED8_ver2.search_function()

if __name__ == '__main__':
    main()



