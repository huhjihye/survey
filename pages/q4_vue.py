import streamlit as st
from question_list import *

# --- 세션 초기화 ---
if "page" not in st.session_state:
    st.session_state.page = 0

scale_labels_5 = ["① 매우 그렇지 않음", "② 그렇지 않음", "③ 보통", "④ 그렇다", "⑤ 매우 그렇다"]
scale_labels_7 = [
    "① 매우 그렇지 않음", "② 그렇지 않음", "③ 약간 그렇지 않음",
    "④ 보통이다", "⑤ 약간 그렇다", "⑥ 그렇다", "⑦ 매우 그렇다"
]

# --- 각 페이지 함수 정의 ---

def page_intro():
    st.title("미경험 서비스 도입 영향 요인 연구에 대한 설문조사")
    
    with st.container():
        st.markdown(
            """
            <div style="padding: 20px; border: 2px solid #ccc; border-radius: 10px; background-color: #f9f9f9; font-size: 16px; line-height: 1.6;">
                안녕하십니까? 본 연구는 <b>미경험 분야</b>에 대한 서비스 도입을 위한 소비자의 수용 연구를 수행하고자 합니다. <br><br>
                <b>설문 응답 시간은 약 10분 정도 소요됩니다.</b><br><br>
                본 설문 응답은 익명으로 처리되며, 연구 목적 외에는 사용되지 않습니다. 감사합니다.
                <div style="text-align: right; margin-top: 40px;">
                    연구기관: 경희대학교<br>
                    연구책임자: 권오병 교수<br>
                    연구원: 박사과정 오희주<br>
                    연구원: 석사과정 강유진<br>
                    문의: obkwon@khu.ac.kr, gajng@khu.ac.kr, joank@khu.ac.kr
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    st.subheader("1. 귀하는 우주 호텔에 대해 들어보신 적이 있으십니까?")
    for idx, q in enumerate(question_list_1(), start=1):
        st.radio(f"{idx}. {q}", scale_labels_7, key=f"q1_{idx}")

    st.divider()

    st.subheader("2. 귀하는 호텔 경영에 대해 얼마나 알고 계십니까?")
    for idx, q in enumerate(question_list_2(), start=1):
        st.radio(f"{idx}. {q}", scale_labels_7, key=f"q2_{idx}")

    st.divider()

    st.subheader("3. 귀하는 우주에 대해 얼마나 알고 계십니까?")
    for idx, q in enumerate(question_list_3(), start=1):
        st.radio(f"{idx}. {q}", scale_labels_7, key=f"q3_{idx}")

    st.divider()

    col1, col2 = st.columns(2)
    with col2:
        if st.button("다음", key="next_intro"):
            st.session_state.page += 1

def page_q4():
    st.title("4. 직관 유형 측정")

    question_4_1, question_4_2, question_4_3, question_4_4 = question_list_4()

    st.subheader("4-1. HB 거시적 직관")
    for idx, q in enumerate(question_4_1, start=1):
        st.radio(f"{idx}. {q}", scale_labels_5, key=f"q4_1_{idx}")

    st.subheader("4-2. HA 거시적 추상적 직관")
    for idx, q in enumerate(question_4_2, start=1):
        st.radio(f"{idx}. {q}", scale_labels_5, key=f"q4_2_{idx}")

    st.subheader("4-3. I 추론적 직관")
    for idx, q in enumerate(question_4_3, start=1):
        st.radio(f"{idx}. {q}", scale_labels_5, key=f"q4_3_{idx}")

    st.subheader("4-4. A 감정적 직관")
    for idx, q in enumerate(question_4_4, start=1):
        st.radio(f"{idx}. {q}", scale_labels_5, key=f"q4_4_{idx}")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("이전", key="prev_q4"):
            st.session_state.page -= 1
    with col2:
        if st.button("다음", key="next_q4"):
            st.session_state.page += 1

def page_q5():
    st.markdown(
    """
    <h3 style='font-size: 1.5em; font-weight: bold; text-align: left; white-space: normal; word-break: keep-all;'>
        5. 혁신 소비 성향  
    </h3>
    """,
    unsafe_allow_html=True
    )


    st.markdown(
    """
    <div style="padding: 20px; border: 2px solid #ccc; border-radius: 10px; background-color: #f9f9f9; font-size: 16px; line-height: 1.6;">
    귀하의 혁신 성향에 대해 알아보고자 합니다.
    </div>
    """,
    unsafe_allow_html=True
    )
    
    for idx, question in enumerate(question_list_5(), start=1):
        st.radio(f"{idx}. {question}", scale_labels_5, key=f"q5{idx}")


    st.markdown(
    """
    <h3 style='font-size: 1.5em; font-weight: bold; text-align: left; white-space: normal; word-break: keep-all;'>
        다음 동영상을 시청하고 설문을 진행해주시기 바랍니다   
    </h3>
    """,
    unsafe_allow_html=True
    )
    
    video_file = open('./video/Noise_2s.mp4', 'rb')   # 파일 열기 (rb는 read binary)
    video_bytes = video_file.read()

    st.video(video_bytes)

    # 여기에 Q5 문항 출력

    col1, col2 = st.columns(2)
    with col1:
        if st.button("이전", key="prev_q5"):
            st.session_state.page -= 1
    with col2:
        if st.button("다음", key="next_q5"):
            st.session_state.page += 1

def page_q68():
    st.title("6~8번 문항")

  # --------------------------------
    # 6번 문항
    # --------------------------------
    st.subheader("6. 우주호텔 이용 의도")
    for idx, question in enumerate(question_list_6(), start=1):
        st.radio(f"{idx}. {question}", scale_labels_5, key=f"q6{idx}")
        
    
    # --------------------------------
    # 7번 문항
    # --------------------------------
    st.markdown(
        """
    <h3 style='font-size: 1.5em; font-weight: bold; text-align: left; white-space: normal; word-break: keep-all;'>
        7. 다음을 읽고 답변해주세요 
        </h3>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style="padding: 20px; border: 2px solid #ccc; border-radius: 10px; background-color: #f9f9f9; font-size: 16px; line-height: 1.6;">
        우주선을 타고 우주공간을 나가면 방사선에 강하게 노출되는 밴앨런대를 무사히 통과하는 게 불가능하다고 한다.        </div>
        """,
        unsafe_allow_html=True
    )
    
    for idx, question in enumerate(question_list_7(), start=1):
        st.radio(f"{idx}. {question}", scale_labels_5, key=f"q7{idx}")
        
        
    # --------------------------------
    # 8번 문항
    # --------------------------------
        st.markdown(
        """
    <h3 style='font-size: 1.5em; font-weight: bold; text-align: left; white-space: normal; word-break: keep-all;'>
        8. 다음도 읽고 답변해주세요 
        </h3>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style="padding: 20px; border: 2px solid #ccc; border-radius: 10px; background-color: #f9f9f9; font-size: 16px; line-height: 1.6;">
        앞의 이야기는 악성 루머에 불과하며, 밴앨런대를 통과하는 데 걸린 시간은  1시간이 채 되지 않을 뿐더러 방사선이 가장 약한 경로로 우주선이 비행할 수 있어, 전혀 인체에 문제가 없다.        """,
        unsafe_allow_html=True
    )
    
    for idx, question in enumerate(question_list_8(), start=1):
        st.radio(f"{idx}. {question}", scale_labels_5, key=f"q8{idx}")
        
    col1, col2 = st.columns(2)
    with col1:
        if st.button("이전", key="prev_q68"):
            st.session_state.page -= 1
    with col2:
        if st.button("다음", key="next_q68"):
            st.session_state.page += 1

def page_survey_info():
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
    col1, col2 = st.columns(2)
    with col1:
        if st.button("이전", key="prev_info"):
            st.session_state.page -= 1
    with col2:
        if st.button("제출", key="submit"):
            st.success("제출이 완료되었습니다. 감사합니다!")

# --- 페이지 매핑 ---
pages = [page_intro, page_q4, page_q5, page_q68, page_survey_info]

# --- 현재 페이지 출력 ---
pages[st.session_state.page]()
