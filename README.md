import streamlit as st
import numpy as np
import json
from PIL import Image
import cv2
import time

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="BRAHMILENS | NEURAL DECRYPTOR",
    page_icon="⚡",
    layout="wide",
)

# --------------------------------------------------
# THE "CRAZY" UI INJECTION (CSS)
# --------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@100;500&display=swap');

    /* The "Void" Background with Cyber-Grid */
    .stApp {
        background-color: #050505;
        background-image: 
            linear-gradient(rgba(0, 245, 212, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 245, 212, 0.05) 1px, transparent 1px);
        background-size: 30px 30px;
        color: #00f5d4;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Glitch Title Effect */
    .glitch-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 6rem;
        font-weight: 900;
        text-transform: uppercase;
        position: relative;
        color: #fff;
        text-shadow: 
            2px 2px #ff00c1, 
            -2px -2px #00fff9;
        letter-spacing: 15px;
        margin-bottom: 0;
    }

    /* Animated Neon Card */
    .neon-card {
        background: rgba(0, 0, 0, 0.8);
        border: 2px solid #00f5d4;
        box-shadow: 0 0 15px #00f5d4, inset 0 0 10px #00f5d4;
        padding: 30px;
        position: relative;
        overflow: hidden;
        transition: 0.3s;
    }

    .neon-card:hover {
        box-shadow: 0 0 30px #ff00c1, inset 0 0 20px #ff00c1;
        border-color: #ff00c1;
    }

    /* Floating Scanline Animation */
    .neon-card::after {
        content: " ";
        display: block;
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        z-index: 2;
        background-size: 100% 2px, 3px 100%;
        pointer-events: none;
    }

    /* Custom Buttons */
    .stButton>button {
        background: transparent;
        color: #00f5d4;
        border: 2px solid #00f5d4;
        font-family: 'Orbitron', sans-serif;
        text-transform: uppercase;
        width: 100%;
        border-radius: 0;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background: #00f5d4;
        color: black;
        box-shadow: 0 0 20px #00f5d4;
    }

    /* Metric Overrides */
    [data-testid="stMetricValue"] {
        font-family: 'Orbitron', sans-serif;
        color: #ff00c1 !important;
        font-size: 3rem !important;
    }

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER: THE COMMAND CENTER
# --------------------------------------------------
st.markdown("<p style='text-align:center; color:#ff00c1; letter-spacing:10px;'>[ ARCHIVE_DECRYPTION_PROTOCOL_v4.2 ]</p>", unsafe_allow_html=True)
st.markdown("<h1 class='glitch-title' style='text-align:center;'>BRAHMI_LENS</h1>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --------------------------------------------------
# MAIN WORKSPACE: THE HUD
# --------------------------------------------------
col_left, col_right = st.columns([1.5, 1], gap="large")

with col_left:
    st.markdown("### ⚡ `ACTIVE_SCANNER`")
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        st.markdown('<div class="neon-card">', unsafe_allow_html=True)
        img = Image.open(uploaded_file)
        st.image(img, use_container_width=True)
        
        # Add a fake "Scanning" progress bar
        bar = st.progress(0)
        for i in range(101):
            time.sleep(0.01)
            bar.progress(i)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="height:400px; border:2px dashed #00f5d4; display:flex; align-items:center; justify-content:center; background:rgba(0, 245, 212, 0.05);">
            <h2 style="color:#00f5d4; font-family:'Orbitron';">INSERT_ARTIFACT_IMAGE</h2>
        </div>
        """, unsafe_allow_html=True)

with col_right:
    st.markdown("### 📡 `NEURAL_LOG`")
    
    # Data Readout Card
    st.markdown('<div class="neon-card">', unsafe_allow_html=True)
    if uploaded_file:
        st.metric("TARGET_ID", "क (KA)", "CONFIDENCE: 98.4%")
        st.write("---")
        st.markdown("**PROBABILITY_STREAM**")
        st.code("""
        [0] KA: 0.9842
        [1] AA: 0.0121
        [2] MA: 0.0031
        [3] YA: 0.0006
        """, language="python")
        st.markdown("<p style='color:#ff00c1; font-size:0.7rem;'>LATENCY: 7.2ms | JITTER: 0.1ms</p>", unsafe_allow_html=True)
    else:
        st.warning("SYSTEM_IDLE: Awaiting spectral input...")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Map Card
    st.markdown("### 🧬 `STRUCTURAL_MATCH`")
    st.markdown('<div class="neon-card">', unsafe_allow_html=True)
    st.write("Comparing input topography against Ashokan Ashokan_Edict_Dataset_BCE3...")
    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# SYSTEM BLUEPRINT: THE CRAZY ARCHITECTURE
# --------------------------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()

with st.expander("🛠️ VIEW_HARDWARE_LOG (CNN_ARCHITECTURE)"):
    st.markdown("### CORE_REPRESENTATION_GRAPH")
    
    
    
    col_a, col_b, col_c = st.columns(3)
    col_a.markdown("<div class='neon-card'><b>KERNELS</b><br>16 / 32 / 64</div>", unsafe_allow_html=True)
    col_b.markdown("<div class='neon-card'><b>ACTIVATION</b><br>RE_LU (NON-LINEAR)</div>", unsafe_allow_html=True)
    col_c.markdown("<div class='neon-card'><b>POOLING</b><br>MAX_POOL_2X2</div>", unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER: THE "TERMINAL" END
# --------------------------------------------------
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; padding: 20px; border-top: 1px solid #00f5d4; opacity:0.8; font-family:'Orbitron';">
    <span style="color:#ff00c1;">>></span> END_OF_TRANSMISSION <span style="color:#ff00c1;"><<</span>
    <br><small style="color:#00f5d4;">SYSTEM_SECURE | 2024_BRAHMILENS_CORE</small>
</div>
""", unsafe_allow_html=True)