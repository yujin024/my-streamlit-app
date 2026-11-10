import streamlit as st
import pandas as pd
import numpy as np

# 여기서부터 자유롭게 작성하세요

# ── 예시 구조 (지우고 새로 써도 됩니다) ────────────────

st.title("드럼 연습기록")           # ← 제목을 바꾸세요
st.caption("10강 실습 과제")

# [텍스트]
st.header("소개")
st.write("이 대시보드는 주별 총 연습시간과 곡별 연습시간에 관한 내용입니다.")  # ← 내용을 채우세요

# [데이터]
st.header("연습시간 데이터")
data = {
    "날짜": [
        "2026-10-16",
        "2026-10-17",
        "2026-10-23",
        "2026-10-24",
        "2026-10-27",
        "2026-10-28",
        "2026-10-30",
        "2026-11-02",
        "2026-11-05",
        "2026-11-06"
        ],        # ← 실제 데이터로 바꾸세요
    "곡A": [40, 20, 30, 50, 30, 40, 40, 10, 20, 40],
    "곡B": [10, 30, 30, 20, 10, 20, 30, 50, 20, 10],
    "곡C": [40, 40, 30, 20, 50, 30, 20, 30, 50, 40]
} 
df = pd.DataFrame(data)
df["날짜"] = pd.to_datetime(df["날짜"])
df["총연습시간"] = df[["곡A", "곡B", "곡C"]].sum(axis=1)
st.dataframe(
    df.style.format({"날짜": lambda x: x.strftime("%Y-%m-%d")})
)

# [주별 총 연습시간]
st.header("주별 총 연습시간")
df["주"] = (
    df["날짜"]
    .dt.to_period("W-SUN")
    .apply(lambda x: x.start_time)
)

weekly = df.groupby("주")["총연습시간"].sum()
st.bar_chart(weekly)

# [곡별 총 연습시간]
st.header("곡별 총 연습시간")
song_total = df[["곡A", "곡B", "곡C"]].sum()
st.bar_chart(song_total)

# [위젯 + 위젯-화면 연동]
st.header("곡별 연습 기록")
선택곡 = st.radio("확인할 곡을 선택하세요", ["곡A", "곡B", "곡C"])   # ← 위젯 추가
선택곡총시간 = df[선택곡].sum()
st.metric(
    label=f"{선택곡} 총 연습시간",
    value=f"{선택곡총시간} 분"
)                    # ← 위젯 값에 따라 화면 변경
