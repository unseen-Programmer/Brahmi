import streamlit as st

st.set_page_config(
    page_title="Neural Map | BrahmiLens",
    page_icon="🧬",
    layout="wide"
)

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

st.markdown("""
<style>
.glass {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 28px;
    backdrop-filter: blur(14px);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("## 🧬 The Neural Map")
st.caption("How BrahmiLens *sees* ancient scripts")

st.markdown("""
<div class="glass">
<h3>🧠 Convolutional Vision Pipeline</h3>
<p>
BrahmiLens uses a compact CNN optimized for <b>low-contrast stone inscriptions</b>.
Instead of deep residual stacks, the network focuses on <b>stroke topology</b>,
curvature, and terminal hooks—features critical to Brahmi glyphs.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glass">
<h3>🔍 Feature Hierarchy</h3>
<ul>
<li><b>Layer 1</b>: Edge & stroke orientation detection</li>
<li><b>Layer 2</b>: Shape abstraction & curvature grouping</li>
<li><b>Dense Bottleneck</b>: 64D latent script embedding</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glass">
<h3>⚙ Why Not ResNet / ViT?</h3>
<p>
Ancient scripts exhibit <b>low intra-class variance</b>.
Heavier models tend to hallucinate noise patterns.
This architecture prioritizes <b>interpretability, stability, and speed</b>.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center; opacity:0.5; font-family:monospace">
NEURAL_MAP :: CNN_VISION_STACK :: VERIFIED
</p>
""", unsafe_allow_html=True)
st.markdown("---")