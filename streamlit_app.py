import streamlit as st
import pandas as pd
import numpy as np

# ── 여기서부터 자유롭게 수정하세요 ───────────────

st.title("나의 첫 번째 Streamlit 앱")   # ← 제목을 바꿔보세요

# ── 사이드바 ──────────────────────────────────
st.sidebar.title("설정")

chart_type = st.sidebar.radio(
    "차트 유형",
    ["꺾은선 그래프", "막대 그래프", "면적 그래프"]   # ← 유형을 바꿔보세요
)

n = st.sidebar.slider(
    "데이터 개수",
    min_value=10,    # ← 최솟값을 바꿔보세요
    max_value=100,   # ← 최댓값을 바꿔보세요
    value=30
)

# ── 메인 화면 ─────────────────────────────────
st.write("차트 유형과 데이터 개수를 선택해 시각화 결과를 확인해보세요")   # ← 설명을 바꿔보세요

data = pd.DataFrame(
    np.random.randn(n, 3),
    columns=['A', 'B', 'C']   # ← 컬럼 이름을 바꿔보세요
)

if chart_type == "꺾은선 그래프":
    st.line_chart(data)
elif chart_type == "막대 그래프":
    st.bar_chart(data)
else:
    st.area_chart(data)

st.dataframe(data.head(5))

# ── 여기까지 ──────────────────────────────────
