import streamlit as st

st.set_page_config(
    page_title="Heritage Goal | BrahmiLens",
    page_icon="🏛️",
    layout="wide"
)

# --------------------------------------------------
# ELITE UI STYLING
# --------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');

    .stApp {
        background: radial-gradient(circle at top right, #1e2a3a 0%, #050505 100%);
        color: #f0f0f0;
        font-family: 'Space Grotesk', sans-serif;
    }

    .glass {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(15px);
        height: 100%;
    }

    .header-accent {
        color: #58a6ff;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.8rem;
    }

    .stat-box {
        text-align: center;
        padding: 20px;
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    .last-stat { border-right: none; }

    .wiki-card {
        background: linear-gradient(135deg, rgba(88,166,255,0.1) 0%, rgba(0,0,0,0) 100%);
        border-left: 4px solid #58a6ff;
        padding: 20px;
        margin: 20px 0;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# NAVIGATION & HEADER
# --------------------------------------------------
if st.button("← BACK TO COMMAND CENTER"):
    st.switch_page("app.py")

st.markdown("<h1 style='font-size: 3rem;'>Heritage Preservation<span style='color:#58a6ff'>_</span></h1>", unsafe_allow_html=True)
st.markdown("<p class='header-accent'>Digital Immortality for Ancient Scripts</p>", unsafe_allow_html=True)

# --------------------------------------------------
# HISTORICAL CONTEXT (WIKI DATA)
# --------------------------------------------------
st.markdown("""
<div class="wiki-card">
    "The Brahmi script is the ancestor of most of the 40 or so modern Indian languages, 
    including Devanagari, Bengali, and Tamil. Its decipherment by <b>James Prinsep</b> in 1837 
    unlocked the Edicts of Ashoka, revealing a lost era of non-violence and moral governance 
    that had been forgotten for nearly 2,000 years." 
    <br><small>— Historical Record Archival</small>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# MAIN CONTENT GRID
# --------------------------------------------------
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="glass">
        <p class="header-accent">01. The Problem</p>
        <h3 style="color: #ff4b4b;">The Erosion of Time</h3>
        <p style="opacity:0.8; line-height:1.6;">
            Thousands of Brahmi inscriptions are found on iron pillars, cave walls, and rock edicts 
            across South Asia. However, environmental degradation and urbanization are destroying 
            these artifacts faster than humans can catalog them.
        </p>
        <p style="opacity:0.8; line-height:1.6;">
            Current challenges include <b>weathering</b> (illegible characters), <b>fragmentation</b>, 
            and a critical shortage of epigraphists trained in Prakrit and early Brahmi variants.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass">
        <p class="header-accent">02. The Mission</p>
        <h3 style="color: #58a6ff;">Cognitive Archaeology</h3>
        <p style="opacity:0.8; line-height:1.6;">
            BrahmiLens utilizes <b>Convolutional Neural Networks (CNN)</b> to recognize patterns 
            invisible to the naked eye. Our goal is to create a bridge between:
        </p>
        <ul style="opacity:0.8; line-height:1.8;">
            <li><b>Neural Transcription:</b> Real-time decoding of faded rock edicts.</li>
            <li><b>Linguistic Mapping:</b> Connecting Brahmi to modern Devanagari.</li>
            <li><b>Open Access:</b> Making history searchable for global researchers.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------------------------------
# ETHICAL STATS
# --------------------------------------------------
st.markdown("""
<div class="glass">
    <div style="display: flex; justify-content: space-around; align-items: center;">
        <div class="stat-box">
            <h2 style="margin:0; color:#58a6ff;">3RD C. BCE</h2>
            <p style="font-size:0.8rem; opacity:0.6;">SCRIPTS ORIGIN</p>
        </div>
        <div class="stat-box">
            <h2 style="margin:0; color:#58a6ff;">98%</h2>
            <p style="font-size:0.8rem; opacity:0.6;">CNN ACCURACY TARGET</p>
        </div>
        <div class="stat-box">
            <h2 style="margin:0; color:#58a6ff;">ZERO</h2>
            <p style="font-size:0.8rem; opacity:0.6;">HISTORICAL ALTERATION</p>
        </div>
        <div class="stat-box last-stat">
            <h2 style="margin:0; color:#58a6ff;">GLOBAL</h2>
            <p style="font-size:0.8rem; opacity:0.6;">HERITAGE REACH</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
<div style="margin-top: 40px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px; text-align: center;">
    <p style="font-family: monospace; font-size: 0.7rem; opacity: 0.4; letter-spacing: 5px;">
        ETHICAL_AI // ARCHAEOLOGICAL_INTEGRITY // V.2.0.26
    </p>
</div>
""", unsafe_allow_html=True)