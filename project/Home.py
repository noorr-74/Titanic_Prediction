import streamlit as st

st.set_page_config(
    page_title="Titanic Survival System",
    layout="wide"
)

# ================= BACKGROUND =================

page_bg = """
<style>

[data-testid="stAppViewContainer"]{
background:
linear-gradient(
135deg,
#0f172a,
#1e293b,
#334155
);
color:white;
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

[data-testid="stSidebar"]{
background-color:#111827;
}

.center-text{
text-align:center;
}

img{
border-radius:20px;
box-shadow:0px 0px 25px rgba(255,255,255,0.2);
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ================= TITLE =================

st.markdown(
"""
<div class="center-text">

<h1 style="font-size:60px;">
🚢 Titanic Survival System
</h1>

<h3>
Welcome to the Titanic Prediction Project
</h3>

<p style="font-size:22px;">
Use the sidebar to navigate between pages
</p>

</div>
""",
unsafe_allow_html=True
)

# ================= IMAGE =================

col1, col2, col3 = st.columns([1,2,1])

with col2:

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/f/fd/RMS_Titanic_3.jpg",
        use_container_width=True
    )

# ================= INFO =================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
"""
<div class="center-text">

<h3>📌 Available Pages</h3>

<p style="font-size:20px;">
🎯 Prediction Page
</p>

<p style="font-size:20px;">
📊 Visualization Dashboard
</p>

</div>
""",
unsafe_allow_html=True
)