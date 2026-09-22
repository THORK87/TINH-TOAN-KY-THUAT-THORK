import streamlit as st
import numpy as np
import pandas as pd
import math

# 1. BẮT BUỘC LÀ LỆNH STREAMLIT ĐẦU TIÊN
st.set_page_config(
    page_title="HỆ THỐNG TÍNH TOÁN KỸ THUẬT THORK 2026", 
    layout="wide", 
    page_icon="⚙️"
)

# 2. SAU ĐÓ MỚI ĐẾN ĐOẠN CSS CĂN CHỈNH
st.markdown("""
<style>
    /* Chống mất ô nhập liệu phía trên */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
    }

    /* Tinh chỉnh thẻ KPI Metric */
    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-top: 4px solid #1d4ed8;
        border-radius: 8px;
        padding: 14px 10px;
        text-align: center !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    }
    div[data-testid="stMetricLabel"] > div {
        justify-content: center !important;
        color: #475569 !important;
        font-weight: 700 !important;
    }
    div[data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace !important;
        color: #0f172a !important;
    }
    div[data-testid="stMetricDelta"] {
        justify-content: center !important;
        margin-top: 4px !important;
    }
    div[data-testid="stMetricDelta"] svg {
        display: none !important;
    }

    /* Banner thông số xuất xưởng */
    .spec-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        color: #ffffff;
        border-radius: 8px;
        padding: 16px 20px;
        margin-top: 24px !important;
        text-align: center;
        border: 1px solid #3b82f6;
    }
</style>
""", unsafe_allow_html=True)
