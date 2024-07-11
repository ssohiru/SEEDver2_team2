import streamlit as st
import pandas as pd

def standard_function(subject_selection, category_selection, grade_selection):
    # Load the provided Excel file
    file_path = 'data/2022_특수교육교육과정(기본+공통)_성취기준_목록.xlsx'

    try:
        # Load the Excel file from the specified path
        excel_data = pd.ExcelFile(file_path)

        # Get sheet names excluding '안내'
        sheet_names = [name for name in excel_data.sheet_names if name != '안내']

        # Load and display the "과목이름2" (성취기준)
        sheet_name2 = f'{subject_selection}2'
        if sheet_name2 in sheet_names:
            sheet_data2 = pd.read_excel(file_path, sheet_name=sheet_name2).dropna(how='all').fillna('')
            
            # Filter data based on selections
            filtered_data = sheet_data2[(sheet_data2['구분'] == category_selection) & (sheet_data2['학년군'] == grade_selection)]
            st.dataframe(filtered_data)
    except FileNotFoundError:
        st.error(f"파일을 찾을 수 없습니다: {file_path}")

def seed_function():
    # 세션 상태 초기화
    if 'step' not in st.session_state:
        st.session_state.step = 0

    if 'formatted_text' not in st.session_state:
        st.session_state.formatted_text = ""

    # 사이드바 설정
    st.sidebar.title("2022 교사교육과정 및 학급교육과정 개발 도우미")
    st.sidebar.markdown("by. SEED")

    # 메인 페이지 제목
    st.title("2022 교사교육과정 및 학급교육과정 개발 도우미")

    if st.session_state.step == 0:
        st.subheader("1. 시작 (Start)")
        st.write('과목, 교육과정, 학년군을 선택해주세요.')

        # 교과 선택 옵션
        subjects = [
            '국어', '수학', '영어', '과학', '사회', '음악', 
            '미술', '체육', '도덕', '기술', '가정', '정보'
        ]

        # 사용자 입력 폼
        with st.form(key='start_form'):
            subject = st.selectbox('과목을 선택하세요:', subjects)
            category_selection = st.selectbox('교육과정을 선택하세요:', ['기본', '공통'])
            grade_selection = st.selectbox('학년군을 선택하세요:', ['초1~2','초3~4','초5~6','중1~3','고1~3'])
            submit_button = st.form_submit_button(label='Submit')

        # 제출 후 처리
        if submit_button:
            st.session_state.subject = subject
            st.session_state.category_selection = category_selection
            st.session_state.grade_selection = grade_selection
            st.session_state.step = 1

    if st.session_state.step == 1:
        st.subheader("2. 성취기준 검색 (Search Achievement Standards)")
        st.write('선택한 과목, 교육과정, 학년군의 성취기준을 검색하세요.')
        
        # 성취기준 검색 기능
        standard_function(st.session_state.subject, st.session_state.category_selection, st.session_state.grade_selection)

        st.subheader("3. 추가 정보 입력 (Additional Information)")
        st.write('수업에 참여하는 학생들의 추가 정보를 입력하세요.')

        # 장애 유형 목록
        disability_options = [
            '지적 장애', '지체 장애', '시각 장애', '청각 장애', '정서 및 행동 장애', 
            '자폐성 장애', '의사소통 장애', '학습 장애', '건강 장애', 
            '발달 지체', '뇌병변 장애', '간질 장애', '기타 장애'
        ]

        with st.form(key='additional_info_form'):
            disability_type = st.multiselect('수업에 참여하는 학생들의 장애 유형 (최대 3가지)', disability_options, max_selections=3)
            subject_level = st.text_input('교과와 관련한 현재 학습 수행 수준')
            student_response = st.text_input('학생들의 반응 양식 및 표현 양식, 언어 유창성')
            core_concept = st.text_input('교사가 선정한 수업할 핵심개념 또는 핵심개념을 추출할 교육과정 핵심아이디어의 문장')
            achievement_standard = st.text_input('수업할 부분의 관련한 성취기준(코드까지)')
            content_category = st.text_input('수업할 부분의 교육과정 내용체계의 범주(ex: 지식&이해, 과정&기능, 가치&태도)')
            submit_button = st.form_submit_button(label='Submit')

        # 제출 후 처리
        if submit_button:
            formatted_text = f"""
            과목: {st.session_state.subject}
            교육과정: {st.session_state.category_selection}
            학년군: {st.session_state.grade_selection}
            장애 유형: {', '.join(disability_type)}
            현재 학습 수행 수준: {subject_level}
            학생들의 반응 양식 및 표현 양식, 언어 유창성: {student_response}
            교사가 선정한 핵심개념: {core_concept}
            성취기준: {achievement_standard}
            교육과정 내용체계의 범주: {content_category}
            """

            st.session_state.formatted_text = formatted_text

    if st.session_state.formatted_text:
        st.subheader("입력된 정보")
        st.text_area("다음 텍스트를 복사하여 챗봇에 입력하세요:", st.session_state.formatted_text, height=200)
        
        # 복사하기 버튼
        st.write("생성된 텍스트를 Ctrl+C 키로 복사해 다음 페이지로 이동하세요.")

        # 챗봇 URL 제공
        st.markdown("[ChatGPT 챗봇으로 이동](https://chatgpt.com/g/g-u4h9tW1bd-gaenyeomgiban-gyoyuggwajeong-seolgye-dijaineo-caesbos-feat-edyutekeu-beojeon2-teugsugyoyugyong)")

# 앱 실행
seed_function()
