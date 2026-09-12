import streamlit as st
import numpy as np
import pandas as pd
import math

st.set_page_config(page_title="HỆ THỐNG TÍNH KỸ THUẬT CAO SU & BĂNG TẢI", layout="wide", page_icon="⚙️")

# ==============================================================================
# DỮ LIỆU TIÊU CHUẨN (TIEU CHUAN & AP LUC MAY)
# ==============================================================================
DF_TIEUCHUAN_VAI = pd.DataFrame([
    {"LOAI_VAI": "EP100", "LUC_CHON": 0,   "LUC_THUC": 100, "BE_DAY": 1.00},
    {"LOAI_VAI": "EP125", "LUC_CHON": 100, "LUC_THUC": 125, "BE_DAY": 1.15},
    {"LOAI_VAI": "EP150", "LUC_CHON": 125, "LUC_THUC": 150, "BE_DAY": 1.20},
    {"LOAI_VAI": "EP200", "LUC_CHON": 150, "LUC_THUC": 200, "BE_DAY": 1.40},
    {"LOAI_VAI": "EP250", "LUC_CHON": 200, "LUC_THUC": 250, "BE_DAY": 1.45},
    {"LOAI_VAI": "EP300", "LUC_CHON": 250, "LUC_THUC": 300, "BE_DAY": 1.50},
    {"LOAI_VAI": "EP350", "LUC_CHON": 300, "LUC_THUC": 350, "BE_DAY": 1.55},
    {"LOAI_VAI": "EP400", "LUC_CHON": 350, "LUC_THUC": 400, "BE_DAY": 1.65},
    {"LOAI_VAI": "EP500", "LUC_CHON": 400, "LUC_THUC": 500, "BE_DAY": 1.70},
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

# ==============================================================================
# MENU ĐIỀU HƯỚNG BÊN TRÁI (IN HOA CÁC TAB)
# ==============================================================================
st.sidebar.title("🛠️ MENU HỆ THỐNG")
lua_chon = st.sidebar.radio(
    "CHỌN MODULE TÍNH TOÁN:",
    [
        "1. THIẾT KẾ BĂNG TẢI & ĐỘNG CƠ (DIN 22101)",
        "2. ÁP LỰC MÁY ÉP THỦY LỰC & LƯU HÓA",
        "3. TÍNH TOÁN CÔNG THỨC ĐƠN COMPOUND"
    ]
)

# ==============================================================================
# MODULE 1: THIẾT KẾ BĂNG TẢI & ĐỘNG CƠ (DIN 22101)
# ==============================================================================
if lua_chon == "1. THIẾT KẾ BĂNG TẢI & ĐỘNG CƠ (DIN 22101)":
    st.title("⚡ THIẾT KẾ TUYẾN BĂNG TẢI & TÍNH CÔNG SUẤT ĐỘNG CƠ")
    st.caption("TIÊU CHUẨN DIN 22101 - TÍNH TOÁN LỰC CĂNG, SF KHỞI ĐỘNG VÀ ĐỀ XUẤT KẾT CẤU VẢI BỐ")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("THÔNG SỐ TUYẾN BĂNG")
        B = st.number_input("KHỔ RỘNG BĂNG B (mm):", value=800, step=50)
        CVLT = st.number_input("CHU VI LIỀN TRÒN CVLT (m):", value=400.0, step=10.0)
        L_tuyen = CVLT / 2.0
        st.info(f"CHIỀU DÀI TUYẾN BĂNG (L/2): **{L_tuyen:.1f} m**")
        alpha_deg = st.number_input("GÓC DỐC BĂNG TẢI (°):", value=23.0, step=1.0)

    with col2:
        st.subheader("THÔNG SỐ VẬN HÀNH")
        Q = st.number_input("NĂNG SUẤT Q (t/h):", value=400.0, step=10.0)
        V = st.number_input("VẬN TỐC BĂNG V (m/s):", value=1.0, step=0.1)
        mu = st.number_input("HỆ SỐ MA SÁT CON LĂN (f):", value=0.07, step=0.01, format="%.2f")
        he_so_an_toan = st.number_input("HỆ SỐ AN TOÀN (SF):", value=6.0, step=0.5)

    with col3:
        st.subheader("KẾT CẤU BĂNG TẢI")
        cao_su_tren = st.number_input("BỀ DÀY CAO SU MẶT TRÊN (mm):", value=4.0, step=0.5)
        cao_su_duoi = st.number_input("BỀ DÀY CAO SU MẶT DƯỚI (mm):", value=2.0, step=0.5)
        hieu_suat_truyen_dong = st.number_input("HIỆU SUẤT TRUYỀN ĐỘNG (η):", value=0.85, step=0.05)
        he_so_vai = 0.95

    # Tính toán
    tl_bang_kg_m = B * 0.0125
    m_vat_lieu_kg_m = (Q * 1000.0) / (3600.0 * V)
    sf_start = tinh_sf_start(L_tuyen)

    alpha_rad = math.radians(alpha_deg)
    sin_alpha = math.sin(alpha_rad)
    chieu_cao_nang = sin_alpha * L_tuyen

    F_kN = ((tl_bang_kg_m + m_vat_lieu_kg_m) * L_tuyen * 9.81 * (mu + sin_alpha)) / 1000.0
    P_dong_co_kW = (F_kN * V / hieu_suat_truyen_dong) * sf_start
    luc_keo_kgf_cm = (F_kN * sf_start * 101.972) / (B / 10.0)

    luc_yeu_cau_tong = luc_keo_kgf_cm * he_so_an_toan * he_so_vai
    vai_3p = f"3P({tra_cuu_vai(luc_yeu_cau_tong / 3.0)})"
    vai_4p = f"4P({tra_cuu_vai(luc_yeu_cau_tong / 4.0)})"
    vai_5p = f"5P({tra_cuu_vai(luc_yeu_cau_tong / 5.0)})"

    matched_row = DF_TIEUCHUAN_VAI[DF_TIEUCHUAN_VAI["LOAI_VAI"] == tra_cuu_vai(luc_yeu_cau_tong / 5.0)].iloc[0]
    be_day_tong_mm = 5 * matched_row["BE_DAY"] + cao_su_tren + cao_su_duoi
    quy_cach_de_xuat = f"B{int(B)} x 5P({matched_row['LOAI_VAI']}) x ({int(cao_su_tren)}+{int(cao_su_duoi)}) x {be_day_tong_mm:.1f}mm : CVLT = {CVLT:.0f}m"

    st.divider()
    st.subheader("📊 KẾT QUẢ TÍNH TOÁN KỸ THUẬT")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("CÔNG SUẤT ĐỘNG CƠ", f"{P_dong_co_kW:.1f} kW")
    m2.metric("TỔNG LỰC KÉO F", f"{F_kN:.2f} kN")
    m3.metric("LỰC CĂNG ĐƠN VỊ", f"{luc_keo_kgf_cm:.2f} kgf/cm")
    m4.metric("CHIỀU CAO NÂNG (H)", f"{chieu_cao_nang:.2f} m")

    st.markdown("#### 🎯 GỢI Ý PHƯƠNG ÁN KẾT CẤU VẢI BỐ")
    df_phuong_an = pd.DataFrame({
        "KẾT CẤU": ["PHƯƠNG ÁN 3 LỚP (3P)", "PHƯƠNG ÁN 4 LỚP (4P)", "PHƯƠNG ÁN 5 LỚP (5P) [KHUYẾN NGHỊ]"],
        "QUY CÁCH VẢI BỐ": [vai_3p, vai_4p, vai_5p],
        "LỰC CĂNG PHÂN BỔ/LỚP (kgf/cm)": [f"{luc_yeu_cau_tong/3:.1f}", f"{luc_yeu_cau_tong/4:.1f}", f"{luc_yeu_cau_tong/5:.1f}"],
        "HỆ SỐ KHỞI ĐỘNG SF": [f"{sf_start:.3f}", f"{sf_start:.3f}", f"{sf_start:.3f}"]
    })
    st.table(df_phuong_an)
    st.success(f"📌 **QUY CÁCH BĂNG TẢI HOÀN CHỈNH XUẤT XƯỞNG:** `{quy_cach_de_xuat}`")

# ==============================================================================
# MODULE 2: ÁP LỰC MÁY ÉP THỦY LỰC & LƯU HÓA
# ==============================================================================
elif lua_chon == "2. ÁP LỰC MÁY ÉP THỦY LỰC & LƯU HÓA":
    st.title("🛑 TÍNH TOÁN ÁP LỰC ÉP THỦY LỰC & KIỂM TRA LƯU HÓA")
    st.caption("KIỂM TRA ÁP LỰC TRUYỀN LÊN DIỆN TÍCH KHUÔN SO VỚI QUY ĐỊNH LƯU HÓA CAO SU")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. THÔNG SỐ MÁY ÉP")
        ten_cac_may = [m["TÊN MÁY"] for m in DANH_SACH_MAY_EP]
        may_da_chon = st.selectbox("CHỌN MÁY ÉP XƯỞNG:", ten_cac_may)
        
        thong_tin_may = next(item for item in DANH_SACH_MAY_EP if item["TÊN MÁY"] == may_da_chon)
        
        col_xl1, col_xl2 = st.columns(2)
        with col_xl1:
            dk_xl = st.number_input("ĐƯỜNG KÍNH XI LANH (mm):", value=float(thong_tin_may["DK_XL_MM"]))
        with col_xl2:
            so_xl = st.number_input("SỐ LƯỢNG XI LANH:", value=int(thong_tin_may["SO_XL"]), step=1)

        ap_luc_dong_ho = st.number_input("ÁP LỰC CÀI ĐẶT ĐỒNG HỒ (kg/cm²):", value=float(thong_tin_may["AP_LUC_DEFAULT"]), step=5.0)
        st.caption(f"KÍCH THƯỚC BÀN NHIỆT MÁY: **{thong_tin_may['KICH_THUOC_BAN']} mm**")

    with col2:
        st.subheader("2. THÔNG SỐ KHUÔN & SẢN PHẨM")
        loai_nhap_khuon = st.radio("CÁCH NHẬP KÍCH THƯỚC KHUÔN:", ["DÀI x RỘNG (cm)", "DIỆN TÍCH TRỰC TIẾP (cm²)"], horizontal=True)
        if loai_nhap_khuon == "DÀI x RỘNG (cm)":
            c_k1, c_k2 = st.columns(2)
            with c_k1:
                dai_khuon = st.number_input("CHIỀU DÀI KHUÔN (cm):", value=104.0, step=1.0)
            with c_k2:
                rong_khuon = st.number_input("CHIỀU RỘNG KHUÔN (cm):", value=64.0, step=1.0)
            dien_tich_khuon = dai_khuon * rong_khuon
        else:
            dien_tich_khuon = st.number_input("DIỆN TÍCH CHIẾU KHUÔN (cm²):", value=6656.0, step=50.0)

        st.info(f"DIỆN TÍCH KHUÔN TÍNH TOÁN: **{dien_tich_khuon:,.1f} cm²**")

        do_cung = st.selectbox("ĐỘ CỨNG SẢN PHẨM (Shore A):", ["SHORE A 40-50", "SHORE A 50-60", "SHORE A 60-70", "SHORE A 70-80"], index=1)
        do_phuc_tap = st.selectbox("MỨC ĐỘ PHỨC TẠP HOA VĂN KHUÔN:", ["ĐƠN GIẢN KHÔNG GÂN", "NHIỀU GÂN MỎNG"])

    # Tính toán
    r_cm = (dk_xl / 10.0) / 2.0
    s_piston_cm2 = (r_cm ** 2) * math.pi
    tong_luc_ep_kg = (s_piston_cm2 * ap_luc_dong_ho) * so_xl
    luc_ep_thuc_te_kg_cm2 = tong_luc_ep_kg / dien_tich_khuon if dien_tich_khuon > 0 else 0

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
    st.subheader("📋 ĐÁNH GIÁ ÁP LỰC LƯU HÓA")

    res1, res2, res3 = st.columns(3)
    res1.metric("TỔNG LỰC ÉP MÁY", f"{tong_luc_ep_kg/1000.0:,.1f} Tấn")
    res2.metric("LỰC ÉP TRÊN KHUÔN THỰC TẾ", f"{luc_ep_thuc_te_kg_cm2:.2f} kg/cm²")
    res3.metric("TIÊU CHUẨN QUI ĐỊNH", f"{min_qc} – {max_qc} kg/cm²")

    if luc_ep_thuc_te_kg_cm2 < min_qc:
        st.warning(f"⚠️ **THIẾU ÁP LỰC:** Lực ép thực tế ({luc_ep_thuc_te_kg_cm2:.1f} kg/cm²) thấp hơn mức tối thiểu ({min_qc} kg/cm²). Có nguy cơ rỗ khí, không điền đầy hoa văn khuôn!")
    elif luc_ep_thuc_te_kg_cm2 > max_qc:
        st.info(f"ℹ️ **ÁP LỰC CAO:** Lực ép thực tế ({luc_ep_thuc_te_kg_cm2:.1f} kg/cm²) cao hơn mức tiêu chuẩn ({max_qc} kg/cm²). Cần chú ý bavia mỏng hoặc biến dạng khuôn.")
    else:
        st.success(f"✅ **ĐẠT CHUẨN:** Áp lực ép thực tế ({luc_ep_thuc_te_kg_cm2:.1f} kg/cm²) nằm trong dải làm việc tối ưu ({min_qc} – {max_qc} kg/cm²).")

# ==============================================================================
# MODULE 3: TÍNH TOÁN ĐƠN PHA CHẾ COMPOUND
# ==============================================================================
elif lua_chon == "3. TÍNH TOÁN CÔNG THỨC ĐƠN COMPOUND":
    st.title("🧪 TÍNH ĐƠN PHA CHẾ COMPOUND CAO SU & TỶ TRỌNG LÝ THUYẾT")
    st.caption("TÍNH TOÁN TỶ LỆ % KHỐI LƯỢNG, THỂ TÍCH RIÊNG TỪNG CẤU TỬ VÀ TỶ TRỌNG TỔNG CỦA MẺ LUYỆN")

    data_mau = [
        {"STT": 1, "VẬT TƯ": "CAO SU SBR1712", "KHỐI LƯỢNG (kg)": 10.0, "TỶ TRỌNG RIÊNG": 0.945},
        {"STT": 2, "VẬT TƯ": "CAO SU TÁI SINH CS TS", "KHỐI LƯỢNG (kg)": 30.0, "TỶ TRỌNG RIÊNG": 1.210},
        {"STT": 3, "VẬT TƯ": "THAN N330", "KHỐI LƯỢNG (kg)": 5.0, "TỶ TRỌNG RIÊNG": 1.950},
        {"STT": 4, "VẬT TƯ": "BỘT MÀI CAO SU", "KHỐI LƯỢNG (kg)": 37.5, "TỶ TRỌNG RIÊNG": 1.300},
        {"STT": 5, "VẬT TƯ": "BÔNG CHỈ", "KHỐI LƯỢNG (kg)": 5.0, "TỶ TRỌNG RIÊNG": 1.000},
        {"STT": 6, "VẬT TƯ": "DẦU PARAFIN", "KHỐI LƯỢNG (kg)": 2.0, "TỶ TRỌNG RIÊNG": 0.880},
        {"STT": 7, "VẬT TƯ": "PHÒNG LÃO RD", "KHỐI LƯỢNG (kg)": 0.375, "TỶ TRỌNG RIÊNG": 1.050},
        {"STT": 8, "VẬT TƯ": "ACID STEARIC", "KHỐI LƯỢNG (kg)": 0.25, "TỶ TRỌNG RIÊNG": 0.980},
        {"STT": 9, "VẬT TƯ": "LƯU HUỲNH (S)", "KHỐI LƯỢNG (kg)": 0.8, "TỶ TRỌNG RIÊNG": 2.070},
    ]

    edited_df = st.data_editor(
        pd.DataFrame(data_mau),
        num_rows="dynamic",
        use_container_width=True,
        column_config={
            "KHỐI LƯỢNG (kg)": st.column_config.NumberColumn(format="%.3f"),
            "TỶ TRỌNG RIÊNG": st.column_config.NumberColumn(format="%.3f")
        }
    )

    df_calc = edited_df.dropna(subset=["VẬT TƯ"]).copy()
    df_calc["KHỐI LƯỢNG (kg)"] = pd.to_numeric(df_calc["KHỐI LƯỢNG (kg)"], errors="coerce").fillna(0)
    df_calc["TỶ TRỌNG RIÊNG"] = pd.to_numeric(df_calc["TỶ TRỌNG RIÊNG"], errors="coerce").fillna(1.0)
    
    df_calc["THỂ TÍCH (Lít)"] = df_calc["KHỐI LƯỢNG (kg)"] / df_calc["TỶ TRỌNG RIÊNG"]
    
    tong_khoi_luong = df_calc["KHỐI LƯỢNG (kg)"].sum()
    tong_the_tich = df_calc["THỂ TÍCH (Lít)"].sum()
    
    if tong_khoi_luong > 0:
        df_calc["TỶ LỆ (%)"] = (df_calc["KHỐI LƯỢNG (kg)"] / tong_khoi_luong) * 100.0
    else:
        df_calc["TỶ LỆ (%)"] = 0.0

    ty_trong_compound = tong_khoi_luong / tong_the_tich if tong_the_tich > 0 else 0.0

    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.metric("TỔNG KHỐI LƯỢNG MẺ (M)", f"{tong_khoi_luong:.3f} kg")
    c2.metric("TỔNG THỂ TÍCH (V)", f"{tong_the_tich:.3f} Lít")
    c3.metric("TỶ TRỌNG LÝ THUYẾT (d)", f"{ty_trong_compound:.3f} g/cm³")

    st.markdown("#### 📋 CHI TIẾT TỶ LỆ CÔNG THỨC COMPOUND")
    st.dataframe(
        df_calc[["STT", "VẬT TƯ", "KHỐI LƯỢNG (kg)", "TỶ LỆ (%)", "TỶ TRỌNG RIÊNG", "THỂ TÍCH (Lít)"]],
        use_container_width=True,
        hide_index=True
    )
