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

# --------------------------------
# 척도 옵션
# --------------------------------
scale_labels_5 = ["① 매우 그렇지 않음", "② 그렇지 않음", "③ 보통", "④ 그렇다", "⑤ 매우 그렇다"]


def page_q68(): 
    
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
        
    
    # --- 이전 / 다음 버튼 ---
    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.page > 0:
            if st.button("이전", key="prev_button_q68"):
                st.session_state.page -= 1
                scroll_to_top() 
                st.rerun()

    with col2:
        if st.session_state.page < 4:
            if st.button("다음", key="next_button_q68"):
                st.session_state.page += 1
                scroll_to_top() 
                st.rerun()
                