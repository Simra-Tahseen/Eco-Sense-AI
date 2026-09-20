import streamlit as st

st.set_page_config(
    page_title="EcoSense AI - Responsible AI",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #071A17;
        color: #F0FDF4;
    }

    html, body {
        background-color: #071A17;
    }

    section[data-testid="stSidebar"] {
        background-color: #061411 !important;
    }

    section[data-testid="stSidebar"] * {
        color: #D1FAE5 !important;
    }

    h1 {
        color: #F0FDF4 !important;
    }

    h2 {
        color: #5EEAD4 !important;
    }

    h3 {
        color: #A7F3D0 !important;
    }

    p {
        color: #D1FAE5;
    }

    .card {
        background-color: #102D27;
        border: 1px solid #24584B;
        border-radius: 15px;
        padding: 22px;
        margin-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🌱 EcoSense AI")
st.sidebar.write("Responsible AI")

st.sidebar.markdown("---")

st.sidebar.write(
    "🌆 SDG 11 - Sustainable Cities and Communities"
)

st.sidebar.write(
    "♻️ SDG 12 - Responsible Consumption"
)

st.sidebar.write(
    "🌍 SDG 13 - Climate Action"
)

# =========================================================
# TITLE
# =========================================================

st.title("🛡️ Responsible AI")

st.write(
    "EcoSense AI is designed with responsible and transparent "
    "AI principles to support sustainable decision-making."
)

st.markdown("---")

# =========================================================
# INTRODUCTION
# =========================================================

st.header("🤖 Why Responsible AI?")

st.write(
    "Environmental AI systems can influence how users understand "
    "pollution, sustainability and environmental conditions. "
    "Therefore, EcoSense AI focuses on transparency, fairness, "
    "privacy and human oversight."
)

# =========================================================
# FOUR PRINCIPLES
# =========================================================

st.header("🔐 Responsible AI Principles")

col1, col2 = st.columns(2)

with col1:

    st.subheader("🔍 Transparency")

    st.write(
        "EcoSense AI communicates the environmental data used "
        "for its recommendations and clearly identifies "
        "prototype indicators."
    )

    st.subheader("⚖️ Fairness")

    st.write(
        "Recommendations are designed as general guidance and "
        "should be adaptable to different users, locations "
        "and circumstances."
    )

with col2:

    st.subheader("🔐 Privacy")

    st.write(
        "The prototype does not require personal identity "
        "information to provide environmental insights."
    )

    st.subheader("👤 Human Oversight")

    st.write(
        "AI recommendations are advisory. Users should verify "
        "important environmental information using trusted "
        "official sources."
    )

# =========================================================
# AI WORKFLOW
# =========================================================

st.header("🔄 Responsible AI Workflow")

step1, step2, step3, step4 = st.columns(4)

with step1:
    st.subheader("1️⃣ Data")
    st.write(
        "Environmental data is collected from an external "
        "air-quality API."
    )

with step2:
    st.subheader("2️⃣ Context")
    st.write(
        "Current AQI and PM2.5 values are interpreted as "
        "environmental context."
    )

with step3:
    st.subheader("3️⃣ AI Reasoning")
    st.write(
        "The system generates sustainability guidance based "
        "on the available context."
    )

with step4:
    st.subheader("4️⃣ Human Review")
    st.write(
        "Users should evaluate recommendations before making "
        "important decisions."
    )

# =========================================================
# DATA PRIVACY
# =========================================================

st.header("🔒 Data Privacy")

privacy_data = {
    "Data Type": [
        "Personal identity",
        "Location selection",
        "Air quality data",
        "User questions"
    ],
    "Required": [
        "No",
        "Yes",
        "Yes",
        "Optional"
    ],
    "Purpose": [
        "Not required",
        "Select environmental context",
        "Generate sustainability insights",
        "Generate AI guidance"
    ]
}

st.dataframe(
    privacy_data,
    use_container_width=True,
    hide_index=True
)

# =========================================================
# LIMITATIONS
# =========================================================

st.header("⚠️ AI Limitations")

st.write(
    "• Sustainability indicators are prototype measurements."
)

st.write(
    "• The system does not replace official environmental "
    "monitoring or government advisories."
)

st.write(
    "• Environmental conditions can change rapidly."
)

st.write(
    "• AI-generated recommendations may not cover every "
    "individual circumstance."
)

st.write(
    "• Additional verified datasets would improve future versions."
)

# =========================================================
# FUTURE IMPROVEMENTS
# =========================================================

st.header("🚀 Future Responsible AI Improvements")

future1, future2 = st.columns(2)

with future1:

    st.write(
        "🌍 Integrate more verified environmental datasets"
    )

    st.write(
        "📊 Add explainable AI-based sustainability scoring"
    )

    st.write(
        "🔎 Add source citations for AI-generated responses"
    )

with future2:

    st.write(
        "👥 Add user feedback for recommendation improvement"
    )

    st.write(
        "🛡️ Add stronger privacy controls"
    )

    st.write(
        "📈 Continuously evaluate recommendation quality"
    )

# =========================================================
# RESPONSIBLE AI STATEMENT
# =========================================================

st.header("🌱 EcoSense AI Responsibility Statement")

st.success(
    "EcoSense AI is designed to assist users with environmental "
    "awareness and sustainable actions. AI outputs are advisory "
    "and should be evaluated alongside reliable environmental "
    "information and human judgment."
)

st.markdown("---")

st.caption(
    "EcoSense AI | Responsible AI | AI for Sustainability"
)