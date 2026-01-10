import streamlit as st
import numpy as np
import json
from PIL import Image
from tensorflow.keras.models import load_model

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="BrahmiLens | Neural Heritage",
    page_icon="📜",
    layout="wide"
)

# --------------------------------------------------
# ELITE UI STYLING (CAZTO-INSPIRED)
# --------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');

    .stApp {
        background: radial-gradient(circle at top right, #1e2a3a 0%, #050505 100%);
        color: #f0f0f0;
        font-family: 'Space Grotesk', sans-serif;
    }

    /* Professional Glass Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 2rem;
        backdrop-filter: blur(20px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        margin-bottom: 20px;
    }

    /* Hero Typography */
    .hero-title {
        font-size: 4rem;
        font-weight: 700;
        letter-spacing: -2px;
        background: linear-gradient(135deg, #fff 30%, #58a6ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }

    /* Prediction Result Styling */
    .prediction-value {
        font-size: 6rem;
        font-weight: 700;
        color: #58a6ff;
        text-shadow: 0 0 30px rgba(88,166,255,0.4);
        line-height: 1;
        margin: 10px 0;
    }

    /* Custom Streamlit Button Overrides */
    div.stButton > button {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        color: white;
        padding: 20px;
        border-radius: 15px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    div.stButton > button:hover {
        background: #58a6ff;
        color: black;
        border-color: #58a6ff;
        transform: scale(1.02);
    }

    /* Scanline effect for images */
    .img-scan {
        border-radius: 15px;
        border: 2px solid #58a6ff;
        position: relative;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# RESOURCES
# --------------------------------------------------
@st.cache_resource
def load_resources():
    # Replace with your actual model/json paths
    try:
        model = load_model("brahmi_cnn_final.h5")
        with open("index_to_label.json", encoding="utf-8") as f:
            data = json.load(f)
            index_to_label = {int(k): v for k, v in data.items()}
        return model, index_to_label
    except:
        return None, None

model, index_to_label = load_resources()
IMG_SIZE = 64

# --------------------------------------------------
# UI LAYOUT
# --------------------------------------------------
st.markdown("<h1 class='hero-title'>BrahmiLens<span style='color:#58a6ff'>.</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='opacity:0.6; font-size:1.2rem; margin-top:-10px;'>Neural Transcription Engine v2.0</p>", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown("### 🛰️ INPUT STREAM")
    file = st.file_uploader("Drop manuscript fragment here...", type=["png", "jpg", "jpeg"])
    
    if file:
        image = Image.open(file)
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.image(image, use_container_width=True, caption="Source Fragment")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("System Offline: Please upload a Brahmi character to initialize scanning.")

with col2:
    st.markdown("### 💎 DATA ANALYSIS")
    
    if file and model:
        # Preprocessing
        img = image.convert("L").resize((IMG_SIZE, IMG_SIZE))
        arr = np.array(img) / 255.0
        arr = arr.reshape(1, IMG_SIZE, IMG_SIZE, 1)

        # Logic
        preds = model.predict(arr, verbose=0)[0]
        top = np.argmax(preds)
        conf = preds[top] * 100

        st.markdown(f"""
        <div class='glass-card' style='text-align:center'>
            <span style='text-transform:uppercase; letter-spacing:2px; font-size:0.8rem; opacity:0.7'>Identified Glyph</span>
            <div class='prediction-value'>{index_to_label[top]}</div>
            <div style='background:rgba(88,166,255,0.1); padding:10px; border-radius:10px; color:#58a6ff; font-weight:bold'>
                {conf:.2f}% Match Probability
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("PROBABILITY SPECTRUM"):
            for i in np.argsort(preds)[-4:][::-1]:
                st.write(f"**{index_to_label[i]}**")
                st.progress(float(preds[i]))
    else:
        st.markdown("""
        <div class='glass-card' style='height:280px; display:flex; align-items:center; justify-content:center; opacity:0.5'>
            Waiting for Optical Data...
        </div>
        """, unsafe_allow_html=True)

# --------------------------------------------------
# NAVIGATION (TECH CARDS)
# --------------------------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
nav_cols = st.columns(3)

nav_items = [
    ("🧬 Neural Map", "3_🧬_Neural_Map.py"),
    ("📖 Phonetic Bridge", "4_📖_Phonetic_Bridge.py"),
    ("🏛️ Heritage Goal", "5_🏛️_Heritage_Goal.py")
]

for i, (label, path) in enumerate(nav_items):
    with nav_cols[i]:
        if st.button(label, use_container_width=True):
            st.switch_page(f"pages/{path}")

st.markdown("""
<div style='text-align:center; margin-top:50px; opacity:0.3; font-size:0.8rem; letter-spacing:4px'>
    TERMINAL // 0X-BRAHMI-STREAMS // SECURE_NODE
</div>
""", unsafe_allow_html=True)