import streamlit as st
from streamlit.components.v1 import html
from question_list import *  # 너가 만든 질문 리스트 불러오는 파일

# --- 세션 초기화 ---
if "page" not in st.session_state:
    st.session_state.page = 0

# --- 척도 옵션 ---
scale_labels_5 = ["① 매우 그렇지 않음", "② 그렇지 않음", "③ 보통", "④ 그렇다", "⑤ 매우 그렇다"]
scale_labels_7 = ["① 매우 그렇지 않음", "② 그렇지 않음", "③ 약간 그렇지 않음", "④ 보통이다", "⑤ 약간 그렇다", "⑥ 그렇다", "⑦ 매우 그렇다"]


def force_scroll_to_top():
    html("""
        <script>
            const section = window.parent.document.querySelector('section.main');
            if (section) {
                section.scrollTo({top: 0, behavior: 'instant'});
            }
        </script>
    """, height=0)


# --- 페이지 함수들 ---

def page_intro():
    force_scroll_to_top()
    st.markdown(
        """
        <h1 style='white-space: nowrap; font-size: 2.0em; font-weight: bold; text-align:center'>
            미경험 서비스 도입 영향 요인<br>
            연구에 대한 설문조사
        </h1>
        """,
        unsafe_allow_html=True
    )
    with st.container():
        st.markdown(
            """
            <div style="padding: 20px; border: 2px solid #ccc; border-radius: 10px; background-color: #f9f9f9; font-size: 16px; line-height: 1.6;">
                안녕하십니까? 본 연구는 <b>미경험 분야</b>에 대한 서비스 도입을 위한 소비자의 수용 연구를 수행하고자 합니다. <br><br>
                <b>설문 응답 시간은 약 10분 정도 소요로 예상합니다.</b><br><br>
                본 설문 응답 내용은 오로지 학술적 목적으로만 사용하고자 하며, 설문 문항의 저작권은 연구기관에 있으므로 무단 복사 및 배포를 금합니다. 설문에 참여해 주셔서 감사합니다.
                <div style="text-align: right; margin-top: 40px;">
                    연구기관: 경희대학교<br>
                    연구책임자: 권오병 교수<br>
                    연구원: 박사과정 오현주<br>
                    연구원: 석사과정 강유진<br>
                    문의: obkwon@khu.ac.kr, gajng@khu.ac.kr, joank@khu.ac.kr
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    st.markdown("<p> </p>", unsafe_allow_html=True)

    st.markdown("""
    <h4 style="font-size: 1.5em; font-weight: bold; margin-bottom: 0.5em;">
    1. 귀하는 우주 호텔에 대해 들어보신 적이 있으십니까?
    </h4>
    """, unsafe_allow_html=True)
    
    for idx, q in enumerate(question_list_1(), start=1):
        st.markdown(
            f"""
            <h4 style="font-size: 1.0em; font-weight: bold; margin-bottom: 0.2em; margin-top: 0.5em;">
                {q}
            </h4>
            """,
            unsafe_allow_html=True
        )
        st.radio(
            label="",
            options=scale_labels_7,
            key=f"q1_{idx}",
            label_visibility="collapsed"
        )
    
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("""
    <h4 style="font-size: 1.5em; font-weight: bold; margin-bottom: 0.5em;">
    2. 귀하는 호텔 경영에 대해 얼마나 알고 계십니까?
    </h4>
    """, unsafe_allow_html=True)
    
    for idx, q in enumerate(question_list_2(), start=1):
        st.markdown(
            f"""
            <h4 style="font-size: 1.0em; font-weight: bold; margin-bottom: 0.2em; margin-top: 0.5em;">
                {q}
            </h4>
            """,
            unsafe_allow_html=True
        )
        st.radio(
            label="",
            options=scale_labels_7,
            key=f"q2_{idx}",
            label_visibility="collapsed"
        )
        
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown("""
    <h4 style="font-size: 1.5em; font-weight: bold; margin-bottom: 0.5em;">
    3. 귀하는 우주에 대해 얼마나 알고 계십니까?
    </h4>
    """, unsafe_allow_html=True)
    
    for idx, q in enumerate(question_list_3(), start=1):
        st.markdown(
            f"""
            <h4 style="font-size: 1.0em; font-weight: bold; margin-bottom: 0.2em; margin-top: 0.5em;">
                {q}
            </h4>
            """,
            unsafe_allow_html=True
        )
        st.radio(
            label="",
            options=scale_labels_7,
            key=f"q3_{idx}",
            label_visibility="collapsed"
        )
    
    st.markdown("<hr>", unsafe_allow_html=True)

    nav_buttons()

def page_q4():
    force_scroll_to_top()
    st.markdown(
        """
        <h1 style='white-space: nowrap; font-size: 1.5em; font-weight: bold; text-align:center'>
           4.직관의 유형 측정
        </h1>
        """,
        unsafe_allow_html=True
    )    
    with st.container():
        st.markdown("""
            <div style="padding:20px; border:2px solid #ccc; border-radius:10px;
                        background:#f9f9f9; font-size:16px; line-height:1.6;">
                귀하의 직관 유형에 대해 알아보고자 합니다.
            </div>
        """, unsafe_allow_html=True)
    

    q4_1, q4_2, q4_3, q4_4 = question_list_4()
    
    st.markdown("<p> </p>", unsafe_allow_html=True)

    st.markdown("""
    <h4 style="font-size: 1.5em; font-weight: bold; margin-bottom: 0.5em;">
    4-1. HB 거시적 직관 (Holistic-Big Picture) 측정
    </h4>
    """, unsafe_allow_html=True)
    
    for idx, q in enumerate(q4_1, start=1):
        st.markdown(
            f"""
            <h4 style="font-size: 1.0em; font-weight: bold; margin-bottom: 0.2em; margin-top: 0.5em;">
                {q}
            </h4>
            """,
            unsafe_allow_html=True
        )
        st.radio(
            label="",
            options=scale_labels_5,
            key=f"q4_1_{idx}",
            label_visibility="collapsed"
        )
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown("""
    <h4 style="font-size: 1.5em; font-weight: bold; margin-bottom: 0.5em;">
    4-2. HA 거시적 추상적 직관 (Holistic- Abstract) 측정
    </h4>
    """, unsafe_allow_html=True)
    
    for idx, q in enumerate(q4_2, start=1):
        st.markdown(
            f"""
            <h4 style="font-size: 1.0em; font-weight: bold; margin-bottom: 0.2em; margin-top: 0.5em;">
                {q}
            </h4>
            """,
            unsafe_allow_html=True
        )
        st.radio(
            label="",
            options=scale_labels_5,
            key=f"q4_2_{idx}",
            label_visibility="collapsed"
        )
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown("""
    <h4 style="font-size: 1.5em; font-weight: bold; margin-bottom: 0.5em;">
    4-3. I 추론적 직관 (Inferential) 측정
    </h4>
    """, unsafe_allow_html=True)
    
    for idx, q in enumerate(q4_3, start=1):
        st.markdown(
            f"""
            <h4 style="font-size: 1.0em; font-weight: bold; margin-bottom: 0.2em; margin-top: 0.5em;">
                {q}
            </h4>
            """,
            unsafe_allow_html=True
        )
        st.radio(
            label="",
            options=scale_labels_5,
            key=f"q4_3_{idx}",
            label_visibility="collapsed"
        )
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    
    st.markdown("""
    <h4 style="font-size: 1.5em; font-weight: bold; margin-bottom: 0.5em;">
    4-4. A 감정적 직관 (Affective) 측정
    </h4>
    """, unsafe_allow_html=True)
    
    for idx, q in enumerate(q4_4, start=1):
        st.markdown(
            f"""
            <h4 style="font-size: 1.0em; font-weight: bold; margin-bottom: 0.2em; margin-top: 0.5em;">
                {q}
            </h4>
            """,
            unsafe_allow_html=True
        )
        st.radio(
            label="",
            options=scale_labels_5,
            key=f"q4_4_{idx}",
            label_visibility="collapsed"
        )
    
    st.markdown("<hr>", unsafe_allow_html=True)

   
    nav_buttons()

def page_q5():
    force_scroll_to_top()
    st.markdown(
        """
        <h1 style='white-space: nowrap; font-size: 1.5em; font-weight: bold; text-align:center'>
           5. 혁신 소비 성향
        </h1>
        """,
        unsafe_allow_html=True
    )    
    with st.container():
        st.markdown("""
            <div style="padding:20px; border:2px solid #ccc; border-radius:10px;
                        background:#f9f9f9; font-size:16px; line-height:1.6;">
            귀하의 혁신 성향에 대해 알아보고자 합니다.
            </div>
        """, unsafe_allow_html=True)
        
    for idx, q in enumerate(question_list_5(), start=1):
        st.markdown(
            f"""
            <h4 style="font-size: 1.0em; font-weight: bold; margin-bottom: 0.2em; margin-top: 0.5em;">
                {q}
            </h4>
            """,
            unsafe_allow_html=True
        )
        st.radio(
            label="",
            options=scale_labels_5,
            key=f"q5_{idx}",
            label_visibility="collapsed"
        )
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <h1 style='white-space: nowrap; font-size: 1.5em; font-weight: bold; text-align:center'>
           다음 동영상을 시청하고 설문을 진행해 주세요.
        </h1>
        """,
        unsafe_allow_html=True
    )   

    with open('./video/Noise_2s.mp4', 'rb') as f:
        st.video(f.read())
        
    st.markdown("<hr>", unsafe_allow_html=True)

    nav_buttons()

def page_q68():
    force_scroll_to_top()
    
    st.markdown("""
    <h4 style="font-size: 1.5em; font-weight: bold; margin-bottom: 0.5em;">
    6. 우주호텔 이용 의도
    </h4>
    """, unsafe_allow_html=True)
    
    for idx, q in enumerate(question_list_6(), start=1):
        st.markdown(
            f"""
            <h4 style="font-size: 1.0em; font-weight: bold; margin-bottom: 0.2em; margin-top: 0.5em;">
                {q}
            </h4>
            """,
            unsafe_allow_html=True
        )
        st.radio(
            label="",
            options=scale_labels_5,
            key=f"q6_{idx}",
            label_visibility="collapsed"
        )
    
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("""
    <h4 style="font-size: 1.5em; font-weight: bold; margin-bottom: 0.5em;">
    7. 다음을 읽고 답변해주세요 
    </h4>
    """, unsafe_allow_html=True)
    with st.container():
        st.markdown("""
            <div style="padding:20px; border:2px solid #ccc; border-radius:10px;
                        background:#f9f9f9; font-size:16px; line-height:1.6;">            
            우주선을 타고 우주공간을 나가면 방사선에 강하게 노출되는<br>
            밴앨런대를 무사히 통과하는 게 불가능하다고 한다.
            </div>
        """, unsafe_allow_html=True)
        
    for idx, q in enumerate(question_list_7(), start=1):
        st.markdown(
            f"""
            <h4 style="font-size: 1.0em; font-weight: bold; margin-bottom: 0.2em; margin-top: 0.5em;">
                {q}
            </h4>
            """,
            unsafe_allow_html=True
        )
        st.radio(
            label="",
            options=scale_labels_5,
            key=f"q7_{idx}",
            label_visibility="collapsed"
        )
        
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("""
    <h4 style="font-size: 1.5em; font-weight: bold; margin-bottom: 0.5em;">
    8. 다음을 읽고 답변해주세요 
    </h4>
    """, unsafe_allow_html=True)
    with st.container():
        st.markdown("""
            <div style="padding:20px; border:2px solid #ccc; border-radius:10px;
                        background:#f9f9f9; font-size:16px; line-height:1.6;">            
            앞의 이야기는 악성 루머에 불과하며, 밴앨런대를 통과하는 데 걸린 시간은  1시간이 채 되지 않을 뿐더러<br> 
            방사선이 가장 약한 경로로 우주선이 비행할 수 있어, 전혀 인체에 문제가 없다.
            </div>
        """, unsafe_allow_html=True)
        
    for idx, q in enumerate(question_list_8(), start=1):
        st.markdown(
            f"""
            <h4 style="font-size: 1.0em; font-weight: bold; margin-bottom: 0.2em; margin-top: 0.5em;">
                {q}
            </h4>
            """,
            unsafe_allow_html=True
        )
        st.radio(
            label="",
            options=scale_labels_5,
            key=f"q8_{idx}",
            label_visibility="collapsed"
        )
        
        st.markdown("<hr>", unsafe_allow_html=True)



    nav_buttons()

def page_survey_info():
    force_scroll_to_top()
    
    st.markdown(
        """
        <h1 style='white-space: nowrap; font-size: 2.0em; font-weight: bold; text-align:center'>
            다음은 통계 처리를 위한 일반적 사항입니다.
        </h1>
        """,
        unsafe_allow_html=True
    )
    with st.container():
        st.markdown(
            """
            <div style="padding: 20px; border: 2px solid #ccc; border-radius: 10px; background-color: #f9f9f9; font-size: 16px; line-height: 1.6;">
                   <b>개인정보 수집 및 이용에 대한 안내</b><br><br>
                    본 설문조사는 연구 목적으로만 사용되며, 수집된 모든 개인정보는 철저히 보호됩니다.<br><br>
                    - 수집 항목: 나이, 성별, 전공 분야, 최종 학력, 직업, 월평균 소득<br>
                    - 수집 목적: 연구 결과의 통계적 분석 및 연구 자료 작성<br>
                    - 보관 기간: 연구 종료 후 즉시 파기<br><br>
                    본 설문에 응답함으로써 개인정보 수집 및 이용에 동의하는 것으로 간주합니다.<br>
                    응답 내용은 익명으로 처리되며, 연구 목적 외에는 절대 사용되지 않습니다.<br><br>
                    감사합니다.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
   
    st.markdown("<p> </p>", unsafe_allow_html=True)
    
    # --- 개인정보 입력 폼 ---

      # 만 나이
    st.markdown("""
    <h4 style="font-size: 1.2em; font-weight: bold; margin-top: 1em; margin-bottom: 0.3em;">
    만 나이를 입력해주세요
    </h4>
    """, unsafe_allow_html=True)
    st.number_input(
        label="만 나이를 입력해주세요",
        min_value=0,
        max_value=100,
        step=1,
        key="age",
        label_visibility="collapsed"
    )

    # 성별
    st.markdown("""
    <h4 style="font-size: 1.2em; font-weight: bold; margin-top: 1em; margin-bottom: 0.3em;">
    성별을 선택하세요
    </h4>
    """, unsafe_allow_html=True)
    st.radio(
        label="성별",
        options=["① 남자", "② 여자"],
        horizontal=True,
        key="gender",
        label_visibility="collapsed"
    )

    # 전공 분야
    st.markdown("""
    <h4 style="font-size: 1.2em; font-weight: bold; margin-top: 1em; margin-bottom: 0.3em;">
    전공 분야를 선택하세요
    </h4>
    """, unsafe_allow_html=True)
    st.radio(
        label="전공 분야",
        options=["① 항공우주", "② 호텔/경영", "③ 자연과학", "④ 기타"],
        key="major",
        label_visibility="collapsed"
    )

    # 최종 학력
    st.markdown("""
    <h4 style="font-size: 1.2em; font-weight: bold; margin-top: 1em; margin-bottom: 0.3em;">
    최종 학력을 선택하세요
    </h4>
    """, unsafe_allow_html=True)
    st.radio(
        label="최종 학력",
        options=["① 고등학교", "② 대학교 재학", "③ 대학교 졸업", "④ 대학원 이상"],
        key="education",
        label_visibility="collapsed"
    )

    # 직업
    st.markdown("""
    <h4 style="font-size: 1.2em; font-weight: bold; margin-top: 1em; margin-bottom: 0.3em;">
    직업을 선택하세요
    </h4>
    """, unsafe_allow_html=True)
    st.radio(
        label="직업",
        options=["① 학생", "② 회사원", "③ 전문직", "④ 주부", "⑤ 무직"],
        key="job",
        label_visibility="collapsed"
    )

    # 월평균 소득
    st.markdown("""
    <h4 style="font-size: 1.2em; font-weight: bold; margin-top: 1em; margin-bottom: 0.3em;">
    월평균 소득을 선택하세요
    </h4>
    """, unsafe_allow_html=True)
    st.radio(
        label="월평균 소득",
        options=["① 200만원 미만", "② 200~400만원", "③ 400~600만원", "④ 600~800만원", "⑤ 800만원 이상"],
        key="income",
        label_visibility="collapsed"
    )
    col1, col2 = st.columns(2)
    with col1:
        if st.button("이전"):
            st.session_state.page = max(st.session_state.page - 1, 0)

    with col2:
        if st.button("제출"):
            st.success("제출이 완료되었습니다! 감사합니다.")
            st.session_state.page = 0

# --- 페이지 이동 관리 ---
def nav_buttons():
    col1, col2 = st.columns(2)
    move = None

    with col1:
        if st.button("이전"):
            move = "prev"
    with col2:
        if st.session_state.page == len(pages) - 1:
            if st.button("제출"):
                st.success("제출이 완료되었습니다! 감사합니다.")
                st.session_state.page = 0
                st.session_state.scroll_to_top = True
                st.rerun()
        else:
            if st.button("다음"):
                move = "next"

    # 버튼 클릭 후 이동 처리
    if move == "prev":
        st.session_state.page = max(st.session_state.page - 1, 0)
        st.session_state.scroll_to_top = True
        st.rerun()
    elif move == "next":
        st.session_state.page = min(st.session_state.page + 1, len(pages) - 1)
        st.session_state.scroll_to_top = True
        st.rerun()

# --- 페이지 실행 ---
pages = [page_intro, page_q4, page_q5, page_q68, page_survey_info]

#  이동 직후 강제 스크롤
if st.session_state.get("scroll_to_top", False):
    force_scroll_to_top()
    st.session_state.scroll_to_top = False  # 초기화

pages[st.session_state.page]()
