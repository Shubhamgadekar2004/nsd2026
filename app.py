import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Battle of Brilliance | National Science Day 2026",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="auto"
)

# --- Force consistent theme ---
st.markdown("""
<style>
html, body, [class*="st-"], .stApp {
    background-color: #ffffff !important;
    color: #000000 !important;
}
h1, h2, h3, h4 {
    color: #003366 !important;
}
.stButton button {
    background-color: #1E90FF !important;
    color: white !important;
    border-radius: 8px !important;
    padding: 10px 20px !important;
    font-size: 16px !important;
}
.footer {
    text-align: center;
    margin-top: 20px;
    padding: 10px;
    color: #003366;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
with st.container():
    col1, col2 = st.columns([2, 5])
    with col1:
        logo_path = Path(__file__).parent / "logo.png"
        if logo_path.exists():
            st.image(str(logo_path), use_container_width=True)
        else:
            st.warning("logo.png not found in the app directory")
    with col2:
        st.markdown("""
        <div style="text-align:center;">
            <h2>National Forensic Sciences University, Goa Campus</h2>
            <h3>Organizing</h3>
            <h1 style="color:#c2185b;">“Battle of Brilliance”</h1>
            <h3>An Inter-School Competition on the occasion of</h3>
            <h2 style="color:#f4b400;">National Science Day 2026</h2>
            <p style="font-size:16px;">
                📅 <b>3rd March 2026</b>
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# ================= ABOUT =================
st.subheader("📌 About the Event")
st.write("""
**Battle of Brilliance** is an **inter-school competition** organized by  
**National Forensic Sciences University, Goa Campus** on the occasion of  
**National Science Day 2026**.

The event aims to encourage scientific thinking, creativity, innovation,
and competitive spirit among school students through quiz, model, and
drawing competitions.
""")
# ============ OBJECTIVES ============
st.subheader("🎯 Objectives")

st.write("""
**National Science Day** is celebrated to spread awareness about the importance
of science and its impact on everyday life. The day commemorates the discovery
of the **Raman Effect** by **Sir C. V. Raman** on **28 February 1928**, for which
he was awarded the **Nobel Prize in Physics in 1930**.

The celebration of National Science Day at **National Forensic Sciences
University (NFSU), Goa Campus** aims to achieve the following objectives:
""")

st.markdown("""
1. **Promote scientific awareness** among the general public, especially students and young minds.  
2. **Conduct scientific outreach activities** through NFSU Goa to promote forensic science as an emerging and impactful field in the state of Goa.  
3. **Encourage scientific temper**, innovation, creativity, and research-oriented thinking.  
4. **Highlight the importance and role of NFSU Goa** in strengthening the Indian judicial and criminal justice system through science and technology.  
5. **Inspire youth to pursue careers in science and research**, with a special focus on forensic science and cybersecurity programmes offered by NFSU Goa.  
6. **Bridge the gap between science and society** by making scientific knowledge accessible and engaging for learners at all levels.  
7. **Establish a strong bond between Goan culture and tradition and the forensic science community** at NFSU Goa, fostering local engagement and inclusivity.
""")

# ================= COMPETITIONS =================
st.subheader("🏆 Competitions & Prize Money")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🧠 Quiz Competition
    **Prize Money**
    - 🥇 1st: ₹4000/-
    - 🥈 2nd: ₹3000/-
    - 🥉 3rd: ₹2000/-
    """)

with col2:
    st.markdown("""
    ### 🔬 Model Competition
    **Prize Money**
    - 🥇 1st: ₹6000/-
    - 🥈 2nd: ₹4000/-
    - 🥉 3rd: ₹3000/-
    """)

with col3:
    st.markdown("""
    ### 🎨 Drawing Competition
    **Prize Money**
    - 🥇 1st: ₹2000/-
    - 🥈 2nd: ₹1500/-
    - 🥉 3rd: ₹1000/-
    """)

# ================= REGISTRATION FEES =================
st.subheader("💰 Registration Fees")

st.markdown("""
- **Quiz Competition:** ₹200 / Team  
- **Model Competition:** ₹500 / Team  
- **Drawing Competition:** ₹100 / Person  
""")

# ================= AWARD =================
st.subheader("🏅 Special Award")
st.success("🏆 **Winner Shield will be awarded to the Best School**")

# ================= REGISTRATION =================
st.subheader("📝 Registration")
# ================= SIMPLE BIG BUTTON =================
st.markdown("""
<style>
.simple-register-btn {
    text-align: center;
    margin: 30px 0;
}
.simple-register-btn a {
    text-decoration: none;
}
.simple-register-btn button {
    background-color: #0056b3;
    color: white;
    font-size: 20px;
    font-weight: 600;
    padding: 16px 36px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
}
.simple-register-btn button:hover {
    background-color: #003f7f;
}
</style>

<div class="simple-register-btn">
    <a href="https://forms.gle/ckh9yXvdWREnFgrCA" target="_blank">
        <button>📌 Register Now</button>
    </a>
</div>
""", unsafe_allow_html=True)



st.info("👉 Registration link will be updated soon.")

# ============ ORGANIZING COMMITTEE ============
st.subheader("👥 Organizing Committee")
st.markdown("""
<div class="highlight-box">
<b>Chief Patron:</b> Dr. J. M. Vyas, Hon'ble Vice-Chancellor, NFSU <br>
<b>Chair:</b> Prof. (Dr.) Naveen Kumar Chaudhary, Director, NFSU Goa  <br>
<b>Co-Chair:</b> Dr. Lokesh Chouhan, Dean Academics, NFSU Goa  <br>
<b>Coordinators:</b> Dr. Sanay Naha, Assistant Professor, NFSU Goa<br>
<b>Coordinators:</b> Dr. Suryakant Patil, Assistant Professor, NFSU Goa<br>
<b>Coordinator:</b> Dr. Ranjit Kolkar, Assistant Professor, NFSU Goa<br>

""", unsafe_allow_html=True)


# ============ FOOTER ============
st.markdown("---")
st.markdown('<div class="footer">Contact <br><b><href>sanay.naha@nfsu.ac.in</href></b>  Mobile:<b>6382927133</b>,<br><b><href>suryakant.patil_goa@nfsu.ac.in</href></b>  Mobile:<b>9764035856</b></div>', unsafe_allow_html=True)

st.markdown('<div class="footer">📍 Organized by <b>National Forensic Sciences University, Goa Campus</b></div>', unsafe_allow_html=True)
