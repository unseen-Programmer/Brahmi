import streamlit as st

st.set_page_config(
    page_title="History of Brahmi | BrahmiLens",
    page_icon="📜",
    layout="wide"
)

# --------------------------------------------------
# ELITE UI STYLING
# --------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');

    .stApp {
        background: radial-gradient(circle at top left, #2b1b17 0%, #050505 100%);
        color: #f0f0f0;
        font-family: 'Space Grotesk', sans-serif;
    }

    .glass {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(15px);
        margin-bottom: 25px;
    }

    .history-accent {
        color: #d4af37; 
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.8rem;
    }

    .timeline-node {
        border-left: 2px solid #d4af37;
        padding-left: 20px;
        margin-left: 10px;
        position: relative;
        padding-bottom: 20px;
    }

    .timeline-node::before {
        content: '';
        position: absolute;
        left: -6px;
        top: 0;
        width: 10px;
        height: 10px;
        background: #d4af37;
        border-radius: 50%;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------
if st.button("← RETURN TO COMMAND CENTER"):
    st.switch_page("app.py")

st.markdown("<h1 style='font-size: 3.5rem;'>Chronicles of Brahmi<span style='color:#d4af37'>.</span></h1>", unsafe_allow_html=True)
st.markdown("<p class='history-accent'>Tracing the Mother of Indic Scripts</p>", unsafe_allow_html=True)

# --------------------------------------------------
# THE GENESIS SECTION
# --------------------------------------------------
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 🏛️ The Mauryan Foundation")
    st.markdown("""
    <div class="glass">
        <p style="opacity:0.8; line-height:1.7;">
            Brahmi emerged as the primary vehicle for the <b>Edicts of Ashoka</b> (r. 268–232 BCE). 
            These inscriptions were not just religious texts but administrative decrees of a 
            pan-Indian empire. They were carved onto massive sandstone pillars and natural 
            rock faces from the Himalayas to the Deccan.
        </p>
        <p style="opacity:0.8; line-height:1.7;">
            The script was a remarkable feat of <b>phonetic engineering</b>, designed to capture 
            the Prakrit dialects spoken across the subcontinent with scientific precision.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # st.image("assets/ashoka_pillar.jpg", caption="Historical Pillar Detail")

with col2:
    st.markdown("### 🕰️ Timeline of Evolution")
    
    st.markdown("""
    <div class="timeline-node">
        <b style="color:#d4af37;">3rd Century BCE:</b><br>
        Ashokan Brahmi reaches its peak as a standardized imperial script.
    </div>
    <div class="timeline-node">
        <b style="color:#d4af37;">2nd Century CE:</b><br>
        Evolution into Kushana and Satavahana variants, beginning the process of regional stylization.
    </div>
    <div class="timeline-node">
        <b style="color:#d4af37;">4th Century CE:</b><br>
        The Gupta Script emerges, adding 'matras' (headbars) that eventually led to Devanagari.
    </div>
    <div class="timeline-node">
        <b style="color:#d4af37;">1837 CE:</b><br>
        James Prinsep successfully deciphers the script, reopening India's ancient history.
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# THE GLOBAL IMPACT
# --------------------------------------------------
st.markdown("---")
st.markdown("### 🌏 A Continental Legacy")

# st.image("assets/brahmi_evolution_map.png", use_container_width=True)

st.markdown("""
<div class="glass">
    <div style="display: flex; justify-content: space-around; text-align: center;">
        <div>
            <h4 style="color:#d4af37; margin-bottom:5px;">Northern Branch</h4>
            <p style="font-size:0.9rem; opacity:0.7;">Devanagari, Gurmukhi,<br>Bengali, Tibetan</p>
        </div>
        <div>
            <h4 style="color:#d4af37; margin-bottom:5px;">Southern Branch</h4>
            <p style="font-size:0.9rem; opacity:0.7;">Tamil, Telugu, Kannada,<br>Malayalam, Sinhala</p>
        </div>
        <div>
            <h4 style="color:#d4af37; margin-bottom:5px;">S.E. Asian Branch</h4>
            <p style="font-size:0.9rem; opacity:0.7;">Khmer, Thai, Javanese,<br>Balinese, Baybayin</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# WHY AI MATTERS
# --------------------------------------------------
st.markdown("### 🤖 The Digital Renaissance")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="glass" style="height:250px;">
        <h5 style="color:#d4af37;">Weathering Recovery</h5>
        <p style="font-size:0.85rem; opacity:0.8;">
            Archaeological sites face "Optical Noise." AI can filter out centuries of erosion 
            and physical damage to identify the original chiseled intent of the scribe.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="glass" style="height:250px;">
        <h5 style="color:#d4af37;">Speed of Analysis</h5>
        <p style="font-size:0.85rem; opacity:0.8;">
            A single pillar can take weeks to manually transcribe. BrahmiLens performs 
            initial character identification in milliseconds, allowing experts to focus 
            on linguistic context.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="glass" style="height:250px;">
        <h5 style="color:#d4af37;">Universal Access</h5>
        <p style="font-size:0.85rem; opacity:0.8;">
            By converting physical stone into digital data, we ensure that these 
            Ashokan values of 'Dharma' are searchable for the next thousand years.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center; opacity:0.3; font-family:monospace; margin-top:50px; letter-spacing:5px;">
ARCHIVE_ENTRY // BRAHMI_TIMELINE // STATUS_COMPLETED
</p>
""", unsafe_allow_html=True)    