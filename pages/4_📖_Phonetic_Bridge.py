import streamlit as st

st.set_page_config(
    page_title="Phonetic Bridge | BrahmiLens",
    page_icon="📖",
    layout="wide"
)

# --------------------------------------------------
# ELITE UI STYLING
# --------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');

    .stApp {
        background: radial-gradient(circle at top right, #1a2a2a 0%, #050505 100%);
        color: #f0f0f0;
        font-family: 'Space Grotesk', sans-serif;
    }

    .glass {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(15px);
        margin-bottom: 20px;
    }

    .header-accent {
        color: #00ffcc;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.8rem;
    }

    .evolution-box {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(0, 255, 204, 0.05);
        padding: 15px;
        border-radius: 12px;
        border: 1px dashed rgba(0, 255, 204, 0.3);
        margin: 10px 0;
    }

    .glyph-large {
        font-size: 2.5rem;
        font-weight: bold;
        color: #00ffcc;
    }
    
    .arrow { color: rgba(255,255,255,0.3); font-size: 1.5rem; }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# NAVIGATION
# --------------------------------------------------
if st.button("← BACK TO COMMAND CENTER"):
    st.switch_page("app.py")

st.markdown("<h1 style='font-size: 3rem;'>Phonetic Bridge<span style='color:#00ffcc'>_</span></h1>", unsafe_allow_html=True)
st.markdown("<p class='header-accent'>Synchronizing Ancient Glyphs with Modern Phonology</p>", unsafe_allow_html=True)

# --------------------------------------------------
# LINGUISTIC CONTEXT
# --------------------------------------------------
st.markdown("""
<div class="glass">
    <p class="header-accent">Archival Intel</p>
    <p style="opacity:0.8; line-height:1.6;">
        Brahmi is an <b>Abugida</b> script—each character represents a consonant with an inherent vowel 'a'. 
        As the script migrated across the Silk Road and maritime routes, it branched into two main lineages: 
        the <b>Northern (Gupta, Nagari)</b> and <b>Southern (Pallava, Kadamba)</b>. 
        The "Bridge" uses neural logic to reverse-engineer these 2,000-year-old phonemes into 
        ISO-standardized International Alphabet of Sanskrit Transliteration (IAST).
    </p>
</div>
""", unsafe_allow_html=True)



# --------------------------------------------------
# EVOLUTION VISUALIZER
# --------------------------------------------------
col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.markdown("### 🛰️ Genetic Lineage")
    st.markdown("""
    <div class="glass">
        <div class="evolution-box">
            <div><small style="display:block; opacity:0.5">Brahmi</small><span class="glyph-large">𑀓</span></div>
            <div class="arrow">→</div>
            <div><small style="display:block; opacity:0.5">Devanagari</small><span class="glyph-large">क</span></div>
            <div class="arrow">→</div>
            <div><small style="display:block; opacity:0.5">IAST</small><span class="glyph-large">Ka</span></div>
        </div>
        <div class="evolution-box">
            <div><small style="display:block; opacity:0.5">Brahmi</small><span class="glyph-large">𑀫</span></div>
            <div class="arrow">→</div>
            <div><small style="display:block; opacity:0.5">Devanagari</small><span class="glyph-large">म</span></div>
            <div class="arrow">→</div>
            <div><small style="display:block; opacity:0.5">IAST</small><span class="glyph-large">Ma</span></div>
        </div>
        <div class="evolution-box">
            <div><small style="display:block; opacity:0.5">Brahmi</small><span class="glyph-large">𑀥</span></div>
            <div class="arrow">→</div>
            <div><small style="display:block; opacity:0.5">Devanagari</small><span class="glyph-large">ध</span></div>
            <div class="arrow">→</div>
            <div><small style="display:block; opacity:0.5">IAST</small><span class="glyph-large">Dha</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🧠 Linguistic Logic")
    st.markdown("""
    <div class="glass">
        <h4>Consonant Classification</h4>
        <p style="opacity:0.7; font-size:0.9rem;">The neural engine classifies Brahmi characters based on their articulatory position:</p>
        <table style="width:100%; border-collapse: collapse; margin-top:10px;">
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                <th style="text-align:left; padding:10px;">Class</th>
                <th style="text-align:left; padding:10px;">Phonemes</th>
            </tr>
            <tr>
                <td style="padding:10px; color:#00ffcc;">Velar</td>
                <td style="padding:10px;">Ka, Kha, Ga, Gha</td>
            </tr>
            <tr>
                <td style="padding:10px; color:#00ffcc;">Palatal</td>
                <td style="padding:10px;">Ca, Cha, Ja, Jha</td>
            </tr>
            <tr>
                <td style="padding:10px; color:#00ffcc;">Retroflex</td>
                <td style="padding:10px;">Ṭa, Ṭha, Ḍa, Ḍha</td>
            </tr>
            <tr>
                <td style="padding:10px; color:#00ffcc;">Labial</td>
                <td style="padding:10px;">Pa, Pha, Ba, Bha</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# FUTURE EXTENSIONS
# --------------------------------------------------
st.markdown("### 🌍 Universal Mapping Protocol")
c1, c2, c3 = st.columns(3)

with c1:
    st.info("**IAST Translation**\n\nMapping Brahmi directly to the International Alphabet of Sanskrit Transliteration for academic rigor.")
with c2:
    st.success("**Dravidian Connection**\n\nTracing the evolution into the Grantha script and modern Tamil/Telugu/Kannada forms.")
with c3:
    st.warning("**Pali/Prakrit Synthesis**\n\nReconstructing the spoken dialects of the Mauryan Empire from visual glyphs.")

st.markdown("""
<div style="margin-top: 40px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px; text-align: center;">
    <p style="font-family: monospace; font-size: 0.7rem; opacity: 0.4; letter-spacing: 5px;">
        PHONETIC_BRIDGE // LINGUISTIC_ENGINE // ACTIVE
    </p>
</div>
""", unsafe_allow_html=True)