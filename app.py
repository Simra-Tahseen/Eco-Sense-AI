import streamlit as st
import os
from PIL import Image

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="EcoSense AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PROJECT PATH
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")


# =========================================================
# CUSTOM DESIGN
# =========================================================

st.markdown(
    """
    <style>

    /* ================================
       MAIN APPLICATION
       ================================ */

    .stApp {
        background-color: #061A16 !important;
    }

    .main {
        background-color: #061A16 !important;
    }

    .block-container {
        max-width: 1400px !important;
        padding-top: 2rem !important;
        padding-bottom: 4rem !important;
    }


    /* ================================
       ALL TEXT
       ================================ */

    .stApp,
    .stApp p,
    .stApp span,
    .stApp label,
    .stApp div {
        color: #F0FDF4;
    }

    p {
        color: #D1FAE5 !important;
    }

    h1 {
        color: #5EEAD4 !important;
    }

    h2 {
        color: #5EEAD4 !important;
    }

    h3 {
        color: #A7F3D0 !important;
    }


    /* ================================
       SIDEBAR
       ================================ */

    section[data-testid="stSidebar"] {
        background-color: #061411 !important;
    }

    section[data-testid="stSidebar"] * {
        color: #F0FDF4 !important;
    }

    section[data-testid="stSidebar"] p {
        color: #D1FAE5 !important;
    }


    /* ================================
       MARKDOWN
       ================================ */

    [data-testid="stMarkdownContainer"] p {
        color: #D1FAE5 !important;
    }

    [data-testid="stMarkdownContainer"] strong {
        color: #FFFFFF !important;
    }


    /* ================================
       CONTAINERS / CARDS
       ================================ */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #102D27 !important;
        border: 1px solid #24584B !important;
        border-radius: 18px !important;
        padding: 10px !important;
    }


    /* ================================
       ALERTS
       ================================ */

    div[data-testid="stAlert"] {
        border-radius: 12px !important;
    }


    /* ================================
       DIVIDERS
       ================================ */

    hr {
        border-color: #24584B !important;
    }


    /* ================================
       IMAGE
       ================================ */

    [data-testid="stImage"] img {
        border-radius: 20px !important;
        border: 1px solid #24584B !important;
    }


    /* ================================
       METRICS
       ================================ */

    [data-testid="stMetric"] {
        background-color: #102D27 !important;
        border: 1px solid #24584B !important;
        border-radius: 15px !important;
        padding: 15px !important;
    }

    [data-testid="stMetricLabel"] {
        color: #A7F3D0 !important;
    }

    [data-testid="stMetricValue"] {
        color: #F0FDF4 !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# IMAGE FUNCTION
# =========================================================

def show_project_image(filename, caption=None, width=550, height=350):

    image_path = os.path.join(
        ASSETS_DIR,
        filename
    )

    # Check whether file exists
    if not os.path.isfile(image_path):
        return False

    try:
        # Open image
        image = Image.open(image_path)

        # Resize image using Pillow to exact width and height
        if width and height:
            image = image.resize((width, height))

        st.image(
            image,
            caption=caption
            # Note: Do NOT pass use_container_width=True here or Streamlit will force it to fill full column width
        )

        return True

    except Exception:
        return False


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🌱 EcoSense AI")

st.sidebar.write(
    "Real-Time Environmental Intelligence"
)

st.sidebar.divider()

st.sidebar.subheader("🌍 SDG 11")

st.sidebar.write(
    "Sustainable Cities and Communities"
)

st.sidebar.divider()

st.sidebar.write("Explore the platform:")

st.sidebar.write("🌫️ Air Quality")
st.sidebar.write("🗺️ Map & Trends")
st.sidebar.write("🤖 AI Assistant")
st.sidebar.write("📊 Reports & Score")
st.sidebar.write("🛡️ Responsible AI")


# =========================================================
# HERO
# =========================================================

st.markdown(
    "### REAL-TIME DATA • AI INSIGHTS • SUSTAINABLE ACTIONS"
)

st.title("🌱 EcoSense AI")

st.write(
    "A real-time environmental intelligence platform "
    "that transforms environmental data into "
    "understandable insights and practical "
    "sustainable actions."
)

st.divider()


# =========================================================
# HERO IMAGE
# =========================================================


# =========================================================
# WHY ECOSENSE AI
# =========================================================

st.header("🌍 Why EcoSense AI?")

col1, col2, col3 = st.columns(3)

with col1:

    with st.container(border=True):

        st.subheader("🌬️ Environmental Awareness")

        st.write(
            "Understand current air-quality conditions "
            "and important environmental indicators."
        )


with col2:

    with st.container(border=True):

        st.subheader("🤖 AI-Powered Insights")

        st.write(
            "Convert complex environmental information "
            "into simple explanations and "
            "sustainability recommendations."
        )


with col3:

    with st.container(border=True):

        st.subheader("🌱 Sustainable Actions")

        st.write(
            "Discover practical choices that support "
            "healthier and more sustainable communities."
        )


# =========================================================
# ENVIRONMENTAL INTELLIGENCE
# =========================================================

st.header("🌿 Environmental Intelligence")

left, right = st.columns([1.1, 1])

with left:

    city_path = os.path.join(
        ASSETS_DIR,
        "city.png"
    )

    if show_project_image(
        "city.png",
        "Sustainable Cities and Environmental Monitoring"
    ):

        pass

    elif not os.path.isfile(city_path):

        st.warning(
            "🖼️ city.png was not found inside the assets folder."
        )

    else:

        st.warning(
            "⚠️ city.png exists, but it is not a valid image file."
        )


with right:

    st.subheader(
        "From environmental data to meaningful action"
    )

    st.write(
        "EcoSense AI combines real-time environmental "
        "data with AI reasoning to help users understand "
        "their surroundings and make sustainable choices."
    )

    st.success(
        "🌫️ MONITOR — Track air quality and "
        "environmental conditions."
    )

    st.info(
        "🤖 UNDERSTAND — Convert environmental data "
        "into simple AI insights."
    )

    st.success(
        "🌱 ACT — Receive practical sustainability "
        "recommendations."
    )


# =========================================================
# PLATFORM FEATURES
# =========================================================

st.header("🚀 Platform Features")

col1, col2, col3 = st.columns(3)

with col1:

    with st.container(border=True):

        st.subheader("🌫️ Air Quality")

        st.write(
            "Live AQI, PM2.5 and pollutant information."
        )


with col2:

    with st.container(border=True):

        st.subheader("🗺️ Map & Trends")

        st.write(
            "Compare environmental conditions "
            "across different cities."
        )


with col3:

    with st.container(border=True):

        st.subheader("🤖 AI Assistant")

        st.write(
            "Ask sustainability questions and receive "
            "context-aware recommendations."
        )


col1, col2, col3 = st.columns(3)

with col1:

    with st.container(border=True):

        st.subheader("📊 Sustainability Score")

        st.write(
            "Understand environmental and sustainability "
            "indicators through a simple score."
        )


with col2:

    with st.container(border=True):

        st.subheader("📄 Sustainability Reports")

        st.write(
            "Generate downloadable environmental "
            "sustainability reports."
        )


with col3:

    with st.container(border=True):

        st.subheader("🛡️ Responsible AI")

        st.write(
            "Transparency, fairness, privacy and "
            "human oversight."
        )


# =========================================================
# SUSTAINABILITY IN ACTION
# =========================================================

st.header("🌱 Sustainability in Action")

left, right = st.columns([1, 1])

with left:

    sustainability_path = os.path.join(
        ASSETS_DIR,
        "sustainability.png"
    )

    if show_project_image(
        "sustainability.png",
        "Sustainable Lifestyle and Environmental Action"
    ):

        pass

    elif not os.path.isfile(sustainability_path):

        st.warning(
            "🖼️ sustainability.png was not found "
            "inside the assets folder."
        )

    else:

        st.warning(
            "⚠️ sustainability.png exists, but it is "
            "not a valid image file."
        )


with right:

    st.subheader(
        "Small actions. Meaningful impact."
    )

    st.write(
        "EcoSense AI encourages practical sustainable "
        "choices that can contribute to cleaner and "
        "more resilient communities."
    )

    st.success(
        "🚲 Choose sustainable transportation when practical."
    )

    st.info(
        "⚡ Reduce unnecessary energy consumption."
    )

    st.warning(
        "♻️ Reduce waste and avoid unnecessary "
        "single-use plastics."
    )


# =========================================================
# SDG ALIGNMENT
# =========================================================

st.header("🌍 Sustainable Development Goals")

col1, col2, col3 = st.columns(3)

with col1:

    with st.container(border=True):

        st.subheader("🌆 SDG 11")

        st.write(
            "Sustainable Cities and Communities."
        )


with col2:

    with st.container(border=True):

        st.subheader("♻️ SDG 12")

        st.write(
            "Responsible Consumption and Production."
        )


with col3:

    with st.container(border=True):

        st.subheader("🌍 SDG 13")

        st.write(
            "Climate Action."
        )


# =========================================================
# RESPONSIBLE AI
# =========================================================

st.header("🛡️ Responsible AI")

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):

        st.subheader("🔍 Transparency")

        st.write(
            "EcoSense AI explains the environmental "
            "context behind its recommendations."
        )


with col2:

    with st.container(border=True):

        st.subheader("🔐 Privacy")

        st.write(
            "The prototype does not require personal "
            "identity information to provide "
            "sustainability insights."
        )


# =========================================================
# PROJECT SNAPSHOT
# =========================================================

st.header("🌱 EcoSense AI at a Glance")

st.write(
    "EcoSense AI connects real-time environmental "
    "information, AI-assisted reasoning and "
    "sustainable actions in one platform."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🌍 Primary SDG",
        "SDG 11"
    )

with col2:
    st.metric(
        "🤖 AI",
        "Enabled"
    )

with col3:
    st.metric(
        "🌫️ Live Data",
        "AQI"
    )

with col4:
    st.metric(
        "♻️ Focus",
        "Sustainability"
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🌱 EcoSense AI | AI for Sustainability | "
    "SDG 11 • SDG 12 • SDG 13"
)

st.caption(
    "Real-Time Environmental Intelligence"
)