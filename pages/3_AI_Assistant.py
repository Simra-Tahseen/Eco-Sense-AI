import streamlit as st
from utils.api import get_air_quality, get_air_status
from utils.ai import analyze_question


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="EcoSense AI - Assistant",
    page_icon="🤖",
    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

/* ================================
   MAIN APPLICATION
================================ */

.stApp {
    background:
        radial-gradient(
            circle at top right,
            rgba(20,184,166,0.12),
            transparent 35%
        ),
        #071A17;

    color: #F0FDF4;
}


/* ================================
   MAIN TEXT
================================ */

html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}


/* ================================
   TITLE
================================ */

.title {
    font-size: 42px;
    font-weight: 800;
    color: #F0FDF4;
}

.subtitle {
    color: #A7F3D0;
    font-size: 17px;
}


/* ================================
   AI HERO CARD
================================ */

.ai-card {
    background: linear-gradient(
        135deg,
        rgba(20,184,166,0.16),
        rgba(34,197,94,0.06)
    );

    border: 1px solid rgba(45,212,191,0.25);

    border-radius: 22px;

    padding: 28px;

    margin-bottom: 20px;

    color: #E2FBEA;
}

.ai-card h3 {
    color: #5EEAD4;
}

.ai-card p {
    color: #D1FAE5;
}


/* ================================
   SECTION TITLES
================================ */

.section-title {
    font-size: 28px;
    font-weight: 700;

    margin-top: 30px;
    margin-bottom: 15px;

    color: #F0FDF4;
}


/* ================================
   CONTEXT BOX
================================ */

.context-box {
    background: rgba(255,255,255,0.04);

    border-radius: 16px;

    padding: 18px;

    border: 1px solid rgba(255,255,255,0.07);

    color: #D1FAE5;
}

.context-box h4 {
    color: #5EEAD4;
}


/* ================================
   FEATURE CARDS
================================ */

.feature-card {
    background: rgba(255,255,255,0.055);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 18px;

    padding: 20px;

    min-height: 150px;

    color: #D1FAE5;
}

.feature-card h3 {
    color: #22C55E;
}

.feature-card h4 {
    color: #F0FDF4;
}

.feature-card p {
    color: #A7F3D0;
}


/* ==================================================
   TRY ASKING BUTTONS
================================================== */

/* Button itself */

div.stButton > button {

    width: 100%;

    min-height: 58px;

    background: #102D27 !important;

    color: #D1FAE5 !important;

    border: 1px solid #24584B !important;

    border-radius: 14px !important;

    font-size: 14px !important;

    font-weight: 600 !important;

    transition: all 0.2s ease !important;

    box-shadow: none !important;
}


/* Hover */

div.stButton > button:hover {

    background: #17463B !important;

    color: #FFFFFF !important;

    border-color: #2DD4BF !important;

    transform: translateY(-2px);

}


/* Active */

div.stButton > button:active {

    background: #1D594B !important;

}


/* Focus */

div.stButton > button:focus {

    outline: none !important;

    box-shadow:
        0 0 0 2px rgba(45,212,191,0.25) !important;
}


/* ================================
   CHAT INPUT
================================ */

/* Chat input container */

div[data-testid="stChatInput"] {

    background: transparent !important;

}


/* Actual textarea */

div[data-testid="stChatInput"] textarea {

    background: #102D27 !important;

    color: #F0FDF4 !important;

    caret-color: #5EEAD4 !important;

    border: 1px solid #2A5D50 !important;

    border-radius: 16px !important;

    font-size: 16px !important;

}


/* Placeholder */

div[data-testid="stChatInput"] textarea::placeholder {

    color: #94A3B8 !important;

    opacity: 1 !important;

}


/* Focused chat input */

div[data-testid="stChatInput"] textarea:focus {

    background: #102D27 !important;

    color: #FFFFFF !important;

    border-color: #2DD4BF !important;

    box-shadow:
        0 0 0 1px #2DD4BF !important;

}


/* Chat input send button */

div[data-testid="stChatInput"] button {

    background: #14532D !important;

    color: #FFFFFF !important;

    border-radius: 10px !important;

}


/* ================================
   CHAT MESSAGES
================================ */

/* User message */

div[data-testid="stChatMessage"] {

    color: #E2FBEA !important;

}


/* Message text */

div[data-testid="stChatMessage"] p {

    color: #E2FBEA !important;

}


/* Markdown inside chat */

div[data-testid="stChatMessage"] div {

    color: #E2FBEA;
}


/* ================================
   SELECTBOX
================================ */

div[data-baseweb="select"] > div {

    background-color: #102D27 !important;

    color: #F0FDF4 !important;

    border-color: #2A5D50 !important;
}


/* Selected text */

div[data-baseweb="select"] span {

    color: #F0FDF4 !important;
}


/* Dropdown menu */

div[data-baseweb="popover"] {

    background-color: #0B211C !important;

}


/* Dropdown options */

div[role="option"] {

    background-color: #0B211C !important;

    color: #D1FAE5 !important;
}


/* Dropdown hover */

div[role="option"]:hover {

    background-color: #17463B !important;

    color: #FFFFFF !important;
}


/* ================================
   METRICS
================================ */

div[data-testid="stMetric"] {

    background: rgba(255,255,255,0.045);

    padding: 18px;

    border-radius: 16px;

    border: 1px solid rgba(255,255,255,0.07);
}

div[data-testid="stMetricLabel"] {

    color: #A7F3D0 !important;
}

div[data-testid="stMetricValue"] {

    color: #F0FDF4 !important;
}


/* ================================
   INFO / WARNING BOXES
================================ */

div[data-testid="stAlert"] {

    background: #102D27 !important;

    color: #D1FAE5 !important;

    border-radius: 14px !important;

}


/* ================================
   SIDEBAR
================================ */

section[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #061411,
        #0B211C
    ) !important;

    border-right:
        1px solid rgba(45,212,191,0.15);
}


/* Sidebar text */

section[data-testid="stSidebar"] * {

    color: #D1FAE5 !important;
}


/* Sidebar headings */

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {

    color: #5EEAD4 !important;
}


/* ================================
   SCROLLBAR
================================ */

::-webkit-scrollbar {

    width: 8px;

}

::-webkit-scrollbar-track {

    background: #071A17;

}

::-webkit-scrollbar-thumb {

    background: #24584B;

    border-radius: 10px;

}

::-webkit-scrollbar-thumb:hover {

    background: #2DD4BF;

}

</style>
""", unsafe_allow_html=True)


# ==================================================
# HEADER
# ==================================================

st.markdown(
    '<div class="title">🤖 EcoSense AI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Ask questions about sustainability, air quality and environmental action.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.markdown("## 🤖 EcoSense AI")

st.sidebar.markdown("---")

st.sidebar.markdown("### 📍 Environmental Context")


locations = {

    "Warangal, Telangana": (17.9689, 79.5941),

    "Hyderabad, Telangana": (17.3850, 78.4867),

    "Delhi, India": (28.6139, 77.2090),

    "Mumbai, Maharashtra": (19.0760, 72.8777),

    "Bengaluru, Karnataka": (12.9716, 77.5946),

    "Chennai, Tamil Nadu": (13.0827, 80.2707),

    "Pune, Maharashtra": (18.5204, 73.8567)
}


selected_city = st.sidebar.selectbox(
    "Monitoring location",
    list(locations.keys())
)

latitude, longitude = locations[selected_city]


# ==================================================
# CURRENT ENVIRONMENTAL DATA
# ==================================================

with st.spinner("Loading environmental context..."):

    data = get_air_quality(
        latitude,
        longitude
    )


aqi = None
pm25 = None
status = "Unavailable"


if "error" not in data:

    current = data.get(
        "current",
        {}
    )

    aqi = current.get("us_aqi")

    pm25 = current.get("pm2_5")

    status = get_air_status(aqi)


# ==================================================
# ENVIRONMENTAL CONTEXT
# ==================================================

st.markdown(
    '<div class="section-title">🌍 Current Environmental Context</div>',
    unsafe_allow_html=True
)

context1, context2, context3 = st.columns(3)


with context1:

    st.metric(
        "Location",
        selected_city
    )


with context2:

    st.metric(
        "Current AQI",
        f"{aqi:.0f}" if aqi is not None else "N/A"
    )


with context3:

    st.metric(
        "Air Quality",
        status
    )


# ==================================================
# HOW IT WORKS
# ==================================================

st.markdown(
    '<div class="section-title">🧠 How EcoSense AI Works</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="ai-card">

<h3>Environmental Context → AI Reasoning → Sustainable Action</h3>

<p>
EcoSense AI combines environmental information with
user questions to generate understandable sustainability
insights.
</p>

<p>
<strong>1. Observe</strong> — Retrieve environmental information.
<br><br>

<strong>2. Understand</strong> — Interpret the user's question.
<br><br>

<strong>3. Reason</strong> — Connect the question with
environmental context.
<br><br>

<strong>4. Recommend</strong> — Provide practical sustainability actions.
<br><br>

<strong>5. Responsible AI</strong> — Communicate limitations
and encourage verification of important information.
</p>

</div>
""", unsafe_allow_html=True)


# ==================================================
# TRY ASKING
# ==================================================

st.markdown(
    '<div class="section-title">💡 Try Asking</div>',
    unsafe_allow_html=True
)

quick_questions = [

    "What is the current air quality?",

    "How can I reduce pollution?",

    "How can students save energy?",

    "How can we reduce plastic waste?",

    "What are sustainable transportation options?",

    "How does this project support the SDGs?"
]


cols = st.columns(3)


for index, question_text in enumerate(
    quick_questions
):

    with cols[index % 3]:

        if st.button(
            question_text,
            key=f"quick_{index}",
            use_container_width=True
        ):

            st.session_state[
                "selected_question"
            ] = question_text


# ==================================================
# CHAT HISTORY
# ==================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ==================================================
# CHAT INPUT
# ==================================================

st.markdown(
    '<div class="section-title">💬 Ask EcoSense AI</div>',
    unsafe_allow_html=True
)

selected_question = st.session_state.get(
    "selected_question",
    ""
)

question = st.chat_input(
    "Ask a sustainability question..."
)


if question is None and selected_question:

    question = selected_question

    st.session_state[
        "selected_question"
    ] = ""


# ==================================================
# PROCESS QUESTION
# ==================================================

if question:

    st.session_state.messages.append({

        "role": "user",

        "content": question

    })

    response = analyze_question(

        question,

        aqi=aqi,

        pm25=pm25,

        city=selected_city

    )

    st.session_state.messages.append({

        "role": "assistant",

        "content": response

    })


# ==================================================
# DISPLAY CHAT
# ==================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# ==================================================
# CLEAR CHAT
# ==================================================

if st.session_state.messages:

    if st.button(
        "🧹 Clear Conversation",
        key="clear_chat"
    ):

        st.session_state.messages = []

        st.rerun()


# ==================================================
# RESPONSIBLE AI
# ==================================================

st.markdown("---")

st.markdown("""
<div class="context-box">

<h4>🛡️ Responsible AI Notice</h4>

<p>
EcoSense AI provides educational and environmental
decision-support information. AI-generated responses
may contain errors or incomplete interpretations.
Important environmental and health-related information
should be verified using authoritative sources.
</p>

<p>
The system does not use personal health information
and does not make medical diagnoses.
</p>

</div>
""", unsafe_allow_html=True)


# ==================================================
# AI WORKFLOW
# ==================================================

st.markdown(
    '<div class="section-title">🔬 AI Workflow</div>',
    unsafe_allow_html=True
)

workflow1, workflow2, workflow3, workflow4 = st.columns(4)


workflow_cards = [

    (
        "01",
        "Environmental Data",
        "Real-time air-quality information."
    ),

    (
        "02",
        "Prompt Understanding",
        "Identify the user's sustainability intent."
    ),

    (
        "03",
        "Contextual Reasoning",
        "Connect environmental data with the question."
    ),

    (
        "04",
        "Sustainable Action",
        "Provide practical sustainability suggestions."
    )
]


for column, card in zip(
    [workflow1, workflow2, workflow3, workflow4],
    workflow_cards
):

    number, title, description = card

    with column:

        st.markdown(
            f"""
            <div class="feature-card">

            <h3>{number}</h3>

            <h4>{title}</h4>

            <p>{description}</p>

            </div>
            """,
            unsafe_allow_html=True
        )