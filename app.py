import streamlit as st
import json
from pathlib import Path

# ==================================================
# CONFIG
# ==================================================

st.set_page_config(
    page_title="MNR Seguimiento",
    page_icon="🖥️",
    layout="centered"
)

# ==================================================
# COLORES MNR
# ==================================================

APP_BLUE = "#1b2f7b"
BACKGROUND = "#081229"
CARD = "#111c36"
TEXT = "#f8fafc"
MUTED = "#94a3b8"

# ==================================================
# CSS PREMIUM
# ==================================================

st.markdown(f"""
<style>

html, body, [class*="css"] {{
    font-family: 'Segoe UI', sans-serif;
}}

.stApp {{
    background: linear-gradient(
        180deg,
        #081229 0%,
        #0b1731 100%
    );
    color: white;
}}

.block-container {{
     padding-top: 1rem;
    padding-bottom: 1rem;
}}

.main-card {{
     background: rgba(17, 28, 54, 0.95);
    padding: 18px;
    border-radius: 20px;
    margin-bottom: 14px;
}}

.title {{
    color: white;
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    margin-top: 10px;
}}

.subtitle {{
    color: {MUTED};
    text-align: center;
    font-size: 17px;
    margin-bottom: 40px;
}}

.card-title {{
    color: white;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 16px;
}}

.status {{
    font-size: 34px;
    font-weight: 800;
    color: white;
    margin-bottom: 15px;
}}

.info {{
    color: {TEXT};
    font-size: 17px;
    line-height: 1.7;
}}

.footer {{
    text-align: center;
    color: {MUTED};
    margin-top: 45px;
    font-size: 14px;
}}

.message-box {{
    border-left: 4px solid {APP_BLUE};
    padding-left: 16px;
    margin-top: 10px;
}}

.logo-glow {{
    text-align: center;
    font-size: 58px;
    margin-bottom: 5px;
    filter: drop-shadow(0px 0px 10px rgba(59,130,246,0.45));
}}

</style>
""", unsafe_allow_html=True)

# ==================================================
# LEER ID
# ==================================================

query_params = st.query_params

ord_id = query_params.get("id", "MNR-1032")

# ==================================================
# BUSCAR JSON
# ==================================================

json_path = Path("../seguimientos") / f"{ord_id}.json"

st.write("Buscando archivo en:")
st.write(json_path.resolve())
if not json_path.exists():
    st.error("No se encontró el seguimiento solicitado.")
    st.stop()

with open(json_path, "r", encoding="utf-8") as f:
    dados = json.load(f)

# ==================================================
# COLOR ESTADO
# ==================================================

estado = dados["estado"]

if "Listo" in estado:
    estado_color = "#22c55e"

elif "Esperando" in estado:
    estado_color = "#f97316"

elif "diagnóstico" in estado.lower():
    estado_color = "#eab308"

else:
    estado_color = "#3b82f6"

# ==================================================
# HEADER
# ==================================================

st.markdown(
    f"""
    <div class='logo-glow'>🖥️</div>
    <div class='title'>MNR COMPUTACIÓN</div>
    <div class='subtitle'>
        Seguimiento de equipos en tiempo real
    </div>
    """,
    unsafe_allow_html=True
)

# ==================================================
# ESTADO
# ==================================================

st.markdown("<div class='main-card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='card-title'>Estado actual</div>",
    unsafe_allow_html=True
)

st.markdown(
    f'''
    <div class='status' style='color:{estado_color};'>
        {estado}
    </div>
    ''',
    unsafe_allow_html=True
)

st.progress(int(dados["progreso"]) / 100)

st.markdown(
    f"""
    <div class='info' style='margin-top:10px;'>
        {dados["progreso"]}% completado
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# EQUIPO
# ==================================================

st.markdown("<div class='main-card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='card-title'>Equipo</div>",
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class='info'>
        💻 {dados["equipo"]}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class='info'>
        👤 {dados["cliente"]}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# MENSAJE
# ==================================================

st.markdown("<div class='main-card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='card-title'>Última actualización</div>",
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class='message-box'>
        <div class='info'>
            {dados["mensaje"]}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# CONTACTO
# ==================================================

st.markdown("<div class='main-card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='card-title'>Contacto</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='info'>
        📍 Paraná, Entre Ríos<br><br>
        📸 Instagram: @mnr.computacion<br><br>
        📱 WhatsApp: 3434602256
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# FOOTER
# ==================================================

st.markdown(
    """
    <div class='footer'>
        MNR Computación • Servicio técnico profesional
    </div>
    """,
    unsafe_allow_html=True
)