import streamlit as st
import numpy as np
import pandas as pd
import math

# ==============================================================================
# CẤU HÌNH TRANG & DESIGN SYSTEM CĂN GIỮA ĐỐI XỨNG
# ==============================================================================
st.set_page_config(
    page_title="THORK 2026 | Technical Engineering Suite",
    layout="wide",
    page_icon="⚙️"
)

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.block-container {
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
}

div[data-testid="stMetric"] {
    background: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
    border-top: 4px solid #1d4ed8 !important;
    border-radius: 10px !important;
    padding: 14px 10px !important;
    text-align: center !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
}

div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] *,
div[data-testid="stMetricLabel"] > label,
div[data-testid="stMetricLabel"] > div {
    width: 100% !important;
    text-align: center !important;
    justify-content: center !important;
    font-size: 0.82rem !important;
    font-weight: 800 !important;
    color: #334155 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.6px !important;
    display: flex !important;
}

div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] * {
    width: 100% !important;
    text-align: center !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 1.55rem !important;
    font-weight: 700 !important;
    color: #0f172a !important;
    margin: 4px 0 !important;
    display: block !important;
}

div[data-testid="stMetricDelta"],
div[data-testid="stMetricDelta"] * {
    width: 100% !important;
    text-align: center !important;
    justify-content: center !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    margin-top: 4px !important;
    display: flex !important;
}

div[data-testid="stMetricDelta"] svg {
    display: none !important;
}

div[data-testid="stDataFrame"] th,
div[data-testid="stDataFrame"] [role="columnheader"],
div[data-testid="stDataFrame"] [role="columnheader"] * {
    text-align: center !important;
    justify-content: center !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.5px !important;
    color: #1e293b !important;
}

.thork-card-header {
    font-weight: 800;
    font-size: 0.92rem;
    color: #1e293b;
    text-align: center;
    padding-bottom: 8px;
    margin-bottom: 14px;
    border-bottom: 2px solid #3b82f6;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.spec-banner {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
    color: #ffffff;
    border-radius: 10px;
    padding: 18px 24px;
    margin-top: 24px !important;
    text-align: center;
    box-shadow: 0 4px 10px rgba(15, 23, 42, 0.15);
    border: 1px solid #3b82f6;
}

.spec-title {
    font-size: 0.82rem;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: #93c5fd;
    font-weight: 700;
}

.spec-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.35rem;
    font-weight: 700;
    margin-top: 6px;
    color: #ffffff;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ==============================================================================
# DỮ LIỆU CƠ SỞ TIÊU CHUẨN
# ==============================================================================
DF_TIEUCHUAN_VAI = pd.DataFrame([
    {"LOAI_VAI": "EP100", "LUC_CHON": 0,   "LUC_THUC": 100, "BE_DAY": 1.00, "TL_M2": 385},
    {"LOAI_VAI": "EP125", "LUC_CHON": 100, "LUC_THUC": 125, "BE_DAY": 1.15, "TL_M2": 450},
    {"LOAI_VAI": "EP150", "LUC_CHON": 125, "LUC_THUC": 150, "BE_DAY": 1.20, "TL_M2": 540},
    {"LOAI_VAI": "EP200", "LUC_CHON": 150, "LUC_THUC": 200, "BE_DAY": 1.40, "TL_M2": 700},
    {"LOAI_VAI": "EP250", "LUC_CHON": 200, "LUC_THUC": 250, "BE_DAY": 1.45, "TL_M2": 900},
    {"LOAI_VAI": "EP300", "LUC_CHON": 250, "LUC_THUC": 300, "BE_DAY": 1.50, "TL_M2": 1000},
    {"LOAI_VAI": "EP350", "LUC_CHON": 300, "LUC_THUC": 350, "BE_DAY": 1.55, "TL_M2": 1200},
    {"LOAI_VAI": "EP400", "LUC_CHON": 350, "LUC_THUC": 400, "BE_DAY": 1.65, "TL_M2": 1350},
    {"LOAI_VAI": "EP500", "LUC_CHON": 400, "LUC_THUC": 500, "BE_DAY": 1.70, "TL_M2": 1600},
])

DANH_SACH_MAY_EP = [
    {"TÊN MÁY": "MÁY ÉP CHẮN BÙN 34", "DK_XL_MM": 550, "SO_XL": 1, "KICH_THUOC_BAN": "1000x1400", "AP_LUC_DEFAULT": 100},
    {"TÊN MÁY": "MÁY ÉP CHÉN BÙN 35", "DK_XL_MM": 550, "SO_XL": 1, "KICH_THUOC_BAN": "1000x1400", "AP_LUC_DEFAULT": 100},
    {"TÊN MÁY": "MÁY ÉP CHẮN BÙN 35-1", "DK_XL_MM": 450, "SO_XL": 1, "KICH_THUOC_BAN": "1000x1250", "AP_LUC_DEFAULT": 120},
    {"TÊN MÁY": "MÁY ÉP CHẮN BÙN 35-2", "DK_XL_MM": 450, "SO_XL": 1, "KICH_THUOC_BAN": "1000x1250", "AP_LUC_DEFAULT": 120},
    {"TÊN MÁY": "MÁY ÉP CHẮN BÙN 35-3", "DK_XL_MM": 750, "SO_XL": 1, "KICH_THUOC_BAN": "1000x1400", "AP_LUC_DEFAULT": 150},
    {"TÊN MÁY": "MÁY ÉP CHẮN BÙN 35-4", "DK_XL_MM": 885, "SO_XL": 1, "KICH_THUOC_BAN": "1200x1450", "AP_LUC_DEFAULT": 150},
    {"TÊN MÁY": "MÁY ÉP CHẮN BÙN 35-5", "DK_XL_MM": 750, "SO_XL": 1, "KICH_THUOC_BAN": "1200x1250", "AP_LUC_DEFAULT": 150},
    {"TÊN MÁY": "MÁY ÉP CHẮN BÙN 35-6", "DK_XL_MM": 750, "SO_XL": 1, "KICH_THUOC_BAN": "1200x1250", "AP_LUC_DEFAULT": 150},
    {"TÊN MÁY": "MÁY ÉP PANSTON 800T 40-1", "DK_XL_MM": 762, "SO_XL": 1, "KICH_THUOC_BAN": "1100x1400", "AP_LUC_DEFAULT": 180},
    {"TÊN MÁY": "MÁY ÉP PANSTON 800T 40-2", "DK_XL_MM": 762, "SO_XL": 1, "KICH_THUOC_BAN": "1100x1400", "AP_LUC_DEFAULT": 180},
    {"TÊN MÁY": "MÁY ÉP BIDA 37", "DK_XL_MM": 300, "SO_XL": 2, "KICH_THUOC_BAN": "1200x1800", "AP_LUC_DEFAULT": 150},
    {"TÊN MÁY": "MÁY ÉP BIDA 37-1", "DK_XL_MM": 290, "SO_XL": 2, "KICH_THUOC_BAN": "800x1800", "AP_LUC_DEFAULT": 150},
]

DAY_PULLEY_CHUAN = [200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1400, 1600]

def chon_5_phuong_an_vai(F_cang_kgf_cm, he_so_an_toan=10.0, hieu_suat_moi_noi=0.95):
    danh_sach_ep = [100, 125, 150, 200, 250, 300, 400, 500]
    tong_luc_yeu_cau = F_cang_kgf_cm * he_so_an_toan * hieu_suat_moi_noi

    ket_qua = []
    for n in [2, 3, 4, 5, 6]:
        luc_1_lop = tong_luc_yeu_cau / n
        mac_chon = next((ep for ep in danh_sach_ep if ep >= luc_1_lop), None)
        
        ten_pa = f"Phương án {n} lớp ({n}P)"
        if mac_chon:
            de_xuat = f"{n}P(EP{mac_chon})"
            hop_le = True
        else:
            de_xuat = f"{n}P(>EP500 - ST)"
            hop_le = False
            
        ket_qua.append({
            "n": n,
            "KẾT CẤU": ten_pa,
            "LOẠI VẢI ĐỀ XUẤT": de_xuat,
            "LỰC ĐƠN VỊ 1 LỚP (kgf/cm)": round(luc_1_lop, 1),
            "CƯỜNG LỰC TỔNG (kgf/cm)": round(luc_1_lop * n, 1),
            "SF": f"{he_so_an_toan:.1f}",
            "hop_le": hop_le,
            "mac_ep": mac_chon if mac_chon else 9999
        })

    pa_dat = [p for p in ket_qua if p["hop_le"]]
    pa_khuyen_nghi_idx = None
    if pa_dat:
        pa_uu_tien = [p for p in pa_dat if 3 <= p["n"] <= 5]
        muc_tieu = pa_uu_tien if pa_uu_tien else pa_dat
        pa_chon = min(muc_tieu, key=lambda x: x["mac_ep"])
        pa_khuyen_nghi_idx = pa_chon["n"]

    for p in ket_qua:
        if p["n"] == pa_khuyen_nghi_idx:
            p["KẾT CẤU"] = "⭐ " + p["KẾT CẤU"] + " [Khuyến nghị]"
        del p["n"], p["hop_le"], p["mac_ep"]

    return pd.DataFrame(ket_qua)

def lam_tron_pulley_chuan(d_calc_mm):
    for d in DAY_PULLEY_CHUAN:
        if d >= d_calc_mm:
            return d
    return DAY_PULLEY_CHUAN[-1]

def tinh_sf_start(chieu_dai_tuyen):
    if chieu_dai_tuyen < 50:
        return 1.2 + (chieu_dai_tuyen / 50.0) * 0.1
    elif chieu_dai_tuyen <= 200:
        return 1.3 + ((chieu_dai_tuyen - 50.0) / 150.0) * 0.2
    elif chieu_dai_tuyen <= 400:
        return 1.5 + ((chieu_dai_tuyen - 200.0) / 200.0) * 0.3
    else:
        return 2.0 + ((chieu_dai_tuyen - 400.0) / 600.0) * 0.5

def tra_cuu_vai(luc_yeu_cau_1_lop):
    matched_ep = "EP100"
    for _, row in DF_TIEUCHUAN_VAI.iterrows():
        if luc_yeu_cau_1_lop >= row["LUC_CHON"]:
            matched_ep = row["LOAI_VAI"]
    return matched_ep

def tra_cuu_iso_3302(kich_thuoc):
    bang_iso = [
        (0, 3, 0.15, 0.25, 0.40, 0.50),
        (3, 6, 0.20, 0.30, 0.50, 0.70),
        (6, 10, 0.20, 0.40, 0.60, 0.80),
        (10, 18, 0.25, 0.50, 0.70, 1.00),
        (18, 30, 0.30, 0.60, 0.80, 1.30),
        (30, 50, 0.40, 0.80, 1.00, 1.60),
        (50, 80, 0.50, 1.00, 1.30, 2.00),
        (80, 120, 0.60, 1.20, 1.60, 2.50),
        (120, 180, 0.80, 1.40, 2.00, 3.00),
        (180, 250, 1.00, 1.60, 2.50, 4.00),
        (250, 315, 1.20, 2.00, 3.00, 5.00),
    ]
    for r in bang_iso:
        if r[0] <= kich_thuoc <= r[1]:
            return {"M1": r[2], "M2": r[3], "M3": r[4], "M4": r[5]}
    return {"M1": 1.5, "M2": 2.5, "M3": 4.0, "M4": 6.0}

# ==============================================================================
# MENU SIDEBAR
# ==============================================================================
with st.sidebar:
    st.markdown("<h3 style='text-align: center;'>⚙️ THORK ENGINEERING</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.85rem;'>Phiên bản 2026.1 | Cao Su & Băng Tải</p>", unsafe_allow_html=True)
    st.markdown("---")
    module_chon = st.radio(
        "LỰA CHỌN MODULE TÍNH TOÁN:",
        [
            "M1: THIẾT KẾ BĂNG TẢI (DIN & CEMA)",
            "M2: CÔNG NGHỆ ÉP THỦY LỰC & LƯU HÓA",
            "M3: ĐƠN COMPOUND & TRUYỀN ĐỘNG ĐAI"
        ]
    )

# ==============================================================================
# MODULE 1: THIẾT KẾ BĂNG TẢI
# ==============================================================================
if module_chon == "M1: THIẾT KẾ BĂNG TẢI (DIN & CEMA)":
    st.markdown("<h2 style='text-align: center;'>⚡ THIẾT KẾ & TÍNH TOÁN KỸ THUẬT HỆ BĂNG TẢI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b;'>Đối chiếu song song: DIN 22101 (Đức / Xưởng) & CEMA / Rulmeca (Mỹ)</p>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 1. TÍNH ĐỘNG CƠ & VẢI EP (DIN)",
        "⛓️ 2. BĂNG TẢI LÕI THÉP (ST)",
        "⚖️ 3. TRỌNG LƯỢNG 1M & PULLEY D_MIN",
        "🎯 4. BÓC TÁCH LỰC CẢN CEMA (USA)"
    ])

    with tab1:
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown('<div class="thork-card-header">📍 THÔNG SỐ TUYẾN</div>', unsafe_allow_html=True)
            B = st.number_input("Khổ rộng băng B (mm):", value=800, step=50)
            c_mode = st.radio("Cách nhập kích thước:", ["Chiều dài tuyến (L)", "Chu vi liền tròn (CVLT)"], horizontal=True)
            
            if c_mode == "Chiều dài tuyến (L)":
                L_input = st.number_input("Chiều dài tuyến L (m):", value=200.0, step=5.0)
            else:
                CVLT_input = st.number_input("Chu vi liền tròn CVLT (m):", value=400.0, step=5.0)

            alpha_deg = st.number_input("Góc dốc băng tải (°):", value=23.0, step=1.0)

        with c2:
            st.markdown('<div class="thork-card-header">⚙️ VẬN HÀNH & NĂNG SUẤT</div>', unsafe_allow_html=True)
            Q = st.number_input("Năng suất vận chuyển Q (t/h):", value=400.0, step=10.0)
            V = st.number_input("Vận tốc băng V (m/s):", value=1.0, step=0.1)
            mu = st.number_input("Hệ số ma sát con lăn (f):", value=0.07, step=0.01, format="%.2f")
            he_so_an_toan = st.number_input("Hệ số an toàn thiết kế (SF):", value=10.0, step=0.5)

        with c3:
            st.markdown('<div class="thork-card-header">🛡️ KẾT CẤU & TANG PULLEY</div>', unsafe_allow_html=True)
            cao_su_tren = st.number_input("Bề dày cao su trên (mm):", value=4.0, step=0.5)
            cao_su_duoi = st.number_input("Bề dày cao su dưới (mm):", value=2.0, step=0.5)
            hieu_suat = st.number_input("Hiệu suất truyền động (η):", value=0.85, step=0.05)
            he_so_vai = 0.95

            auto_pulley = st.checkbox("Tự động chuẩn hóa Pulley (D_min)", value=True)
            if not auto_pulley:
                D_pulley_custom = st.number_input("Đường kính Pulley tự nhập (mm):", value=630, step=50)

        # Tính toán DIN 22101
        L_tuyen_est = L_input if c_mode == "Chiều dài tuyến (L)" else (CVLT_input / 2.0)
        m2_bang = B * 0.0125
        m_vl = (Q * 1000.0) / (3600.0 * V)
        sf_start_est = tinh_sf_start(L_tuyen_est)
        sin_alpha = math.sin(math.radians(alpha_deg))

        F_kN_est = ((m_vl + m2_bang) * L_tuyen_est * 9.81 * (mu + sin_alpha)) / 1000.0
        luc_keo_kgf_cm_est = (F_kN_est * sf_start_est * 101.972) / (B / 10.0)
        luc_tong_vai_est = luc_keo_kgf_cm_est * he_so_an_toan * he_so_vai

        vai_chuan = tra_cuu_vai(luc_tong_vai_est / 5.0)
        row_vai = DF_TIEUCHUAN_VAI[DF_TIEUCHUAN_VAI["LOAI_VAI"] == vai_chuan].iloc[0]
        be_day_tong_mm = 5 * row_vai["BE_DAY"] + cao_su_tren + cao_su_duoi

        d_min_ly_thuyet = 25.0 * be_day_tong_mm
        d_pulley_chuan_mm = lam_tron_pulley_chuan(d_min_ly_thuyet) if auto_pulley else D_pulley_custom
        d_pulley_chuan_m = d_pulley_chuan_mm / 1000.0

        if c_mode == "Chiều dài tuyến (L)":
            L_tuyen = L_input
            CVLT = 2.0 * L_tuyen + math.pi * d_pulley_chuan_m
        else:
            CVLT = CVLT_input
            L_tuyen = (CVLT - math.pi * d_pulley_chuan_m) / 2.0

        sf_start = tinh_sf_start(L_tuyen)
        FH = (m_vl + m2_bang) * 9.81 * sin_alpha * L_tuyen
        FF = (m_vl + m2_bang) * 9.81 * mu * L_tuyen
        F_kN = (FH + FF) / 1000.0
        P_dong_co_kW = (F_kN * V / hieu_suat) * sf_start
        luc_keo_kgf_cm = (F_kN * sf_start * 101.972) / (B / 10.0)
        luc_cang_don_vi_kgf_cm = (F_kN * 101.972) / (B / 10.0)
        luc_kd_kgf_cm = (F_kN * sf_start * 101.972) / (B / 10.0)
        luc_keo_khoi_dong_N = luc_kd_kgf_cm * (B / 10.0) * 9.80665

        # Lưu session state cho Tab CEMA
        st.session_state['M1_L'] = L_tuyen
        st.session_state['M1_B'] = B
        st.session_state['M1_Q'] = Q
        st.session_state['M1_V'] = V
        st.session_state['M1_alpha'] = alpha_deg
        st.session_state['M1_pulley'] = d_pulley_chuan_mm
        st.session_state['M1_hieu_suat'] = hieu_suat
        st.session_state['M1_m2_bang'] = m2_bang

        st.markdown("---")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("CÔNG SUẤT ĐỘNG CƠ", f"{P_dong_co_kW:.1f} kW", f"Lực KĐ: {luc_keo_khoi_dong_N:,.0f} N")
        m2.metric("TỔNG LỰC KÉO F", f"{F_kN:.2f} kN", f"Cường lực: {luc_cang_don_vi_kgf_cm * he_so_an_toan:.1f} kgf/cm")
        m3.metric("PULLEY TIÊU CHUẨN", f"Ø {d_pulley_chuan_mm} mm", f"D_min tính: {d_min_ly_thuyet:.0f} mm")
        m4.metric("CHU VI LIỀN TRÒN (CVLT)", f"{CVLT:.2f} m", f"Tuyến L = {L_tuyen:.2f} m")

        # Bảng phương án vải bố căn lề & khóa pixel chuẩn
        df_5_phuong_an = chon_5_phuong_an_vai(
            F_cang_kgf_cm=luc_cang_don_vi_kgf_cm,
            he_so_an_toan=he_so_an_toan,
            hieu_suat_moi_noi=0.95
        )
        st.markdown("<h5 style='text-align: center; text-transform: uppercase; font-weight: 700; color: #1e293b;'>📋 CÁC PHƯƠNG ÁN KẾT CẤU VẢI BỐ ĐỀ XUẤT</h5>", unsafe_allow_html=True)
        st.dataframe(
            df_5_phuong_an,
            use_container_width=True,
            hide_index=True,
            column_config={
                "KẾT CẤU": st.column_config.TextColumn("PHƯƠNG ÁN KẾT CẤU", width=220),
                "LOẠI VẢI ĐỀ XUẤT": st.column_config.TextColumn("MÁC BĂNG ĐỀ XUẤT", width=150),
                "LỰC ĐƠN VỊ 1 LỚP (kgf/cm)": st.column_config.NumberColumn("LỰC 1 LỚP (KGF/CM)", format="%.1f", width=160),
                "CƯỜNG LỰC TỔNG (kgf/cm)": st.column_config.NumberColumn("CƯỜNG LỰC TỔNG (KGF/CM)", format="%.1f", width=180),
                "SF": st.column_config.TextColumn("HỆ SỐ AN TOÀN", width=120)
            }
        )

        row_kn = df_5_phuong_an[df_5_phuong_an["KẾT CẤU"].str.contains("Khuyến nghị")]
        quy_cach_de_xuat = row_kn["LOẠI VẢI ĐỀ XUẤT"].values[0] if not row_kn.empty else df_5_phuong_an["LOẠI VẢI ĐỀ XUẤT"].iloc[2]

        st.markdown(f"""
        <div class="spec-banner">
            <div class="spec-title">🚀 Quy cách băng tải thành phẩm xuất xưởng chuẩn hóa</div>
            <div class="spec-value">B{int(B)} x {quy_cach_de_xuat} x ({int(cao_su_tren)}+{int(cao_su_duoi)}) x {be_day_tong_mm:.1f}mm | CVLT = {CVLT:.2f} m</div>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="thork-card-header">⛓️ BĂNG TẢI LÕI THÉP (STEEL CORD BELTING - ST)</div>', unsafe_allow_html=True)
        col_st1, col_st2, col_st3 = st.columns(3)
        with col_st1:
            kho_st = st.number_input("Khổ rộng băng (mm):", value=1050, step=50, key="st_kho")
            chieu_dai_st = st.number_input("Chiều dài tuyến băng (m):", value=303.0, step=10.0, key="st_cd")
            day_tong_st = st.number_input("Bề dày tổng băng (mm):", value=15.0, step=1.0, key="st_day")
        with col_st2:
            dk_cap = st.number_input("Đường kính sợi cáp (mm):", value=6.0, step=0.5, key="st_dk")
            buoc_cap = st.number_input("Bước cáp t (mm):", value=8.0, step=0.5, key="st_buoc")
            loai_cap = st.selectbox("Cấu trúc bện sợi cáp:", ["7x7", "7x19"])
        with col_st3:
            luc_keo_dut_kn = st.number_input("Lực kéo đứt 1 sợi (kN):", value=15.8, step=0.5)
            khoi_luong_cap_g_m = st.number_input("Khối lượng cáp (g/m):", value=61.0, step=1.0)

        so_soi = int((kho_st - 150) / buoc_cap)
        tong_chieu_dai_cap_m = so_soi * chieu_dai_st
        tong_tl_cap_kg = (tong_chieu_dai_cap_m * khoi_luong_cap_g_m) / 1000.0
        tong_luc_keo_kn = so_soi * luc_keo_dut_kn

        st.markdown("---")
        st1, st2, st3 = st.columns(3)
        st1.metric("SỐ SỢI CÁP THÉP", f"{so_soi} sợi", f"Bước cáp: {buoc_cap} mm")
        st2.metric("TỔNG KHỐI LƯỢNG CÁP", f"{tong_tl_cap_kg:,.1f} kg", f"Chiều dài: {tong_chieu_dai_cap_m:,.0f} m")
        st3.metric("TỔNG LỰC KÉO ĐỨT", f"{tong_luc_keo_kn:,.1f} kN", f"Cấu trúc: {loai_cap}")

    with tab3:
        st.markdown('<div class="thork-card-header">⚖️ TRỌNG LƯỢNG 1 MÉT BĂNG & TANG PULLEY TỐI THIỂU</div>', unsafe_allow_html=True)
        c_tl1, c_tl2 = st.columns(2)
        with c_tl1:
            st.markdown("##### 1. Khối Lượng 1m Băng Tải Vải")
            chon_vai = st.selectbox("Mác vải bố EP:", DF_TIEUCHUAN_VAI["LOAI_VAI"].tolist(), index=6)
            so_lop_b = st.number_input("Số lớp bố vải:", value=4, min_value=1, max_value=8)
            kho_m = st.number_input("Khổ rộng (mm):", value=800, step=50, key="m_kho") / 1000.0
            cs_tren_m = st.number_input("Cao su mặt trên (mm):", value=4.0, key="m_cs_tr")
            cs_duoi_m = st.number_input("Cao su mặt dưới (mm):", value=2.0, key="m_cs_du")
            tt_cs = st.number_input("Tỷ trọng cao su (g/cm³):", value=1.15, step=0.01)

            row_v = DF_TIEUCHUAN_VAI[DF_TIEUCHUAN_VAI["LOAI_VAI"] == chon_vai].iloc[0]
            tl_vai_1m = (row_v["TL_M2"] * so_lop_b * kho_m) / 1000.0
            tl_cs_1m = (kho_m * 1.0 * (cs_tren_m + cs_duoi_m) / 1000.0) * (tt_cs * 1000.0)
            tl_tong_1m = tl_vai_1m + tl_cs_1m

            st.metric("TỔNG TRỌNG LƯỢNG 1 MÉT", f"{tl_tong_1m:.2f} kg/m", f"Vải: {tl_vai_1m:.2f} kg/m | CS: {tl_cs_1m:.2f} kg/m")

        with c_tl2:
            st.markdown("##### 2. Đường Kính Tang/Pully Tối Thiểu (D_min)")
            loai_loi = st.radio("Loại lõi chịu lực:", ["BĂNG TẢI EP (VẢI)", "BĂNG TẢI LÕI THÉP (ST)"], horizontal=True)
            if loai_loi == "BĂNG TẢI EP (VẢI)":
                k_pully = st.slider("Hệ số uốn K (EP):", min_value=20, max_value=30, value=25)
                day_bang_tong = so_lop_b * row_v["BE_DAY"] + cs_tren_m + cs_duoi_m
                d_min_ly_thuyet_tab3 = k_pully * day_bang_tong
                d_pulley_chuan_tab3 = lam_tron_pulley_chuan(d_min_ly_thuyet_tab3)
                st.metric("PULLEY TIÊU CHUẨN ĐỀ XUẤT", f"Ø {d_pulley_chuan_tab3} mm", f"D_min tính: {d_min_ly_thuyet_tab3:.1f} mm")
            else:
                alpha_pully = st.slider("Hệ số uốn α (ST):", min_value=120, max_value=150, value=140)
                dk_soi_th = st.number_input("Đường kính sợi cáp (mm):", value=6.0, step=0.5, key="tab3_dk_st")
                d_min_thep = dk_soi_th * alpha_pully
                d_pulley_thep_chuan = lam_tron_pulley_chuan(d_min_thep)
                st.metric("PULLEY TIÊU CHUẨN ĐỀ XUẤT", f"Ø {d_pulley_thep_chuan} mm", f"D_min tính: {d_min_thep:.1f} mm")

    with tab4:
        st.markdown('<div class="thork-card-header">⚡ TÍNH TOÁN CÔNG SUẤT CHUYÊN SÂU CEMA / RULMECA V7.24</div>', unsafe_allow_html=True)
        dong_bo = st.checkbox("🔗 Đồng bộ tự động thông số với Tab 1 (DIN 22101)", value=True)

        c_cema1, c_cema2, c_cema3 = st.columns(3)
        with c_cema1:
            st.markdown("##### 📍 Thông Số Cơ Bản")
            if dong_bo and 'M1_L' in st.session_state:
                B_cema_mm = float(st.session_state['M1_B'])
                L_cema_m = float(st.session_state['M1_L'])
                Q_cema_th = float(st.session_state['M1_Q'])
                V_cema_ms = float(st.session_state['M1_V'])
                H_cema_m = float(L_cema_m * math.sin(math.radians(st.session_state['M1_alpha'])))
                m2_bang_cema = float(st.session_state['M1_m2_bang'])
                st.info(f"Đã liên kết Tab 1: Khổ B={B_cema_mm:.0f}mm, L={L_cema_m:.1f}m, H={H_cema_m:.1f}m")
            else:
                B_cema_mm = st.number_input("Khổ rộng B (mm):", value=800.0, step=50.0, key="cema_B")
                L_cema_m = st.number_input("Chiều dài L (m):", value=200.0, step=5.0, key="cema_L")
                Q_cema_th = st.number_input("Năng suất Q (t/h):", value=400.0, step=20.0, key="cema_Q")
                V_cema_ms = st.number_input("Vận tốc V (m/s):", value=1.0, step=0.1, key="cema_V")
                H_cema_m = st.number_input("Chiều cao nâng H (m):", value=78.1, step=0.5, key="cema_H")
                m2_bang_cema = B_cema_mm * 0.0125

            w_in = B_cema_mm / 25.4

        with c_cema2:
            st.markdown("##### ⚙️ Lực Cản Ma Sát Phụ")
            temp_c = st.number_input("Nhiệt độ môi trường (°C):", value=25.0, step=5.0)
            so_cleaner = st.number_input("Số lượng gạt băng (Cleaners):", value=1, min_value=0, max_value=5)
            chieu_dai_skirt_m = st.number_input("Chiều dài phễu nạp (m):", value=3.66, step=0.5)
            be_sau_skirt_cm = st.number_input("Bề dày liệu tại phễu (cm):", value=7.62, step=1.0)

        with c_cema3:
            st.markdown("##### 🎯 Tang Trống & Bọc Lagging")
            dk_def = float(st.session_state.get('M1_pulley', 630.0)) if dong_bo else 630.0
            dk_tang_cema_mm = st.number_input("Đường kính tang chủ động (mm):", value=dk_def, step=50.0)
            boc_cao_su_mm = st.number_input("Bề dày bọc cao su tang (mm):", value=8.0, step=1.0)
            hieu_suat_truyen = float(st.session_state.get('M1_hieu_suat', 0.85)) if dong_bo else 0.85

        # Quy đổi đơn vị CEMA
        Wb_lbs_ft = m2_bang_cema * 0.67197
        L_ft = L_cema_m * 3.28084
        Q_tph = Q_cema_th * 1.10231
        V_fpm = V_cema_ms * 196.85
        H_ft = H_cema_m * 3.28084
        skirt_len_ft = chieu_dai_skirt_m * 3.28084
        skirt_depth_in = be_sau_skirt_cm / 2.54

        Wm_lbs_ft = (Q_tph * 2000.0) / (60.0 * V_fpm) if V_fpm > 0 else 0
        temp_f = temp_c * 1.8 + 32.0
        Kt = 1.0 if temp_f >= 32 else (1.0 + (32.0 - temp_f) * 0.008)
        Kx = 0.494
        Ky = 0.025

        Tx_lbs = L_ft * Kx * Kt
        Tyr_lbs = L_ft * Ky * Wb_lbs_ft * Kt
        Tyc_lbs = L_ft * Ky * (Wb_lbs_ft + Wm_lbs_ft) * Kt
        Th_lbs = Wm_lbs_ft * H_ft
        Tam_lbs = (Q_tph * V_fpm) / 3474.0
        Tsb_lbs = skirt_len_ft * (0.128 * (skirt_depth_in ** 2) + 0.15) * 6.0
        Tbc_lbs = so_cleaner * 180.0
        Tp_lbs = 20.0

        Te_lbs = Tx_lbs + Tyr_lbs + Tyc_lbs + Th_lbs + Tam_lbs + Tsb_lbs + Tbc_lbs + Tp_lbs
        Te_kN = Te_lbs * 0.00444822

        Cw = 0.38 if boc_cao_su_mm > 0 else 0.50
        T2_lbs = Cw * Te_lbs
        T1_lbs = Te_lbs + T2_lbs
        luc_piw = T1_lbs / w_in if w_in > 0 else 0
        luc_kgf_cm = (T1_lbs * 0.45359) / (B_cema_mm / 10.0) if B_cema_mm > 0 else 0

        HP_belt = (Te_lbs * V_fpm) / 33000.0
        HP_bearing = 0.03 * HP_belt + 0.05
        HP_gear = (HP_belt + HP_bearing) * (1.0 / max(hieu_suat_truyen, 0.01) - 1.0)
        HP_tong = HP_belt + HP_bearing + HP_gear
        P_tong_kW = HP_tong * 0.7457

        st.markdown("---")
        rc1, rc2, rc3, rc4, rc5 = st.columns(5)
        rc1.metric("CÔNG SUẤT MOTOR", f"{P_tong_kW:.2f} kW", f"{HP_tong:.1f} HP")
        rc2.metric("LỰC KÉO Te", f"{Te_kN:.2f} kN", f"{Te_lbs:,.0f} lbs")
        rc3.metric("LỰC CĂNG T1", f"{T1_lbs * 0.00445:.2f} kN", f"Cw = {Cw:.2f}")
        rc4.metric("CƯỜNG LỰC CEMA", f"{luc_piw:.1f} PIW")
        rc5.metric("CƯỜNG LỰC MÉP", f"{luc_kgf_cm:.2f} kgf/cm")

        # Bảng chi tiết thành phần lực
        df_cema_luc = pd.DataFrame({
            "THÀNH PHẦN LỰC CẢN CEMA": [
                "Lực ma sát con lăn (Tx)", "Lực uốn lượn nhánh về (Tyr)", "Lực uốn lượn nhánh tải (Tyc)",
                "Lực nâng thẳng đứng (Th)", "Lực gia tốc nạp liệu (Tam)", "Lực cản tấm chắn liệu (Tsb)",
                "Lực cản gạt băng (Tbc)", "Lực cản tang uốn phụ (Tp)"
            ],
            "GIÁ TRỊ (lbs)": [Tx_lbs, Tyr_lbs, Tyc_lbs, Th_lbs, Tam_lbs, Tsb_lbs, Tbc_lbs, Tp_lbs],
            "GIÁ TRỊ (kN)": [v * 0.00444822 for v in [Tx_lbs, Tyr_lbs, Tyc_lbs, Th_lbs, Tam_lbs, Tsb_lbs, Tbc_lbs, Tp_lbs]],
            "TỶ TRỌNG (%)": [(v / max(Te_lbs, 1.0)) * 100 for v in [Tx_lbs, Tyr_lbs, Tyc_lbs, Th_lbs, Tam_lbs, Tsb_lbs, Tbc_lbs, Tp_lbs]]
        })

        st.markdown("##### 📊 BẢNG BÓC TÁCH CHI TIẾT 8 THÀNH PHẦN LỰC CẢN:")
        st.dataframe(
            df_cema_luc,
            use_container_width=True,
            hide_index=True,
            column_config={
                "THÀNH PHẦN LỰC CẢN CEMA": st.column_config.TextColumn("Thành phần lực cản", width=260),
                "GIÁ TRỊ (lbs)": st.column_config.NumberColumn("Giá trị (lbs)", format="%.1f", width=140),
                "GIÁ TRỊ (kN)": st.column_config.NumberColumn("Giá trị (kN)", format="%.2f", width=140),
                "TỶ TRỌNG (%)": st.column_config.NumberColumn("Tỷ trọng (%)", format="%.1f%%", width=130)
            }
        )

        st.markdown("##### 📈 MÔ PHỎNG ĐƯỜNG CONG QUỸ ĐẠO RƠI VẬT LIỆU (CEMA TRAJECTORY)")
        R_tong_m = (dk_tang_cema_mm / 2.0 + boc_cao_su_mm + 15.0) / 1000.0
        V_tang = V_cema_ms
        ly_tam = (V_tang ** 2) / (9.81 * R_tong_m) if R_tong_m > 0 else 0
        theta_deg = 0.0 if ly_tam >= 1.0 else math.degrees(math.acos(ly_tam))

        t_arr = np.linspace(0, 0.8, 25)
        vx0 = V_tang * math.cos(math.radians(theta_deg))
        vy0 = V_tang * math.sin(math.radians(theta_deg))
        x_m = vx0 * t_arr
        y_m = - (vy0 * t_arr + 0.5 * 9.81 * (t_arr ** 2))

        df_traj = pd.DataFrame({"Khoảng cách bay X (m)": x_m, "Độ cao rơi Y (m)": y_m})
        st.line_chart(df_traj.set_index("Khoảng cách bay X (m)"))

# ==============================================================================
# MODULE 2: ÉP THỦY LỰC & LƯU HÓA
# ==============================================================================
elif module_chon == "M2: CÔNG NGHỆ ÉP THỦY LỰC & LƯU HÓA":
    st.markdown("<h2 style='text-align: center;'>🛑 CÔNG NGHỆ ÉP THỦY LỰC & LƯU HÓA CAO SU</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b;'>Kiểm chuẩn áp lực khuôn, trọng lượng phôi định hình & dung sai ISO 3302-1</p>", unsafe_allow_html=True)

    tab_ep1, tab_ep2, tab_ep3 = st.tabs([
        "⚙️ 1. LỰC ÉP THỦY LỰC & TIÊU CHUẨN",
        "⚖️ 2. TÍNH TRỌNG LƯỢNG PHÔI",
        "📐 3. TRA CỨU DUNG SAI ISO 3302-1"
    ])

    with tab_ep1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="thork-card-header">1. MÁY ÉP & ÁP SUẤT THỦY LỰC</div>', unsafe_allow_html=True)
            ten_cac_may = [m["TÊN MÁY"] for m in DANH_SACH_MAY_EP]
            may_da_chon = st.selectbox("Chọn máy ép từ danh mục xưởng:", ten_cac_may)
            thong_tin_may = next(item for item in DANH_SACH_MAY_EP if item["TÊN MÁY"] == may_da_chon)

            c_xl1, c_xl2 = st.columns(2)
            with c_xl1:
                dk_xl = st.number_input("Đường kính piston xi lanh (mm):", value=float(thong_tin_may["DK_XL_MM"]))
            with c_xl2:
                so_xl = st.number_input("Số lượng xi lanh:", value=int(thong_tin_may["SO_XL"]), step=1)

            ap_luc_dong_ho = st.number_input("Áp lực đồng hồ cài đặt (kg/cm²):", value=float(thong_tin_may["AP_LUC_DEFAULT"]), step=5.0)
            st.caption(f"Kích thước bàn gia nhiệt: **{thong_tin_may['KICH_THUOC_BAN']} mm**")

        with col2:
            st.markdown('<div class="thork-card-header">2. THÔNG SỐ KHUÔN & SẢN PHẨM</div>', unsafe_allow_html=True)
            c_k1, c_k2 = st.columns(2)
            with c_k1:
                dai_khuon = st.number_input("Chiều dài khuôn (cm):", value=104.0, step=1.0)
            with c_k2:
                rong_khuon = st.number_input("Chiều rộng khuôn (cm):", value=64.0, step=1.0)
            dien_tich_khuon = dai_khuon * rong_khuon

            do_cung = st.selectbox("Độ cứng sản phẩm (Shore A):", ["SHORE A 40-50", "SHORE A 50-60", "SHORE A 60-70", "SHORE A 70-80"], index=1)
            do_phuc_tap = st.selectbox("Độ phức tạp hình học / Hoa văn:", ["ĐƠN GIẢN KHÔNG GÂN", "NHIỀU GÂN MỎNG"])

        r_cm = (dk_xl / 10.0) / 2.0
        s_piston_cm2 = (r_cm ** 2) * math.pi
        tong_luc_ep_kg = (s_piston_cm2 * ap_luc_dong_ho) * so_xl
        luc_ep_sp = tong_luc_ep_kg / dien_tich_khuon if dien_tich_khuon > 0 else 0

        quy_chuan = {
            ("SHORE A 40-50", "ĐƠN GIẢN KHÔNG GÂN"): (24, 34),
            ("SHORE A 40-50", "NHIỀU GÂN MỎNG"): (35, 48),
            ("SHORE A 50-60", "ĐƠN GIẢN KHÔNG GÂN"): (30, 42),
            ("SHORE A 50-60", "NHIỀU GÂN MỎNG"): (42, 58),
            ("SHORE A 60-70", "ĐƠN GIẢN KHÔNG GÂN"): (38, 52),
            ("SHORE A 60-70", "NHIỀU GÂN MỎNG"): (52, 70),
            ("SHORE A 70-80", "ĐƠN GIẢN KHÔNG GÂN"): (48, 68),
            ("SHORE A 70-80", "NHIỀU GÂN MỎNG"): (65, 85),
        }
        min_qc, max_qc = quy_chuan.get((do_cung, do_phuc_tap), (30, 45))

        st.markdown("---")
        res1, res2, res3 = st.columns(3)
        res1.metric("TỔNG LỰC ÉP MÁY", f"{tong_luc_ep_kg/1000.0:,.1f} Tấn", f"S_piston: {s_piston_cm2*so_xl:.0f} cm²")
        res2.metric("ÁP LỰC TRÊN KHUÔN THỰC TẾ", f"{luc_ep_sp:.2f} kg/cm²", f"S_khuôn: {dien_tich_khuon:,.0f} cm²")
        res3.metric("TIÊU CHUẨN QUY ĐỊNH", f"{min_qc} – {max_qc} kg/cm²")

        if luc_ep_sp < min_qc:
            st.error(f"❌ **THIẾU ÁP LỰC ÉP:** Áp lực thực tế ({luc_ep_sp:.1f} kg/cm²) thấp hơn chuẩn ({min_qc} kg/cm²). Nguy cơ xốp phôi, thiếu cao su hoặc rỗ bọt khí.")
        elif luc_ep_sp > max_qc:
            st.warning(f"⚠️ **VƯỢT TIÊU CHUẨN ÉP:** Áp lực thực tế ({luc_ep_sp:.1f} kg/cm²) vượt chuẩn ({max_qc} kg/cm²). Cần kiểm tra bavia dày và biến dạng lòng khuôn.")
        else:
            st.success(f"✅ **ÁP LỰC HOÀN HẢO:** Nằm chính xác trong vùng tối ưu ({min_qc} – {max_qc} kg/cm²).")

    with tab_ep2:
        st.markdown('<div class="thork-card-header">⚖️ TÍNH TOÁN TRỌNG LƯỢNG PHÔI CAO SU</div>', unsafe_allow_html=True)
        loai_hinh = st.selectbox("Hình học phôi định hình:", ["HÌNH TRỤ TRÒN", "HÌNH TRỤ RỖNG (ỐNG)", "HÌNH HỘP CHỮ NHẬT", "HÌNH NÓN CỤT RỖNG"])

        col_p1, col_p2 = st.columns(2)
        with col_p1:
            tt_phoi = st.number_input("Tỷ trọng cao su (g/cm³):", value=1.20, step=0.01)
            so_luong_phoi = st.number_input("Số lượng phôi cần cắt:", value=1, min_value=1)

        with col_p2:
            the_tich_cm3 = 0.0
            if loai_hinh == "HÌNH TRỤ TRÒN":
                d_tru = st.number_input("Đường kính (mm):", value=100.0)
                h_tru = st.number_input("Chiều cao (mm):", value=60.0)
                the_tich_cm3 = (math.pi * ((d_tru/10/2)**2) * (h_tru/10))
            elif loai_hinh == "HÌNH TRỤ RỖNG (ỐNG)":
                d_ngoai = st.number_input("Đường kính ngoài (mm):", value=60.0)
                d_trong = st.number_input("Đường kính trong (mm):", value=27.2)
                h_ong = st.number_input("Chiều cao (mm):", value=30.0)
                the_tich_cm3 = math.pi * (((d_ngoai/10/2)**2) - ((d_trong/10/2)**2)) * (h_ong/10)
            elif loai_hinh == "HÌNH HỘP CHỮ NHẬT":
                c1 = st.number_input("Chiều dài (mm):", value=150.0)
                c2 = st.number_input("Chiều rộng (mm):", value=80.0)
                c3 = st.number_input("Chiều dày (mm):", value=25.0)
                the_tich_cm3 = (c1/10) * (c2/10) * (c3/10)
            elif loai_hinh == "HÌNH NÓN CỤT RỖNG":
                D_lon = st.number_input("ĐK đáy lớn ngoài (mm):", value=152.0)
                d_lon_tr = st.number_input("ĐK đáy lớn trong (mm):", value=50.0)
                D_be = st.number_input("ĐK đáy bé ngoài (mm):", value=76.0)
                d_be_tr = st.number_input("ĐK đáy bé trong (mm):", value=50.0)
                h_non = st.number_input("Chiều cao (mm):", value=150.2)

                V_ngoai = (1/3) * math.pi * (h_non/10) * (((D_lon/20)**2) + ((D_be/20)**2) + (D_lon/20)*(D_be/20))
                V_trong = (1/3) * math.pi * (h_non/10) * (((d_lon_tr/20)**2) + ((d_be_tr/20)**2) + (d_lon_tr/20)*(d_be_tr/20))
                the_tich_cm3 = max(0.0, V_ngoai - V_trong)

        khoi_luong_1_phoi_g = the_tich_cm3 * tt_phoi
        tong_tl_phoi_kg = (khoi_luong_1_phoi_g * so_luong_phoi) / 1000.0

        st.markdown("---")
        cp1, cp2 = st.columns(2)
        cp1.metric("KHỐI LƯỢNG 1 PHÔI", f"{khoi_luong_1_phoi_g:.2f} g", f"V = {the_tich_cm3:.2f} cm³")
        cp2.metric(f"TỔNG KHỐI LƯỢNG ({so_luong_phoi} PHÔI)", f"{tong_tl_phoi_kg:.3f} kg")

    with tab_ep3:
        st.markdown('<div class="thork-card-header">📐 TRA CỨU DUNG SAI KÍCH THƯỚC ISO 3302-1 (VDI 2005)</div>', unsafe_allow_html=True)
        kt_nhap = st.number_input("Nhập kích thước danh nghĩa L (mm):", value=42.0, step=1.0)
        ds = tra_cuu_iso_3302(kt_nhap)

        df_ds = pd.DataFrame({
            "CẤP CHÍNH XÁC": ["Cấp M1 (Rất chính xác)", "Cấp M2 (Chính xác)", "Cấp M3 (Tiêu chuẩn)", "Cấp M4 (Thô)"],
            "DUNG SAI CHO PHÉP": [f"± {ds['M1']:.2f}", f"± {ds['M2']:.2f}", f"± {ds['M3']:.2f}", f"± {ds['M4']:.2f}"],
            "GIỚI HẠN DƯỚI (mm)": [kt_nhap - ds['M1'], kt_nhap - ds['M2'], kt_nhap - ds['M3'], kt_nhap - ds['M4']],
            "GIỚI HẠN TRÊN (mm)": [kt_nhap + ds['M1'], kt_nhap + ds['M2'], kt_nhap + ds['M3'], kt_nhap + ds['M4']]
        })

        st.dataframe(
            df_ds,
            use_container_width=True,
            hide_index=True,
            column_config={
                "CẤP CHÍNH XÁC": st.column_config.TextColumn("Cấp chính xác", width=220),
                "DUNG SAI CHO PHÉP": st.column_config.TextColumn("Dung sai cho phép", width=160),
                "GIỚI HẠN DƯỚI (mm)": st.column_config.NumberColumn("Giới hạn dưới (mm)", format="%.2f", width=180),
                "GIỚI HẠN TRÊN (mm)": st.column_config.NumberColumn("Giới hạn trên (mm)", format="%.2f", width=180)
            }
        )

# ==============================================================================
# MODULE 3: COMPOUND & TRUYỀN ĐỘNG ĐAI
# ==============================================================================
elif module_chon == "M3: ĐƠN COMPOUND & TRUYỀN ĐỘNG ĐAI":
    st.markdown("<h2 style='text-align: center;'>🧪 CÔNG NGHỆ COMPOUND & TRUYỀN ĐỘNG ĐAI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b;'>Cân bằng đơn pha chế compound lý thuyết & tra cứu đai thang Courroie ISO 4184</p>", unsafe_allow_html=True)

    tab_cp1, tab_cp2 = st.tabs([
        "🧪 1. TÍNH TOÁN ĐƠN PHA CHẾ COMPOUND",
        "⚙️ 2. TRA CỨU DÂY ĐAI COURROIE (ISO 4184)"
    ])

    with tab_cp1:
        st.markdown('<div class="thork-card-header">🧪 BẢNG TÍNH ĐƠN PHA CHẾ VẬT TƯ COMPOUND</div>', unsafe_allow_html=True)
        data_compound = [
            {"STT": 1, "VẬT TƯ": "Cao su SVR 3L", "KHỐI LƯỢNG (kg)": 0.0, "TỶ TRỌNG RIÊNG": 0.93},
            {"STT": 2, "VẬT TƯ": "Cao su SBR 1712", "KHỐI LƯỢNG (kg)": 10.0, "TỶ TRỌNG RIÊNG": 0.945},
            {"STT": 3, "VẬT TƯ": "Cao su tái sinh CS TS", "KHỐI LƯỢNG (kg)": 30.0, "TỶ TRỌNG RIÊNG": 1.210},
            {"STT": 4, "VẬT TƯ": "Than N330", "KHỐI LƯỢNG (kg)": 5.0, "TỶ TRỌNG RIÊNG": 1.950},
            {"STT": 5, "VẬT TƯ": "Bột mài cao su", "KHỐI LƯỢNG (kg)": 37.5, "TỶ TRỌNG RIÊNG": 1.300},
            {"STT": 6, "VẬT TƯ": "EVA", "KHỐI LƯỢNG (kg)": 7.5, "TỶ TRỌNG RIÊNG": 0.850},
            {"STT": 7, "VẬT TƯ": "Bông chỉ", "KHỐI LƯỢNG (kg)": 5.0, "TỶ TRỌNG RIÊNG": 1.000},
            {"STT": 8, "VẬT TƯ": "Dầu Parafin", "KHỐI LƯỢNG (kg)": 2.0, "TỶ TRỌNG RIÊNG": 0.880},
            {"STT": 9, "VẬT TƯ": "Phòng lão RD", "KHỐI LƯỢNG (kg)": 0.375, "TỶ TRỌNG RIÊNG": 1.050},
            {"STT": 10, "VẬT TƯ": "Acid Stearic", "KHỐI LƯỢNG (kg)": 0.250, "TỶ TRỌNG RIÊNG": 0.980},
            {"STT": 11, "VẬT TƯ": "Lưu huỳnh (S)", "KHỐI LƯỢNG (kg)": 0.800, "TỶ TRỌNG RIÊNG": 2.070},
            {"STT": 12, "VẬT TƯ": "Xúc tiến CC ms3", "KHỐI LƯỢNG (kg)": 0.080, "TỶ TRỌNG RIÊNG": 2.700},
        ]

        df_editor = st.data_editor(
            pd.DataFrame(data_compound),
            num_rows="dynamic",
            use_container_width=True,
            column_config={
                "STT": st.column_config.NumberColumn("STT", width=80),
                "VẬT TƯ": st.column_config.TextColumn("Vật tư", width=220),
                "KHỐI LƯỢNG (kg)": st.column_config.NumberColumn("Khối lượng (kg)", format="%.3f", width=160),
                "TỶ TRỌNG RIÊNG": st.column_config.NumberColumn("Tỷ trọng riêng", format="%.3f", width=140)
            }
        )

        df_calc = df_editor.dropna(subset=["VẬT TƯ"]).copy()
        df_calc["KHỐI LƯỢNG (kg)"] = pd.to_numeric(df_calc["KHỐI LƯỢNG (kg)"], errors="coerce").fillna(0)
        df_calc["TỶ TRỌNG RIÊNG"] = pd.to_numeric(df_calc["TỶ TRỌNG RIÊNG"], errors="coerce").fillna(1.0).replace(0, 1.0)
        df_calc["THỂ TÍCH (Lít)"] = df_calc["KHỐI LƯỢNG (kg)"] / df_calc["TỶ TRỌNG RIÊNG"]

        m_tong = df_calc["KHỐI LƯỢNG (kg)"].sum()
        v_tong = df_calc["THỂ TÍCH (Lít)"].sum()
        df_calc["TỶ LỆ (%)"] = (df_calc["KHỐI LƯỢNG (kg)"] / m_tong * 100.0) if m_tong > 0 else 0
        d_compound = m_tong / v_tong if v_tong > 0 else 0

        st.markdown("---")
        mc1, mc2, mc3 = st.columns(3)
        mc1.metric("TỔNG KHỐI LƯỢNG MẺ", f"{m_tong:.3f} kg")
        mc2.metric("TỔNG THỂ TÍCH MẺ", f"{v_tong:.3f} Lít")
        mc3.metric("TỶ TRỌNG LÝ THUYẾT", f"{d_compound:.3f} g/cm³")

        st.dataframe(
            df_calc[["STT", "VẬT TƯ", "KHỐI LƯỢNG (kg)", "TỶ LỆ (%)", "TỶ TRỌNG RIÊNG", "THỂ TÍCH (Lít)"]],
            use_container_width=True,
            hide_index=True,
            column_config={
                "STT": st.column_config.NumberColumn("STT", width=80),
                "VẬT TƯ": st.column_config.TextColumn("Vật tư", width=220),
                "KHỐI LƯỢNG (kg)": st.column_config.NumberColumn("Khối lượng (kg)", format="%.3f", width=140),
                "TỶ LỆ (%)": st.column_config.NumberColumn("Tỷ lệ (%)", format="%.2f%%", width=120),
                "TỶ TRỌNG RIÊNG": st.column_config.NumberColumn("Tỷ trọng", format="%.3f", width=120),
                "THỂ TÍCH (Lít)": st.column_config.NumberColumn("Thể tích (Lít)", format="%.3f", width=140)
            }
        )

    with tab_cp2:
        st.markdown('<div class="thork-card-header">⚙️ TRA CỨU DÂY ĐAI THANG COURROIE (ISO 4184-1992)</div>', unsafe_allow_html=True)
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            ban_dai = st.selectbox("Tiết diện đai hình thang:", ["BẢN A", "BẢN B", "BẢN C", "BẢN D", "BẢN E"], index=3)
            don_vi_nhap = st.radio("Đơn vị nhập chiều dài ngoài (La):", ["Theo Inch (La)", "Theo mm (La)"], horizontal=True)
            if don_vi_nhap == "Theo Inch (La)":
                la_inch = st.number_input("Chiều dài ngoài La (inch):", value=358.0, step=1.0)
                la_mm = la_inch * 25.4
            else:
                la_mm = st.number_input("Chiều dài ngoài La (mm):", value=9093.0, step=10.0)
                la_inch = la_mm / 25.4

        with col_c2:
            chenh_lech_map = {"BẢN A": 30.0, "BẢN B": 43.0, "BẢN C": 56.0, "BẢN D": 126.0, "BẢN E": 150.0}
            delta_l = chenh_lech_map.get(ban_dai, 126.0)
            li_mm = la_mm - delta_l
            li_inch = li_mm / 25.4
            dung_sai_mm = 0.005 * la_mm + 10.0

        st.markdown("---")
        m_cr1, m_cr2, m_cr3 = st.columns(3)
        m_cr1.metric("CHIỀU DÀI NGOÀI (La)", f"{la_mm:.0f} mm", f"{la_inch:.2f} inch")
        m_cr2.metric("CHIỀU DÀI TRONG (Li)", f"{li_mm:.0f} mm", f"{li_inch:.2f} inch")
        m_cr3.metric("DUNG SAI ISO 4184", f"± {dung_sai_mm:.1f} mm")
