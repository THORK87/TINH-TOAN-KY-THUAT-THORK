import streamlit as st
import numpy as np
import pandas as pd
import math

st.set_page_config(
    page_title="HỆ THỐNG TÍNH TOÁN KỸ THUẬT THORK 2026", 
    layout="wide", 
    page_icon="⚙️"
)

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

def lam_tron_pulley_chuan(d_calc_mm):
    for d in DAY_PULLEY_CHUAN:
        if d >= d_calc_mm:
            return d
    return DAY_PULLEY_CHUAN[-1]

def tinh_sf_start(chieu_dai_tuyen):
    if chieu_dai_tuyen < 50:
        return 1.2 + (chieu_dai_tuyen / 50.0) * (1.3 - 1.2)
    elif chieu_dai_tuyen <= 200:
        return 1.3 + ((chieu_dai_tuyen - 50.0) / (200.0 - 50.0)) * (1.5 - 1.3)
    elif chieu_dai_tuyen <= 400:
        return 1.5 + ((chieu_dai_tuyen - 200.0) / (400.0 - 200.0)) * (1.8 - 1.5)
    else:
        return 2.0 + ((chieu_dai_tuyen - 400.0) / (1000.0 - 400.0)) * (2.5 - 2.0)

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
# MENU ĐIỀU HƯỚNG TỔNG
# ==============================================================================
st.sidebar.title("🛠️ MENU HỆ THỐNG THORK")
module_chon = st.sidebar.radio(
    "CHỌN MODULE TÍNH TOÁN:",
    [
        "MODULE 1: THIẾT KẾ BĂNG TẢI (DIN 22101 & CEMA / RULMECA)",
        "MODULE 2: CÔNG NGHỆ ÉP THỦY LỰC & LƯU HÓA CAO SU",
        "MODULE 3: CÔNG NGHỆ COMPOUND & TRUYỀN ĐỘNG ĐAI"
    ]
)

# ==============================================================================
# MODULE 1: THIẾT KẾ & TÍNH TOÁN BĂNG TẢI (DIN 22101 & CEMA / RULMECA)
# ==============================================================================
if module_chon == "MODULE 1: THIẾT KẾ BĂNG TẢI (DIN 22101 & CEMA / RULMECA)":
    st.title("⚡ MODULE 1: THIẾT KẾ & TÍNH TOÁN HỆ THỐNG BĂNG TẢI")
    st.caption("ĐỐI CHIẾU SONG SONG TIÊU CHUẨN DIN 22101 (ĐỨC/XƯỞNG) & TIÊU CHUẨN CEMA / RULMECA (MỸ)")

    tab1, tab2, tab3, tab4 = st.tabs([
        "1. TÍNH ĐỘNG CƠ & CHỌN VẢI EP (DIN 22101)",
        "2. ĐỊNH MỨC BĂNG TẢI LÕI THÉP (ST)",
        "3. TRỌNG LƯỢNG 1M BĂNG & TANG TỐI THIỂU",
        "4. TÍNH CÔNG SUẤT CHUYÊN SÂU CEMA / RULMECA (USA)"
    ])

    with tab1:
        c1, c2, c3 = st.columns(3)
        with c1:
            st.subheader("THÔNG SỐ TUYẾN BĂNG")
            B = st.number_input("KHỔ RỘNG BĂNG B (mm):", value=800, step=50)
            c_mode = st.radio("CÁCH NHẬP CHIỀU DÀI:", ["CHIỀU DÀI TUYẾN (L)", "CHU VI LIỀN TRÒN (CVLT)"], horizontal=True)
            
            if c_mode == "CHIỀU DÀI TUYẾN (L)":
                L_input = st.number_input("CHIỀU DÀI TUYẾN BĂNG L (m):", value=200.0, step=5.0)
            else:
                CVLT_input = st.number_input("CHU VI LIỀN TRÒN CVLT (m):", value=400.0, step=5.0)

            alpha_deg = st.number_input("GÓC DỐC BĂNG TẢI (°):", value=23.0, step=1.0)

        with c2:
            st.subheader("THÔNG SỐ VẬN HÀNH")
            Q = st.number_input("NĂNG SUẤT VẬN CHUYỂN Q (t/h):", value=400.0, step=10.0)
            V = st.number_input("VẬN TỐC BĂNG V (m/s):", value=1.0, step=0.1)
            mu = st.number_input("HỆ SỐ MA SÁT CON LĂN (f):", value=0.07, step=0.01, format="%.2f")
            he_so_an_toan = st.number_input("HỆ SỐ AN TOÀN (SF):", value=10.0, step=0.5)

        with c3:
            st.subheader("KẾT CẤU & ĐƯỜNG KÍNH PULLEY")
            cao_su_tren = st.number_input("BỀ DÀY CAO SU TRÊN (mm):", value=4.0, step=0.5)
            cao_su_duoi = st.number_input("BỀ DÀY CAO SU DƯỚI (mm):", value=2.0, step=0.5)
            hieu_suat = st.number_input("HIỆU SUẤT TRUYỀN ĐỘNG (η):", value=0.85, step=0.05)
            he_so_vai = 0.95

            auto_pulley = st.checkbox("TỰ ĐỘNG CHỌN PULLEY THEO D_MIN CHUẨN", value=True)
            if not auto_pulley:
                D_pulley_custom = st.number_input("ĐƯỜNG KÍNH PULLEY TỰ NHẬP (mm):", value=630, step=50)

        # -------------------------------------------------------------
        # VÒNG TÍNH TOÁN LẶP CHUẨN XÁC:
        # Bước A: Ước tính tuyến băng sơ bộ
        L_tuyen_est = L_input if c_mode == "CHIỀU DÀI TUYẾN (L)" else (CVLT_input / 2.0)
        m2_bang = B * 0.0125
        m_vl = (Q * 1000.0) / (3600.0 * V)
        sf_start_est = tinh_sf_start(L_tuyen_est)
        
        alpha_rad = math.radians(alpha_deg)
        sin_alpha = math.sin(alpha_rad)

        F_kN_est = ((m_vl + m2_bang) * L_tuyen_est * 9.81 * (mu + sin_alpha)) / 1000.0
        luc_keo_kgf_cm_est = (F_kN_est * sf_start_est * 101.972) / (B / 10.0)
        luc_tong_vai_est = luc_keo_kgf_cm_est * he_so_an_toan * he_so_vai

        # Chọn vải 5P làm chuẩn xác định độ dày
        vai_chuan = tra_cuu_vai(luc_tong_vai_est / 5.0)
        row_vai = DF_TIEUCHUAN_VAI[DF_TIEUCHUAN_VAI["LOAI_VAI"] == vai_chuan].iloc[0]
        be_day_tong_mm = 5 * row_vai["BE_DAY"] + cao_su_tren + cao_su_duoi

        # Tính D_min theo hệ số K=25 và làm tròn lên đường kính tiêu chuẩn
        d_min_ly_thuyet = 25.0 * be_day_tong_mm
        d_pulley_chuan_mm = lam_tron_pulley_chuan(d_min_ly_thuyet) if auto_pulley else D_pulley_custom
        d_pulley_chuan_m = d_pulley_chuan_mm / 1000.0

        # Bước B: Khóa kích thước chính thức bằng công thức chu vi có Pulley
        if c_mode == "CHIỀU DÀI TUYẾN (L)":
            L_tuyen = L_input
            CVLT = 2.0 * L_tuyen + math.pi * d_pulley_chuan_m
        else:
            CVLT = CVLT_input
            L_tuyen = (CVLT - math.pi * d_pulley_chuan_m) / 2.0

        # Tính toán lại lần cuối theo chiều dài tuyến thực
        sf_start = tinh_sf_start(L_tuyen)
        h_nang = sin_alpha * L_tuyen
        FH = (m_vl + m2_bang) * 9.81 * sin_alpha * L_tuyen
        FF = (m_vl + m2_bang) * 9.81 * mu * L_tuyen
        F_kN = (FH + FF) / 1000.0
        P_dong_co_kW = (F_kN * V / hieu_suat) * sf_start
        luc_keo_kgf_cm = (F_kN * sf_start * 101.972) / (B / 10.0)
        luc_tong_vai = luc_keo_kgf_cm * he_so_an_toan * he_so_vai

        vai_3p = tra_cuu_vai(luc_tong_vai / 3.0)
        vai_4p = tra_cuu_vai(luc_tong_vai / 4.0)
        vai_5p = tra_cuu_vai(luc_tong_vai / 5.0)
        quy_cach_de_xuat = f"B{int(B)} x 5P({vai_5p}) x ({int(cao_su_tren)}+{int(cao_su_duoi)}) x {be_day_tong_mm:.1f}mm : CVLT = {CVLT:.2f}m"

        st.divider()
        st.subheader("📊 KẾT QUẢ TÍNH TOÁN KỸ THUẬT & PULLEY")

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("CÔNG SUẤT ĐỘNG CƠ", f"{P_dong_co_kW:.1f} kW")
        # Tính lực kéo khởi động trên 1 cm khổ rộng băng (kgf/cm)
luc_kd_kgf_cm = (F_kN * sf_start * 101.972) / (B / 10.0)

# Hiển thị vào metric:
m2.metric(
    "TỔNG LỰC KÉO F",
    f"{F_kN:.2f} kN",
    delta=f"{luc_kd_kgf_cm:.2f} kgf/cm (kđ)"
)
        m3.metric("PULLEY TIÊU CHUẨN ĐƯỢC CHỌN", f"Ø {d_pulley_chuan_mm} mm", delta=f"D_min: {d_min_ly_thuyet:.0f} mm")
        m4.metric("CHU VI LIỀN TRÒN (CVLT)", f"{CVLT:.2f} m", delta=f"Tuyến L = {L_tuyen:.2f} m")

        st.markdown("#### 🎯 GỢI Ý PHƯƠNG ÁN KẾT CẤU VẢI BỐ")
        df_ep = pd.DataFrame({
            "KẾT CẤU": ["Phương án 3 lớp (3P)", "Phương án 4 lớp (4P)", "Phương án 5 lớp (5P) [Khuyến nghị]"],
            "LOẠI VẢI ĐỀ XUẤT": [f"3P({vai_3p})", f"4P({vai_4p})", f"5P({vai_5p})"],
            "LỰC CHỊU MỖI LỚP (kgf/cm)": [f"{luc_tong_vai/3:.1f}", f"{luc_tong_vai/4:.1f}", f"{luc_tong_vai/5:.1f}"],
            "HỆ SỐ KHỞI ĐỘNG (SF)": [f"{sf_start:.3f}", f"{sf_start:.3f}", f"{sf_start:.3f}"]
        })
        st.table(df_ep)
        st.success(f"📌 **QUY CÁCH BĂNG TẢI HOÀN CHỈNH XUẤT XƯỞNG:** `{quy_cach_de_xuat}`")

    with tab2:
        st.subheader("TÍNH TOÁN BĂNG TẢI LÕI THÉP (ST)")
        col_st1, col_st2, col_st3 = st.columns(3)
        with col_st1:
            kho_st = st.number_input("KHỔ RỘNG BĂNG (mm):", value=1050, step=50, key="st_kho")
            chieu_dai_st = st.number_input("CHIỀU DÀI TUYẾN BĂNG (m):", value=303.0, step=10.0, key="st_cd")
            day_tong_st = st.number_input("BỀ DÀY TỔNG (mm):", value=15.0, step=1.0, key="st_day")
        with col_st2:
            dk_cap = st.number_input("ĐƯỜNG KÍNH SỢI CÁP THÉP (mm):", value=6.0, step=0.5, key="st_dk")
            buoc_cap = st.number_input("BƯỚC CÁP (mm):", value=8.0, step=0.5, key="st_buoc")
            loai_cap = st.selectbox("CẤU TRÚC SỢI CÁP:", ["7x7", "7x19"])
        with col_st3:
            luc_keo_dut_kn = st.number_input("CƯỜNG LỰC KÉO ĐỨT 1 SỢI (kN):", value=15.8, step=0.5)
            khoi_luong_cap_g_m = st.number_input("KHỐI LƯỢNG CÁP (g/m):", value=61.0, step=1.0)

        so_soi = int((kho_st - 150) / buoc_cap)
        tong_chieu_dai_cap_m = so_soi * chieu_dai_st
        tong_tl_cap_kg = (tong_chieu_dai_cap_m * khoi_luong_cap_g_m) / 1000.0
        tong_luc_keo_kn = so_soi * luc_keo_dut_kn

        st.divider()
        st1, st2, st3 = st.columns(3)
        st1.metric("SỐ SỢI CÁP THÉP", f"{so_soi} sợi")
        st2.metric("TỔNG KHỐI LƯỢNG CÁP", f"{tong_tl_cap_kg:,.1f} kg")
        st3.metric("TỔNG LỰC KÉO ĐỨT", f"{tong_luc_keo_kn:,.1f} kN")

    with tab3:
        st.subheader("TRỌNG LƯỢNG 1 MÉT BĂNG & ĐƯỜNG KÍNH TANG TỐI THIỂU")
        c_tl1, c_tl2 = st.columns(2)
        with c_tl1:
            st.markdown("##### 1. Khối lượng 1m Băng Tải Vải")
            chon_vai = st.selectbox("LOẠI VẢI:", DF_TIEUCHUAN_VAI["LOAI_VAI"].tolist(), index=6)
            so_lop_b = st.number_input("SỐ LỚP BỐ VẢI:", value=4, min_value=1, max_value=8)
            kho_m = st.number_input("KHỔ RỘNG (mm):", value=800, step=50, key="m_kho") / 1000.0
            cs_tren_m = st.number_input("CAO SU TRÊN (mm):", value=4.0, key="m_cs_tr")
            cs_duoi_m = st.number_input("CAO SU DƯỚI (mm):", value=2.0, key="m_cs_du")
            tt_cs = st.number_input("TỶ TRỌNG CAO SU MẶT (g/cm³):", value=1.15, step=0.01)

            row_v = DF_TIEUCHUAN_VAI[DF_TIEUCHUAN_VAI["LOAI_VAI"] == chon_vai].iloc[0]
            tl_vai_1m = (row_v["TL_M2"] * so_lop_b * kho_m) / 1000.0
            tl_cs_1m = (kho_m * 1.0 * (cs_tren_m + cs_duoi_m) / 1000.0) * (tt_cs * 1000.0)
            tl_tong_1m = tl_vai_1m + tl_cs_1m

            st.success(f"Khối lượng vải: **{tl_vai_1m:.2f} kg/m** | Cao su mặt: **{tl_cs_1m:.2f} kg/m**")
            st.metric("TỔNG TRỌNG LƯỢNG 1 MÉT BĂNG", f"{tl_tong_1m:.2f} kg/m")

        with c_tl2:
            st.markdown("##### 2. Đường Kính Tang/Pully Tối Thiểu (D_min)")
            loai_loi = st.radio("LOẠI LÕI CHỊU LỰC:", ["BĂNG TẢI EP (VẢI)", "BĂNG TẢI LÕI THÉP (ST)"], horizontal=True)
            if loai_loi == "BĂNG TẢI EP (VẢI)":
                k_pully = st.slider("HỆ SỐ K (mm):", min_value=20, max_value=30, value=25)
                day_bang_tong = so_lop_b * row_v["BE_DAY"] + cs_tren_m + cs_duoi_m
                d_min_ly_thuyet_tab3 = k_pully * day_bang_tong
                d_pulley_chuan_tab3 = lam_tron_pulley_chuan(d_min_ly_thuyet_tab3)
                st.info(f"D_min tính toán: **{d_min_ly_thuyet_tab3:.1f} mm**")
                st.success(f"Đường kính Pulley tiêu chuẩn đề xuất: **Ø {d_pulley_chuan_tab3} mm**")
            else:
                alpha_pully = st.slider("HỆ SỐ α (THÉP):", min_value=120, max_value=150, value=140)
                dk_soi_th = st.number_input("ĐƯỜNG KÍNH SỢI CÁP (mm):", value=6.0, step=0.5)
                d_min_thep = dk_soi_th * alpha_pully
                d_pulley_thep_chuan = lam_tron_pulley_chuan(d_min_thep)
                st.info(f"D_min tính toán: **{d_min_thep:.1f} mm**")
                st.success(f"Đường kính Pulley tiêu chuẩn đề xuất: **Ø {d_pulley_thep_chuan} mm**")
    with tab4:
        st.subheader("⚡ TÍNH TOÁN CÔNG SUẤT CHUYÊN SÂU THEO TIÊU CHUẨN CEMA (RULMECA V7.24)")
        st.caption("BÓC TÁCH CHI TIẾT TỪNG THÀNH PHẦN LỰC CẢN VẬT LÝ & MÔ PHỎNG ĐƯỜNG RƠI PARABOL VẬT LIỆU")

        dong_bo = st.checkbox("🔗 ĐỒNG BỘ TOÀN BỘ THÔNG SỐ VỚI TAB 1 (DIN 22101)", value=True)

        c_cema1, c_cema2, c_cema3 = st.columns(3)
        with c_cema1:
            st.markdown("##### 📍 THÔNG SỐ CƠ BẢN (HỆ MÉT)")
            if dong_bo:
                B_cema_mm = float(B)
                L_cema_m = float(L_tuyen)
                Q_cema_th = float(Q)
                V_cema_ms = float(V)
                # Tự động tính H từ góc dốc alpha của Tab 1: H = L * sin(alpha)
                H_cema_m = float(L_tuyen * math.sin(math.radians(alpha_deg)))
                
                st.info(f"Đang đồng bộ từ Tab 1:\n- Khổ B: **{B_cema_mm:.0f} mm**\n- Tuyến L: **{L_cema_m:.2f} m**\n- Góc dốc: **{alpha_deg:.1f}°** $\\to$ Nâng cao H: **{H_cema_m:.2f} m**\n- Năng suất Q: **{Q_cema_th:.1f} t/h** | V: **{V_cema_ms:.2f} m/s**")
            else:
                B_cema_mm = st.number_input("KHỔ RỘNG BĂNG B (mm):", value=float(B), step=50.0, key="cema_B")
                L_cema_m = st.number_input("CHIỀU DÀI TUYẾN L (m):", value=float(L_tuyen), step=5.0, key="cema_L")
                Q_cema_th = st.number_input("NĂNG SUẤT Q (t/h):", value=float(Q), step=20.0, key="cema_Q")
                V_cema_ms = st.number_input("VẬN TỐC BĂNG V (m/s):", value=float(V), step=0.1, key="cema_V")
                H_cema_m = st.number_input("CHIỀU CAO NÂNG H (m):", value=float(L_tuyen * math.sin(math.radians(alpha_deg))), step=0.5, key="cema_H")

            w_in = B_cema_mm / 25.4

        with c_cema2:
            st.markdown("##### ⚙️ MA SÁT PHỤ CEMA")
            temp_c = st.number_input("NHIỆT ĐỘ MÔI TRƯỜNG (°C):", value=25.0, step=5.0)
            so_cleaner = st.number_input("SỐ LƯỢNG GẠT BĂNG (CLEANERS):", value=1, min_value=0, max_value=5)
            chieu_dai_skirt_m = st.number_input("CHIỀU DÀI TẤM CHẮN PHỄU (m):", value=3.66, step=0.5)
            be_sau_skirt_cm = st.number_input("ĐỘ DÀY LIỆU TẠI PHỄU (cm):", value=7.62, step=1.0)

        with c_cema3:
            st.markdown("##### 🎯 THÔNG SỐ TANG TRỐNG")
            # Đồng bộ đường kính Tang tiêu chuẩn vừa chọn ở Tab 1
            dk_default = float(d_pulley_chuan_mm) if (dong_bo and 'd_pulley_chuan_mm' in locals()) else 320.0
            dk_tang_cema_mm = st.number_input("ĐƯỜNG KÍNH TANG CHỦ ĐỘNG (mm):", value=dk_default, step=20.0)
            boc_cao_su_mm = st.number_input("BỀ DÀY BỌC CAO SU TANG (LAGGING) (mm):", value=8.0, step=1.0)
            hieu_suat_truyen = float(hieu_suat) if dong_bo else 0.94
            st.caption(f"Hiệu suất truyền động: **{hieu_suat_truyen:.2f}**")

        # Quy đổi và tính toán tiếp tục...
        Wb_lbs_ft = (m2_bang * 0.67197) if dong_bo else 9.0
        L_ft = L_cema_m * 3.28084
        Q_tph = Q_cema_th * 1.10231
        V_fpm = V_cema_ms * 196.85
        H_ft = H_cema_m * 3.28084
        skirt_len_ft = chieu_dai_skirt_m * 3.28084
        skirt_depth_in = be_sau_skirt_cm / 2.54

        # Trọng lượng vật liệu Wm (lbs/ft)
        Wm_lbs_ft = (Q_tph * 2000.0) / (60.0 * V_fpm) if V_fpm > 0 else 0
        Wb_lbs_ft = 9.0

        # Hệ số điều kiện CEMA
        temp_f = temp_c * 1.8 + 32.0
        Kt = 1.0 if temp_f >= 32 else (1.0 + (32.0 - temp_f) * 0.008)
        Kx = 0.494
        Ky = 0.025

        # Bóc tách 8 thành phần lực cản Te (lbs)
        Tx_lbs = L_ft * Kx * Kt
        Tyr_lbs = L_ft * Ky * Wb_lbs_ft * Kt
        Tyc_lbs = L_ft * Ky * (Wb_lbs_ft + Wm_lbs_ft) * Kt
        Th_lbs = Wm_lbs_ft * H_ft
        Tam_lbs = (Q_tph * V_fpm) / 3474.0
        Tsb_lbs = skirt_len_ft * (0.128 * (skirt_depth_in ** 2) + 0.15) * 6.0
        Tbc_lbs = so_cleaner * 180.0
        Tp_lbs = 20.0

        Te_lbs = Tx_lbs + Tyr_lbs + Tyc_lbs + Th_lbs + Tam_lbs + Tsb_lbs + Tbc_lbs + Tp_lbs
        Te_lbs = Tx_lbs + Tyr_lbs + Tyc_lbs + Th_lbs + Tam_lbs + Tsb_lbs + Tbc_lbs + Tp_lbs
        Te_kN = Te_lbs * 0.00444822

        # --- DÁN CỤM TÍNH LỰC CĂNG VẢI VÀO ĐÂY ---
        T2_lbs = 0.5 * Te_lbs  # Lực căng nhánh nhả theo hệ số Cw = 0.5
        T1_lbs = Te_lbs + T2_lbs
        luc_piw = T1_lbs / w_in
        luc_kgf_cm = (T1_lbs * 0.45359) / (B_cema_mm / 10.0)

        # Tính công suất điện và tổn hao
        HP_belt = (Te_lbs * V_fpm) / 33000.0
        HP_bearing = 0.03 * HP_belt + 0.05
        HP_gear = (HP_belt + HP_bearing) * (1.0 / hieu_suat_truyen - 1.0)
        HP_tong = HP_belt + HP_bearing + HP_gear
        P_tong_kW = HP_tong * 0.7457

        st.divider()
        st.markdown("#### 📊 BẢNG ĐỐI CHIẾU NĂNG LƯỢNG & LỰC CĂNG VẢI BỐ CEMA")
        rc1, rc2, rc3, rc4, rc5 = st.columns(5)
        rc1.metric("CÔNG SUẤT ĐỘNG CƠ", f"{P_tong_kW:.2f} kW", delta=f"{HP_tong:.2f} HP")
        rc2.metric("LỰC KÉO HIỆU DỤNG TE", f"{Te_kN:.2f} kN", delta=f"{Te_lbs:.0f} lbs")
        rc3.metric("LỰC CĂNG LỚN NHẤT T1", f"{T1_lbs * 0.00445:.2f} kN", delta=f"{T1_lbs:.0f} lbs")
        rc4.metric("CƯỜNG LỰC ĐƠN VỊ (CEMA)", f"{luc_piw:.1f} PIW")
        rc5.metric("LỰC CĂNG MÉP (XƯỞNG)", f"{luc_kgf_cm:.2f} kgf/cm")

        df_cema_luc = pd.DataFrame({
            "THÀNH PHẦN LỰC CẢN CEMA": [
                "Lực ma sát con lăn (Tx)", 
                "Lực cản uốn lượn nhánh không tải (Tyr)", 
                "Lực cản uốn lượn nhánh có tải (Tyc)", 
                "Lực nâng thẳng đứng (Th)", 
                "Lực gia tốc nạp liệu (Tam)", 
                "Lực ma sát tấm chắn liệu (Tsb)", 
                "Lực cản gạt dọn băng (Tbc)", 
                "Lực cản tang uốn phụ (Tp)"
            ],
            "GIÁ TRỊ (lbs)": [f"{Tx_lbs:.1f}", f"{Tyr_lbs:.1f}", f"{Tyc_lbs:.1f}", f"{Th_lbs:.1f}", f"{Tam_lbs:.1f}", f"{Tsb_lbs:.1f}", f"{Tbc_lbs:.1f}", f"{Tp_lbs:.1f}"],
            "GIÁ TRỊ QUY ĐỔI (kN)": [f"{Tx_lbs*0.00445:.2f}", f"{Tyr_lbs*0.00445:.2f}", f"{Tyc_lbs*0.00445:.2f}", f"{Th_lbs*0.00445:.2f}", f"{Tam_lbs*0.00445:.2f}", f"{Tsb_lbs*0.00445:.2f}", f"{Tbc_lbs*0.00445:.2f}", f"{Tp_lbs*0.00445:.2f}"],
            "TỶ TRỌNG (%)": [f"{(Tx_lbs/Te_lbs)*100:.1f}%", f"{(Tyr_lbs/Te_lbs)*100:.1f}%", f"{(Tyc_lbs/Te_lbs)*100:.1f}%", f"{(Th_lbs/Te_lbs)*100:.1f}%", f"{(Tam_lbs/Te_lbs)*100:.1f}%", f"{(Tsb_lbs/Te_lbs)*100:.1f}%", f"{(Tbc_lbs/Te_lbs)*100:.1f}%", f"{(Tp_lbs/Te_lbs)*100:.1f}%"]
        })
        st.table(df_cema_luc)

        # Mô phỏng quỹ đạo rơi vật liệu (CEMA Trajectory)
        st.markdown("#### 📈 MÔ PHỎNG ĐƯỜNG CONG QUỸ ĐẠO RƠI VẬT LIỆU (CEMA TRAJECTORY)")
        R_tong_m = (dk_tang_cema_mm / 2.0 + boc_cao_su_mm + 15.0) / 1000.0
        V_tang = V_cema_ms
        ly_tam = (V_tang ** 2) / (9.81 * R_tong_m)
        theta_deg = 0.0 if ly_tam >= 1.0 else math.degrees(math.acos(ly_tam))

        t_arr = np.linspace(0, 0.8, 25)
        vx0 = V_tang * math.cos(math.radians(theta_deg))
        vy0 = V_tang * math.sin(math.radians(theta_deg))
        x_m = vx0 * t_arr
        y_m = - (vy0 * t_arr + 0.5 * 9.81 * (t_arr ** 2))

        df_traj = pd.DataFrame({"KHOẢNG CÁCH BAY X (m)": x_m, "ĐỘ RƠI SÂU Y (m)": y_m})
        st.line_chart(df_traj.set_index("KHOẢNG CÁCH BAY X (m)"))
        st.caption(f"Góc văng vật liệu khỏi tang: **{theta_deg:.1f}°** | Vận tốc tiếp tuyến: **{V_tang:.2f} m/s**")
# ==============================================================================
# MODULE 2: CÔNG NGHỆ ÉP THỦY LỰC & LƯU HÓA CAO SU
# ==============================================================================
elif module_chon == "MODULE 2: CÔNG NGHỆ ÉP THỦY LỰC & LƯU HÓA CAO SU":
    st.title("🛑 MODULE 2: CÔNG NGHỆ ÉP THỦY LỰC & LƯU HÓA")
    st.caption("KIỂM TRA ÁP LỰC ÉP TRÊN KHUÔN, TÍNH KHỐI LƯỢNG PHÔI CAO SU & TRA CỨU DUNG SAI ISO 3302-1")

    tab_ep1, tab_ep2, tab_ep3 = st.tabs([
        "1. TÍNH LỰC ÉP THỦY LỰC & ĐỐI CHIẾU TIÊU CHUẨN",
        "2. TÍNH TOÁN TRỌNG LƯỢNG PHÔI CAO SU",
        "3. TRA CỨU DUNG SAI CAO SU (ISO 3302-1 / VDI-2005)"
    ])

    with tab_ep1:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("1. CHỌN MÁY ÉP & ÁP SUẤT")
            ten_cac_may = [m["TÊN MÁY"] for m in DANH_SACH_MAY_EP]
            may_da_chon = st.selectbox("DANH SÁCH MÁY ÉP TẠI XƯỞNG:", ten_cac_may)
            thong_tin_may = next(item for item in DANH_SACH_MAY_EP if item["TÊN MÁY"] == may_da_chon)
            
            c_xl1, c_xl2 = st.columns(2)
            with c_xl1:
                dk_xl = st.number_input("ĐƯỜNG KÍNH XI LANH (mm):", value=float(thong_tin_may["DK_XL_MM"]))
            with c_xl2:
                so_xl = st.number_input("SỐ LƯỢNG XI LANH:", value=int(thong_tin_may["SO_XL"]), step=1)

            ap_luc_dong_ho = st.number_input("ÁP LỰC ĐỒNG HỒ CÀI ĐẶT (kg/cm²):", value=float(thong_tin_may["AP_LUC_DEFAULT"]), step=5.0)
            st.caption(f"Kích thước bàn nhiệt máy: **{thong_tin_may['KICH_THUOC_BAN']} mm**")

        with col2:
            st.subheader("2. THÔNG SỐ KHUÔN & YÊU CẦU LƯU HÓA")
            c_k1, c_k2 = st.columns(2)
            with c_k1:
                dai_khuon = st.number_input("CHIỀU DÀI KHUÔN (cm):", value=104.0, step=1.0)
            with c_k2:
                rong_khuon = st.number_input("CHIỀU RỘNG KHUÔN (cm):", value=64.0, step=1.0)
            dien_tich_khuon = dai_khuon * rong_khuon
            st.info(f"Diện tích chiếu khuôn: **{dien_tich_khuon:,.1f} cm²**")

            do_cung = st.selectbox("ĐỘ CỨNG SẢN PHẨM (SHORE A):", ["SHORE A 40-50", "SHORE A 50-60", "SHORE A 60-70", "SHORE A 70-80"], index=1)
            do_phuc_tap = st.selectbox("KẾT CẤU GÂN / HOA VĂN:", ["ĐƠN GIẢN KHÔNG GÂN", "NHIỀU GÂN MỎNG"])

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

        st.divider()
        res1, res2, res3 = st.columns(3)
        res1.metric("TỔNG LỰC ÉP MÁY", f"{tong_luc_ep_kg/1000.0:,.1f} Tấn")
        res2.metric("LỰC ÉP TRÊN KHUÔN THỰC TẾ", f"{luc_ep_sp:.2f} kg/cm²")
        res3.metric("TIÊU CHUẨN QUY ĐỊNH", f"{min_qc} – {max_qc} kg/cm²")

        if luc_ep_sp < min_qc:
            st.error(f"❌ **THIẾU ÁP LỰC:** Lực ép thực tế ({luc_ep_sp:.1f} kg/cm²) nhỏ hơn mức tối thiểu ({min_qc} kg/cm²). Có nguy cơ rỗ khí, không liền mối.")
        elif luc_ep_sp > max_qc:
            st.warning(f"⚠️ **VƯỢT TIÊU CHUẨN:** Lực ép thực tế ({luc_ep_sp:.1f} kg/cm²) lớn hơn mức quy định ({max_qc} kg/cm²). Cần kiểm tra bavia và độ bền khuôn.")
        else:
            st.success(f"✅ **ĐẠT CHUẨN:** Áp lực ép thực tế nằm trong khoảng tối ưu ({min_qc} – {max_qc} kg/cm²).")

    with tab_ep2:
        st.subheader("TÍNH TOÁN TRỌNG LƯỢNG PHÔI CAO SU ĐỊNH HÌNH")
        loai_hinh = st.selectbox("CHỌN HÌNH DẠNG PHÔI:", ["HÌNH TRỤ TRÒN", "HÌNH TRỤ RỖNG (ỐNG)", "HÌNH HỘP CHỮ NHẬT", "HÌNH NÓN CỤT RỖNG"])
        
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            tt_phoi = st.number_input("TỶ TRỌNG CAO SU (g/cm³):", value=1.20, step=0.01)
            so_luong_phoi = st.number_input("SỐ LƯỢNG PHÔI CẦN CẮT:", value=1, min_value=1)
        
        with col_p2:
            the_tich_cm3 = 0.0
            if loai_hinh == "HÌNH TRỤ TRÒN":
                d_tru = st.number_input("ĐƯỜNG KÍNH (mm):", value=100.0)
                h_tru = st.number_input("CHIỀU CAO (mm):", value=60.0)
                the_tich_cm3 = (math.pi * ((d_tru/10/2)**2) * (h_tru/10))
            elif loai_hinh == "HÌNH TRỤ RỖNG (ỐNG)":
                d_ngoai = st.number_input("ĐƯỜNG KÍNH NGOÀI (mm):", value=60.0)
                d_trong = st.number_input("ĐƯỜNG KÍNH TRONG (mm):", value=27.2)
                h_ong = st.number_input("CHIỀU CAO (mm):", value=30.0)
                the_tich_cm3 = math.pi * (((d_ngoai/10/2)**2) - ((d_trong/10/2)**2)) * (h_ong/10)
            elif loai_hinh == "HÌNH HỘP CHỮ NHẬT":
                c1 = st.number_input("CHIỀU DÀI (mm):", value=150.0)
                c2 = st.number_input("CHIỀU RỘNG (mm):", value=80.0)
                c3 = st.number_input("CHIỀU DÀY (mm):", value=25.0)
                the_tich_cm3 = (c1/10) * (c2/10) * (c3/10)
            elif loai_hinh == "HÌNH NÓN CỤT RỖNG":
                D_lon = st.number_input("ĐK ĐÁY LỚN NGOÀI (mm):", value=152.0)
                d_lon_tr = st.number_input("ĐK ĐÁY LỚN TRONG (mm):", value=50.0)
                D_be = st.number_input("ĐK ĐÁY BÉ NGOÀI (mm):", value=76.0)
                d_be_tr = st.number_input("ĐK ĐÁY BÉ TRONG (mm):", value=50.0)
                h_non = st.number_input("CHIỀU CAO (mm):", value=150.2)
                
                V_ngoai = (1/3) * math.pi * (h_non/10) * (((D_lon/20)**2) + ((D_be/20)**2) + (D_lon/20)*(D_be/20))
                V_trong = (1/3) * math.pi * (h_non/10) * (((d_lon_tr/20)**2) + ((d_be_tr/20)**2) + (d_lon_tr/20)*(d_be_tr/20))
                the_tich_cm3 = V_ngoai - V_trong

        khoi_luong_1_phoi_g = the_tich_cm3 * tt_phoi
        tong_tl_phoi_kg = (khoi_luong_1_phoi_g * so_luong_phoi) / 1000.0

        st.divider()
        cp1, cp2 = st.columns(2)
        cp1.metric("KHỐI LƯỢNG 1 PHÔI", f"{khoi_luong_1_phoi_g:.2f} Gram")
        cp2.metric(f"TỔNG KHỐI LƯỢNG ({so_luong_phoi} PHÔI)", f"{tong_tl_phoi_kg:.3f} kg")

    with tab_ep3:
        st.subheader("TRA CỨU DUNG SAI KÍCH THƯỚC THEO TIÊU CHUẨN ISO 3302-1")
        kt_nhap = st.number_input("NHẬP KÍCH THƯỚC DANH NGHĨA SẢN PHẨM (mm):", value=42.0, step=1.0)
        ds = tra_cuu_iso_3302(kt_nhap)

        st.markdown(f"##### DUNG SAI KÍCH THƯỚC CHO SẢN PHẨM L = {kt_nhap} mm:")
        df_ds = pd.DataFrame({
            "CẤP CHÍNH XÁC": ["Cấp M1 (Rất chính xác)", "Cấp M2 (Chính xác)", "Cấp M3 (Tiêu chuẩn kỹ thuật)", "Cấp M4 (Thô)"],
            "DUNG SAI CHO PHÉP (± mm)": [f"± {ds['M1']:.2f}", f"± {ds['M2']:.2f}", f"± {ds['M3']:.2f}", f"± {ds['M4']:.2f}"],
            "PHẠM VI KÍCH THƯỚC (mm)": [
                f"{kt_nhap - ds['M1']:.2f} – {kt_nhap + ds['M1']:.2f}",
                f"{kt_nhap - ds['M2']:.2f} – {kt_nhap + ds['M2']:.2f}",
                f"{kt_nhap - ds['M3']:.2f} – {kt_nhap + ds['M3']:.2f}",
                f"{kt_nhap - ds['M4']:.2f} – {kt_nhap + ds['M4']:.2f}"
            ]
        })
        st.table(df_ds)

# ==============================================================================
# MODULE 3: CÔNG NGHỆ COMPOUND & TRUYỀN ĐỘNG ĐAI
# ==============================================================================
elif module_chon == "MODULE 3: CÔNG NGHỆ COMPOUND & TRUYỀN ĐỘNG ĐAI":
    st.title("🧪 MODULE 3: CÔNG NGHỆ COMPOUND & TRUYỀN ĐỘNG ĐAI")
    st.caption("TÍNH TOÁN ĐƠN COMPOUND LÝ THUYẾT & TRA CỨU DÂY ĐAI COURROIE ISO 4184")

    tab_cp1, tab_cp2 = st.tabs([
        "1. TÍNH ĐƠN PHA CHẾ COMPOUND CAO SU",
        "2. DÂY ĐAI COURROIE (ISO 4184-1992)"
    ])

    with tab_cp1:
        st.subheader("BẢNG TÍNH ĐƠN PHA CHẾ COMPOUND")
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
                "KHỐI LƯỢNG (kg)": st.column_config.NumberColumn(format="%.3f"),
                "TỶ TRỌNG RIÊNG": st.column_config.NumberColumn(format="%.3f")
            }
        )

        df_calc = df_editor.dropna(subset=["VẬT TƯ"]).copy()
        df_calc["KHỐI LƯỢNG (kg)"] = pd.to_numeric(df_calc["KHỐI LƯỢNG (kg)"], errors="coerce").fillna(0)
        df_calc["TỶ TRỌNG RIÊNG"] = pd.to_numeric(df_calc["TỶ TRỌNG RIÊNG"], errors="coerce").fillna(1.0)
        df_calc["THỂ TÍCH (Lít)"] = df_calc["KHỐI LƯỢNG (kg)"] / df_calc["TỶ TRỌNG RIÊNG"]

        m_tong = df_calc["KHỐI LƯỢNG (kg)"].sum()
        v_tong = df_calc["THỂ TÍCH (Lít)"].sum()
        df_calc["TỶ LỆ (%)"] = (df_calc["KHỐI LƯỢNG (kg)"] / m_tong * 100.0) if m_tong > 0 else 0
        d_compound = m_tong / v_tong if v_tong > 0 else 0

        st.divider()
        mc1, mc2, mc3 = st.columns(3)
        mc1.metric("TỔNG KHỐI LƯỢNG MẺ (M)", f"{m_tong:.3f} kg")
        mc2.metric("TỔNG THỂ TÍCH (V)", f"{v_tong:.3f} Lít")
        mc3.metric("TỶ TRỌNG LÝ THUYẾT (d)", f"{d_compound:.3f} g/cm³")

        st.dataframe(
            df_calc[["STT", "VẬT TƯ", "KHỐI LƯỢNG (kg)", "TỶ LỆ (%)", "TỶ TRỌNG RIÊNG", "THỂ TÍCH (Lít)"]],
            use_container_width=True,
            hide_index=True
        )

    with tab_cp2:
        st.subheader("TRA CỨU DÂY ĐAI THANG / COURROIE (ISO 4184-1992)")
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            ban_dai = st.selectbox("QUY CÁCH TIẾT DIỆN ĐAI:", ["BẢN A", "BẢN B", "BẢN C", "BẢN D", "BẢN E"], index=3)
            don_vi_nhap = st.radio("CÁCH NHẬP CHIỀU DÀI:", ["Theo Inch (La)", "Theo mm (La)"], horizontal=True)
            if don_vi_nhap == "Theo Inch (La)":
                la_inch = st.number_input("CHIỀU DÀI LA (inch):", value=358.0, step=1.0)
                la_mm = la_inch * 25.4
            else:
                la_mm = st.number_input("CHIỀU DÀI LA (mm):", value=9093.0, step=10.0)
                la_inch = la_mm / 25.4

        with col_c2:
            chenh_lech_map = {"BẢN A": 30.0, "BẢN B": 43.0, "BẢN C": 56.0, "BẢN D": 126.0, "BẢN E": 150.0}
            delta_l = chenh_lech_map.get(ban_dai, 126.0)
            li_mm = la_mm - delta_l
            li_inch = li_mm / 25.4
            dung_sai_mm = 0.005 * la_mm + 10.0

        st.divider()
        m_cr1, m_cr2, m_cr3 = st.columns(3)
        m_cr1.metric("CHIỀU DÀI NGOÀI LA", f"{la_mm:.0f} mm ({la_inch:.2f}\")")
        m_cr2.metric("CHIỀU DÀI TRONG LI", f"{li_mm:.0f} mm ({li_inch:.2f}\")")
        m_cr3.metric("DUNG SAI CHO PHÉP (ISO 4184)", f"± {dung_sai_mm:.1f} mm")
