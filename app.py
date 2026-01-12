import streamlit as st
import numpy as np
import json
import cv2
import os
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
# ENHANCED "CYBER-ANTIQUITY" CSS
# --------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;700&family=Noto+Serif:ital@0;1&display=swap');
    
    .stApp {
        background: #0a0b10;
        background-image: 
            radial-gradient(at 0% 0%, rgba(88, 166, 255, 0.15) 0, transparent 50%), 
            radial-gradient(at 50% 0%, rgba(188, 133, 255, 0.1) 0, transparent 50%),
            radial-gradient(at 100% 0%, rgba(0, 212, 255, 0.15) 0, transparent 50%);
    }

    h1, h2, h3, p {
        font-family: 'Space Grotesk', sans-serif !important;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(20px);
        border-radius: 28px;
        padding: 2.5rem;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
    }

    .main-title {
        font-size: 4.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #fff 30%, #58a6ff 70%, #bc85ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -2px;
    }

    .result-text {
        font-family: 'Noto Serif', serif;
        font-size: 4.5rem;
        color: #ffffff;
        text-shadow: 0 0 30px rgba(88, 166, 255, 0.6);
        background: rgba(0,0,0,0.2);
        border-radius: 15px;
        padding: 40px 20px;
        margin: 20px 0;
        border: 1px dashed rgba(255,255,255,0.1);
    }

    .status-badge {
        background: linear-gradient(90deg, rgba(88, 166, 255, 0.1), rgba(188, 133, 255, 0.1));
        border: 1px solid rgba(88, 166, 255, 0.5);
        color: #58a6ff;
        padding: 6px 16px;
        border-radius: 100px;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# OCR CORE
# --------------------------------------------------
def segment_characters(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 15, 8
    )
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    boxes = []
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if h > 15 and w > 8:
            boxes.append((x, y, w, h))

    boxes = sorted(boxes, key=lambda b: b[0])
    return boxes, thresh

# --------------------------------------------------
# LOAD MODEL & LABELS (FIXED FOR STREAMLIT CLOUD)
# --------------------------------------------------
@st.cache_resource
def load_resources():
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        MODEL_PATH = os.path.join(BASE_DIR, "brahmi_char_369_v1.h5")
        LABEL_PATH = os.path.join(BASE_DIR, "index_to_label_v1.json")

        model = load_model(MODEL_PATH)

        with open(LABEL_PATH, encoding="utf-8") as f:
            labels = json.load(f)
            labels = {int(k): v for k, v in labels.items()}

        return model, labels

    except Exception as e:
        st.error(f"🚨 Model loading error: {e}")
        return None, None

model, index_to_label = load_resources()
IMG_SIZE = 64

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown('<h1 class="main-title">BrahmiLens</h1>', unsafe_allow_html=True)
st.markdown(
    '<p style="color:#8b949e;font-size:1.4rem;">Where Ancient Scripts meet Neural Networks</p>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# MAIN WORKSPACE
# --------------------------------------------------
if model is None:
    st.error("🚨 System Failure: Neural Weights Missing. Check 'brahmi_char_369_v1.h5'.")
    st.stop()

col1, col2 = st.columns([1, 1.3], gap="large")

with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    file = st.file_uploader("Drop your Brahmi manuscript here", type=["png", "jpg", "jpeg"])
    if file:
        pil_image = Image.open(file).convert("RGB")
        st.image(pil_image, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if file:
        img = np.array(pil_image)
        boxes, thresh = segment_characters(img)

        st.markdown(
            f'<span class="status-badge">Neural Scan: {len(boxes)} Glyphs Found</span>',
            unsafe_allow_html=True
        )

        sentence = ""
        prev_end = None

        for (x, y, w, h) in boxes:
            if prev_end is not None and x - prev_end > 25:
                sentence += " "

            char_img = thresh[y:y+h, x:x+w]
            char_img = cv2.resize(char_img, (IMG_SIZE, IMG_SIZE))
            char_img = char_img.astype("float32") / 255.0
            char_img = char_img.reshape(1, IMG_SIZE, IMG_SIZE, 1)

            pred = model.predict(char_img, verbose=0)
            label = index_to_label[int(np.argmax(pred))]
            sentence += label
            prev_end = x + w

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📝 Neural Decryption")
        st.markdown(f'<div class="result-text">{sentence}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.markdown(
            '<div class="glass-card" style="text-align:center;padding:120px 20px;">'
            '<h2 style="color:rgba(255,255,255,0.3);">INITIALIZE SCAN...</h2>'
            '</div>',
            unsafe_allow_html=True
        )
