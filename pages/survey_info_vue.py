import streamlit as st
from question_list import question_list_6, question_list_7, question_list_8

def scroll_to_top():
    st.markdown(
        """
        <script>
            window.scrollTo(0, 0);
        </script>
        """,
        unsafe_allow_html=True
    )


def survey_info():
    st.title("최종 개인정보 입력")

    # 1) 이름 / 나이
    age = st.number_input("만 나이를 입력해주세요.", min_value=0, max_value=100, step=1)

    st.divider()

    # 2) 성별
    st.subheader("2) 성별")
    gender = st.radio(
        "성별을 선택하세요.",
        ["① 남자", "② 여자"],
        horizontal=True,
        key="gender"
    )

    st.divider()

    # 3) 전공 유사 분야
    st.subheader("3) 다음 중 귀하의 전공과 가장 유사한 것은?")
    major = st.radio(
        "전공 분야를 선택하세요.",
        ["① 항공우주 분야", "② 호텔 또는 경영 분야", "③ 우주 등 자연과학 분야", "④ 기타"],
        key="major"
    )

    st.divider()

    # 4) 최종학력
    st.subheader("4) 최종학력")
    education = st.radio(
        "최종 학력을 선택하세요.",
        ["① 고등학교 졸업", "② 대학교 재학", "③ 대학교 졸업", "④ 대학원 재학이상"],
        key="education"
    )

    st.divider()

    # 5) 직업
    st.subheader("5) 직업")
    job = st.radio(
        "현재 직업을 선택하세요.",
        ["① 학생", "② 회사원", "③ 전문직", "④ 주부", "⑤ 무직"],
        key="job"
    )

    st.divider()

    # 6) 월평균 소득
    st.subheader("6) 월평균 소득")
    income = st.radio(
        "월평균 소득을 선택하세요.",
        [
            "① 200만원 미만",
            "② 200~400만원 미만",
            "③ 400~600만원 미만",
            "④ 600~800만원 미만",
            "⑤ 800만원 이상"
        ],
        key="income"
    )

    st.divider()

    


    # --- 이전 / 제출 버튼 ---
    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.page > 0:
            if st.button("이전", key="prev_button_survey_info"):
                st.session_state.page -= 1
                scroll_to_top() 
                st.rerun()

    with col2:
        if st.button("제출", key="submit_button"):
            st.success("제출이 완료되었습니다! 감사합니다.")
            scroll_to_top() 
            st.session_state.page = 0  # 홈으로 이동