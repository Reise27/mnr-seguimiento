import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import base64

st.set_page_config(
    page_title="MNR Seguimiento",
    page_icon="🖥️",
    layout="wide"
)


def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = get_base64("logo.png")

query_params = st.query_params
ord_id = query_params.get("id", "ORD-2026-0024")

json_path = Path("../seguimientos") / f"{ord_id}.json"

if not json_path.exists():
    st.error("No se encontró el seguimiento solicitado.")
    st.stop()

with open(json_path, "r", encoding="utf-8") as f:
    dados = json.load(f)

fecha_actual = datetime.now().strftime("%d/%m/%Y - %H:%M hs")

estado = dados["estado"]

if "listo" in estado.lower():
    estado_color = "#22c55e"
elif "esperando" in estado.lower():
    estado_color = "#f97316"
elif "diagnóstico" in estado.lower():
    estado_color = "#eab308"
else:
    estado_color = "#3b82f6"

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(59,130,246,0.15), transparent 30%),
        radial-gradient(circle at top right, rgba(37,99,235,0.10), transparent 25%),
        #020b24;
    color: white;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

.glass {
    background: rgba(10, 20, 45, 0.72);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(59,130,246,0.18);
    border-radius: 24px;
    padding: 28px;
    box-shadow:
        0 0 25px rgba(0,0,0,0.35),
        0 0 40px rgba(59,130,246,0.06);
    margin-bottom: 24px;
}

.title {
    font-size: 48px;
    font-weight: 800;
    color: white;
}

.subtitle {
    font-size: 18px;
    color: #9ca3af;
    margin-top: 5px;
}

.card-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 20px;
}

.estado {
    font-size: 38px;
    font-weight: 800;
}

.info {
    color: #d1d5db;
    line-height: 1.8;
    font-size: 17px;
}

.logo {
    width: 240px;
}

.fecha {
    text-align: right;
    color: #cbd5e1;
    font-size: 16px;
}

.progreso {
    font-size: 16px;
    margin-top: 12px;
    color: #cbd5e1;
}

.footer {
    text-align: center;
    color: #64748b;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3,1])

with col1:

    inside1, inside2 = st.columns([1,2])

    with inside1:
        st.image("logo.png", width=220)

    with inside2:

        st.markdown("""
        <div style='padding-top:40px'>

        <div style="
        font-size:52px;
        font-weight:800;
        color:white;
        ">
            MNR Computación
        </div>

        <div style="
        font-size:24px;
        color:#94a3b8;
        margin-top:10px;
        ">
            Seguimiento de equipos
        </div>

        </div>
        """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="glass">
        <div class="card-title">
            🕒 Última actualización
        </div>
        <div class="fecha">
            {fecha_actual}
        </div>
    </div>
    """, unsafe_allow_html=True)

left, right = st.columns([1,1.3])

with left:
    st.markdown(f"""
    <div class="glass">
        <div class="card-title">
            📦 Orden de servicio
        </div>
        <div class="title">
            {dados["orden"]}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="glass">
        <div class="card-title">
            💻 Información del equipo
        </div>
        <div class="info">
            <b>Cliente:</b> {dados["cliente"]}<br><br>
            <b>Equipo:</b> {dados["equipo"]}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="glass">
        <div class="card-title">
            ⚡ Estado actual
        </div>
        <div class="estado" style="color:{estado_color}">
            {estado}
        </div>
        <br>
        <div class="info">
            {dados["mensaje"]}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass">
        <div class="card-title">
            📈 Progreso general
        </div>
    """, unsafe_allow_html=True)

    st.progress(int(dados["progreso"]) / 100)

    st.markdown(f"""
        <div class="progreso">
            {dados["progreso"]}% completado
        </div>
    </div>
    """, unsafe_allow_html=True)

with right:

    st.subheader("🧾 Historial del seguimiento")

    st.markdown("")

    st.markdown(
        f"""
### <span style='color:{estado_color}'>{estado}</span>

{dados["mensaje"]}

<div style='color:#94a3b8; font-size:14px'>
{fecha_actual}
</div>
""",
        unsafe_allow_html=True
    )

st.markdown("""
<div class="footer">
    MNR Computación • Servicio técnico profesional
</div>
""", unsafe_allow_html=True)
