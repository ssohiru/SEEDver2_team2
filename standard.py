import streamlit as st
import pandas as pd

# 엑셀 파일 불러오기
xls = pd.ExcelFile('2022_특수교육교육과정(기본+공통)_성취기준_목록.xlsx')

# 과목별 시트 리스트
subject_sheets = {
    '바슬즐': '바슬즐',
    '국어': '국어',
    '사회': '사회',
    '수학': '수학',
    '과학': '과학',
    '실과': '실과',
    '체육': '체육',
    '음악': '음악',
    '미술': '미술',
    '외국어': '외국어',
    '도덕': '도덕',
    '진로와 직업': '진로와 직업',
    '정보': '정보',
    '보건': '보건',
    '기술과 가정': '기술과 가정',
    '한문': '한문',
    '환경': '환경',
    '선택중심교육과정': '선택중심교육과정',
}

# 과목 탭 생성
subject = st.sidebar.selectbox('과목을 선택하세요', list(subject_sheets.keys()))

# 선택한 과목에 맞는 데이터프레임 불러오기
df = pd.read_excel(xls, sheet_name=subject_sheets[subject])

# '바슬즐'의 경우 교과 선택이 필요함
if subject == '바슬즐':
    교과 = st.selectbox('교과를 선택하세요', df['교과'].unique())
    영역 = st.selectbox('영역을 선택하세요', df['영역'].unique())
    filtered_df = df[(df['교과'] == 교과) & (df['영역'] == 영역)]
    
# '선택중심교육과정'의 경우 추가로 분야 선택이 필요함
elif subject == '선택중심교육과정':
    구분 = st.selectbox('구분을 선택하세요', df['구분'].unique())
    학년군 = st.selectbox('학년군을 선택하세요', df['학년군'].unique())
    분야 = st.selectbox('분야를 선택하세요', df['분야'].unique())
    영역 = st.selectbox('영역을 선택하세요', df['영역'].unique())
    
    filtered_df = df[(df['구분'] == 구분) & (df['학년군'] == 학년군) & 
                     (df['분야'] == 분야) & (df['영역'] == 영역)]
                     
# '수학'의 경우 내용 열도 포함
elif subject == '수학':
    구분 = st.selectbox('구분을 선택하세요', df['구분'].unique())
    학년군 = st.selectbox('학년군을 선택하세요', df['학년군'].unique())
    영역 = st.selectbox('영역을 선택하세요', df['영역'].unique())
    
    filtered_df = df[(df['구분'] == 구분) & (df['학년군'] == 학년군) & (df['영역'] == 영역)]
    
    if '내용' in df.columns:
        st.write('### 내용')
        st.write(filtered_df[['내용']])
    
# 나머지 과목
else:
    구분 = st.selectbox('구분을 선택하세요', df['구분'].unique())
    학년군 = st.selectbox('학년군을 선택하세요', df['학년군'].unique())
    
    if '영역' in df.columns:
        영역 = st.selectbox('영역을 선택하세요', df['영역'].unique())
        filtered_df = df[(df['구분'] == 구분) & (df['학년군'] == 학년군) & (df['영역'] == 영역)]
    else:
        filtered_df = df[(df['구분'] == 구분) & (df['학년군'] == 학년군)]

# 필터링된 결과 표시
st.write('### 검색 결과')
st.write(filtered_df[['분류번호', '성취기준']])

# '내용' 열이 있는 경우 내용도 출력
if '내용' in df.columns and not df['내용'].isna().all():
    st.write('### 내용')
    st.write(filtered_df[['내용']])


