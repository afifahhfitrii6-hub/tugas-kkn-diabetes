import csv
import math
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "dataset_pasien.csv"
K = 3

st.set_page_config(page_title="SPK Risiko Diabetes", page_icon="🩺", layout="wide")

st.markdown("""
<style>
.stApp {background:linear-gradient(135deg,#fff7fb,#fff 55%,#fff0f7);color:#4c2440}
.main .block-container {max-width:1100px;padding-top:1.5rem}
.hero {background:linear-gradient(120deg,#d93687,#f16aa9);color:white;padding:26px 30px;border-radius:20px;margin-bottom:20px}
.hero h1,.hero p {color:white}
div[data-testid="stMetric"] {background:#fff6fb;border:1px solid #f4d6e6;padding:12px;border-radius:12px}
div.stButton>button,div.stFormSubmitButton>button,div.stDownloadButton>button {background:#e94f9b;color:white;border:0;border-radius:10px;font-weight:700}
[data-testid="stHeader"] {background:transparent}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>Sistem Pendukung Keputusan Risiko Diabetes</h1>
<p>Aplikasi klasifikasi menggunakan algoritma K-Nearest Neighbors (KNN). Bisa dibuka melalui browser HP maupun laptop.</p>
</div>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    rows = []
    with DATA_FILE.open(encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            rows.append({
                "id": r["ID Pasien"],
                "x": [float(r["Usia"]), float(r["BMI"]), float(r["Glukosa"]),
                      float(r["Tekanan Darah"]), float(r["Riwayat Keluarga"])],
                "label": r["Kelas"].strip().capitalize()
            })
    return rows

def predict(patient, rows):
    mins = [min(r["x"][i] for r in rows) for i in range(5)]
    maxs = [max(r["x"][i] for r in rows) for i in range(5)]
    ranked = []
    for row in rows:
        dist2 = 0
        for i, value in enumerate(patient):
            span = maxs[i] - mins[i]
            a = (value - mins[i]) / span if span else 0
            b = (row["x"][i] - mins[i]) / span if span else 0
            dist2 += (a - b) ** 2
        ranked.append({"ID Pasien": row["id"], "Kelas": row["label"], "Jarak": math.sqrt(dist2)})
    ranked.sort(key=lambda r: r["Jarak"])
    nearest = ranked[:min(K, len(ranked))]
    high = sum(r["Kelas"] == "Tinggi" for r in nearest)
    low = len(nearest) - high
    return ("Tinggi" if high > low else "Rendah"), nearest, high, low

try:
    dataset = load_data()
except Exception as exc:
    st.error(f"Dataset tidak bisa dibaca. Pastikan data/dataset_pasien.csv ada. Detail: {exc}")
    st.stop()

left, right = st.columns([1, 1], gap="large")
with left:
    st.subheader("Input Data Pasien")
    st.caption("Masukkan data yang ingin diklasifikasikan.")
    with st.form("input_pasien"):
        c1, c2 = st.columns(2)
        with c1:
            age = st.number_input("Usia (tahun)", min_value=1, max_value=120, value=42)
            glucose = st.number_input("Glukosa (mg/dL)", min_value=20, max_value=600, value=130)
        with c2:
            bmi = st.number_input("BMI", min_value=10.0, max_value=80.0, value=28.5, step=0.1)
            bp = st.number_input("Tekanan darah (mmHg)", min_value=30, max_value=300, value=128)
        family = st.selectbox("Riwayat diabetes dalam keluarga", [0, 1],
                              format_func=lambda x: "Tidak ada (0)" if x == 0 else "Ada (1)", index=1)
        submitted = st.form_submit_button("Hitung Prediksi Risiko", use_container_width=True)

with right:
    st.subheader("Hasil Prediksi")
    st.caption("Menggunakan K = 3 tetangga terdekat.")
    if submitted:
        label, neighbors, high, low = predict([float(age), float(bmi), float(glucose), float(bp), float(family)], dataset)
        if label == "Tinggi":
            st.error(f"Hasil klasifikasi: RISIKO {label.upper()}")
        else:
            st.success(f"Hasil klasifikasi: RISIKO {label.upper()}")
        st.write(f"Dari tetangga terdekat: **{high} Tinggi** dan **{low} Rendah**.")
        st.dataframe([{**r, "Jarak": round(r["Jarak"], 4)} for r in neighbors],
                     hide_index=True, use_container_width=True)
    else:
        st.info("Masukkan data pasien lalu tekan tombol prediksi.")
    st.metric("Nilai K", K)

st.divider()
st.subheader("Dataset Pelatihan")
st.caption("Riwayat keluarga: 0 = tidak ada, 1 = ada. Data ini merupakan dataset contoh tugas kuliah.")
st.dataframe([{
    "ID Pasien": r["id"], "Usia": r["x"][0], "BMI": r["x"][1],
    "Glukosa": r["x"][2], "Tekanan Darah": r["x"][3],
    "Riwayat Keluarga": int(r["x"][4]), "Kelas": r["label"]
} for r in dataset], hide_index=True, use_container_width=True)

with DATA_FILE.open("rb") as f:
    st.download_button("Unduh Dataset CSV", f.read(), "dataset_pasien.csv", "text/csv")

st.warning("Catatan: aplikasi ini hanya simulasi pembelajaran dengan dataset kecil, bukan alat diagnosis medis.")
st.caption("Proyek SPK · Python + Streamlit + KNN")
