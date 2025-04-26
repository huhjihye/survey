import streamlit as st
from question_list import question_list_5

def scroll_to_top():
    st.markdown(
        """
        <script>
            window.scrollTo(0, 0);
        </script>
        """,
        unsafe_allow_html=True
    )


# --------------------------------
# 척도 옵션
# --------------------------------
scale_labels_5 = ["① 매우 그렇지 않음", "② 그렇지 않음", "③ 보통", "④ 그렇다", "⑤ 매우 그렇다"]


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
    
    # --- 이전 / 다음 버튼 ---
    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.page > 0:
            if st.button("이전", key="prev_button_q5"):
                st.session_state.page -= 1
                scroll_to_top() 
                st.rerun()

    with col2:
        if st.session_state.page < 4:
            if st.button("다음", key="next_button_q5"):
                st.session_state.page += 1
                scroll_to_top() 
                st.rerun()
      
        
