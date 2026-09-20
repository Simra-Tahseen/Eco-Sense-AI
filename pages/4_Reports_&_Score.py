import streamlit as st
import pandas as pd
from datetime import datetime
from utils.api import get_air_quality, get_air_status


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="EcoSense AI - Sustainability Score",
    page_icon="🌱",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       MAIN APPLICATION
       ===================================================== */

    .stApp {
        background-color: #071A17 !important;
        color: #F0FDF4 !important;
    }

    html,
    body {
        background-color: #071A17 !important;
    }

    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {
        background-color: #061411 !important;
    }

    section[data-testid="stSidebar"] p {
        color: #D1FAE5 !important;
    }

    section[data-testid="stSidebar"] label {
        color: #D4A017 !important;
    }

    /* Sidebar headings */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #F0FDF4 !important;
    }


    /* =====================================================
       MAIN HEADINGS
       ===================================================== */

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


    /* =====================================================
       CITY SELECTBOX
       ===================================================== */

    /* Selectbox label */
    div[data-testid="stSelectbox"] label {
        color: #D4A017 !important;
        font-weight: 600 !important;
    }

    /* Main visible selectbox */
    div[data-testid="stSelectbox"]
    div[data-baseweb="select"] {
        background-color: #102D27 !important;
        border-radius: 10px !important;
    }

    /* Selectbox outer container */
    div[data-testid="stSelectbox"]
    div[data-baseweb="select"] > div {
        background-color: #102D27 !important;
        border: 1px solid #2A5D50 !important;
        border-radius: 10px !important;
        box-shadow: none !important;
    }

    /* Value container */
    div[data-testid="stSelectbox"]
    [data-baseweb="value-container"] {
        background-color: #102D27 !important;
    }

    /* SELECTED CITY TEXT */
    div[data-testid="stSelectbox"]
    [data-baseweb="value-container"] * {
        color: #D4A017 !important;
        background-color: transparent !important;
    }

    /* Additional protection for selected city */
    div[data-testid="stSelectbox"]
    [data-baseweb="select"] span {
        color: #D4A017 !important;
    }

    div[data-testid="stSelectbox"]
    [data-baseweb="select"] div {
        color: #D4A017 !important;
    }

    /* Arrow */
    div[data-testid="stSelectbox"]
    [data-baseweb="select"] svg {
        color: #D4A017 !important;
        fill: #D4A017 !important;
    }

    /* Focused selectbox */
    div[data-testid="stSelectbox"]
    [data-baseweb="select"]:focus-within {
        border-color: #D4A017 !important;
        box-shadow: 0 0 0 1px #D4A017 !important;
    }


    /* =====================================================
       DROPDOWN MENU
       ===================================================== */

    div[data-baseweb="popover"] {
        background-color: #0B211C !important;
        border: 1px solid #2A5D50 !important;
    }

    div[data-baseweb="popover"] > div {
        background-color: #0B211C !important;
    }

    ul[role="listbox"] {
        background-color: #0B211C !important;
    }

    /* Every city option */
    li[role="option"] {
        background-color: #0B211C !important;
        color: #D4A017 !important;
    }

    li[role="option"] * {
        color: #D4A017 !important;
        background-color: transparent !important;
    }

    /* Hover */
    li[role="option"]:hover {
        background-color: #17463B !important;
        color: #FFD966 !important;
    }

    li[role="option"]:hover * {
        color: #FFD966 !important;
    }

    /* Selected option */
    li[role="option"][aria-selected="true"] {
        background-color: #14532D !important;
        color: #FFD966 !important;
    }

    li[role="option"][aria-selected="true"] * {
        color: #FFD966 !important;
    }


    /* =====================================================
       METRIC CARDS
       ===================================================== */

    div[data-testid="stMetric"] {
        background-color: #102D27 !important;
        border: 1px solid #24584B !important;
        border-radius: 15px !important;
        padding: 15px !important;
    }

    div[data-testid="stMetricLabel"] {
        color: #A7F3D0 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #F0FDF4 !important;
    }


    /* =====================================================
       DOWNLOAD BUTTON
       ===================================================== */

    .stDownloadButton button {
        background-color: #14532D !important;
        color: #FFFFFF !important;
        border: 1px solid #22C55E !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
    }

    .stDownloadButton button:hover {
        background-color: #166534 !important;
        color: #FFFFFF !important;
        border-color: #5EEAD4 !important;
    }


    /* =====================================================
       DATAFRAME
       ===================================================== */

    div[data-testid="stDataFrame"] {
        border: 1px solid #24584B !important;
        border-radius: 12px !important;
    }


    /* =====================================================
       DIVIDER
       ===================================================== */

    hr {
        border-color: #24584B !important;
    }


    /* =====================================================
       ALERT BOXES
       ===================================================== */

    div[data-testid="stAlert"] {
        border-radius: 12px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# CITY DATABASE
# =========================================================

cities = {
    "Warangal": (17.9689, 79.5941),
    "Hyderabad": (17.3850, 78.4867),
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Bengaluru": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707),
    "Pune": (18.5204, 73.8567)
}


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🌱 EcoSense AI")

st.sidebar.write(
    "Sustainability Analysis"
)

# City selector
city = st.sidebar.selectbox(
    "📍 Select City",
    list(cities.keys())
)

latitude, longitude = cities[city]


st.sidebar.markdown("---")


# Primary SDG
st.sidebar.write("Primary SDG")

st.sidebar.write(
    "🌆 SDG 11 - Sustainable Cities and Communities"
)


# Secondary SDGs
st.sidebar.write("Secondary SDGs")

st.sidebar.write(
    "♻️ SDG 12 - Responsible Consumption"
)

st.sidebar.write(
    "🌍 SDG 13 - Climate Action"
)


# =========================================================
# GET LIVE AIR QUALITY DATA
# =========================================================

data = get_air_quality(
    latitude,
    longitude
)


if "error" in data:

    aqi = 80
    pm25 = 35
    data_status = "Fallback data"

else:

    current = data.get(
        "current",
        {}
    )

    aqi = current.get(
        "us_aqi"
    )

    pm25 = current.get(
        "pm2_5"
    )

    if aqi is None:
        aqi = 80

    if pm25 is None:
        pm25 = 35

    data_status = "Live data"


# =========================================================
# ENVIRONMENT SCORE
# =========================================================

environment_score = max(
    0,
    min(
        100,
        round(
            100 - (float(aqi) / 3),
            1
        )
    )
)


# =========================================================
# OTHER SUSTAINABILITY INDICATORS
# =========================================================

mobility_score = 78

energy_score = 72

waste_score = 75

climate_score = 70


# =========================================================
# OVERALL SCORE
# =========================================================

overall_score = round(
    (
        environment_score
        + mobility_score
        + energy_score
        + waste_score
        + climate_score
    ) / 5,
    1
)


# =========================================================
# PAGE TITLE
# =========================================================

st.title(
    "🌱 Sustainability Score"
)

st.write(
    f"AI-powered sustainability assessment for {city} "
    "using environmental context and sustainability indicators."
)

st.markdown("---")


# =========================================================
# OVERALL SUSTAINABILITY SCORE
# =========================================================

st.header(
    "🌱 Eco Sustainability Score"
)

score1, score2, score3 = st.columns(
    [1, 2, 1]
)

with score2:

    st.metric(
        label="Overall Sustainability Score",
        value=f"{overall_score}/100"
    )

    if overall_score >= 80:

        st.success(
            "Strong sustainability performance"
        )

    elif overall_score >= 60:

        st.info(
            "Moderate sustainability performance"
        )

    else:

        st.warning(
            "Improvement opportunities identified"
        )


st.write(
    "The score combines environmental, mobility, energy, "
    "waste and climate indicators."
)


# =========================================================
# LIVE ENVIRONMENTAL CONTEXT
# =========================================================

st.header(
    "🌍 Live Environmental Context"
)

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "📍 Location",
        city
    )


with col2:

    st.metric(
        "🌫️ Air Quality Index",
        f"{aqi:.0f}"
    )


with col3:

    st.metric(
        "💨 PM2.5",
        f"{pm25:.1f} µg/m³"
    )


with col4:

    st.metric(
        "📊 AQI Status",
        get_air_status(aqi)
    )


st.caption(
    f"Environmental data status: {data_status}"
)


# =========================================================
# SUSTAINABILITY BREAKDOWN
# =========================================================

st.header(
    "📊 Sustainability Breakdown"
)

col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    st.metric(
        "🌫️ Environment",
        f"{environment_score}/100"
    )


with col2:

    st.metric(
        "🚲 Mobility",
        f"{mobility_score}/100"
    )


with col3:

    st.metric(
        "⚡ Energy",
        f"{energy_score}/100"
    )


with col4:

    st.metric(
        "♻️ Waste",
        f"{waste_score}/100"
    )


with col5:

    st.metric(
        "🌍 Climate",
        f"{climate_score}/100"
    )


# =========================================================
# SCORE DETAILS
# =========================================================

st.subheader(
    "Score Details"
)


score_table = pd.DataFrame(
    {
        "Category": [
            "Environment",
            "Mobility",
            "Energy",
            "Waste",
            "Climate"
        ],

        "Score": [
            environment_score,
            mobility_score,
            energy_score,
            waste_score,
            climate_score
        ],

        "Description": [
            "Based on current air quality",
            "Sustainable transport indicator",
            "Energy efficiency indicator",
            "Waste reduction indicator",
            "Climate action indicator"
        ]
    }
)


st.dataframe(
    score_table,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# PERFORMANCE CHART
# =========================================================

st.header(
    "📈 Sustainability Performance"
)


chart_data = pd.DataFrame(
    {
        "Environment": [
            environment_score
        ],

        "Mobility": [
            mobility_score
        ],

        "Energy": [
            energy_score
        ],

        "Waste": [
            waste_score
        ],

        "Climate": [
            climate_score
        ]
    }
)


st.bar_chart(
    chart_data.T,
    height=350
)


# =========================================================
# AI INSIGHT
# =========================================================

st.header(
    "🤖 EcoSense AI Insight"
)


if overall_score >= 80:

    st.success(
        "The current sustainability profile shows strong "
        "performance across the evaluated indicators."
    )

elif overall_score >= 60:

    st.info(
        "The current sustainability profile shows moderate "
        "performance with several opportunities for improvement."
    )

else:

    st.warning(
        "The current sustainability profile identifies areas "
        "where stronger sustainable practices could be adopted."
    )


# =========================================================
# AI-GENERATED ACTION PLAN
# =========================================================

st.header(
    "🌱 AI-Generated Sustainability Action Plan"
)


if aqi > 100:

    st.write(
        "🌫️ **Air Quality:** Consider reducing unnecessary "
        "outdoor exposure during periods of elevated pollution."
    )

else:

    st.write(
        "🌫️ **Air Quality:** Continue practices that help "
        "maintain cleaner local air."
    )


st.write(
    "🚲 **Mobility:** Prefer walking, cycling, public transport "
    "or shared mobility when practical."
)


st.write(
    "⚡ **Energy:** Switch off unused devices and reduce "
    "unnecessary electricity consumption."
)


st.write(
    "♻️ **Waste:** Reduce single-use plastics and separate "
    "recyclable materials."
)


st.write(
    "🌍 **Climate:** Adopt practical low-carbon lifestyle "
    "choices and reduce unnecessary emissions."
)


# =========================================================
# SUSTAINABILITY REPORT
# =========================================================

st.header(
    "📄 Sustainability Report"
)


report = f"""
ECOSENSE AI
SUSTAINABILITY REPORT
=================================

Generated:
{datetime.now().strftime("%d-%m-%Y %H:%M")}

LOCATION
--------
{city}

LIVE ENVIRONMENTAL DATA
-----------------------
AQI: {aqi:.0f}
PM2.5: {pm25:.1f} µg/m³
AQI Status: {get_air_status(aqi)}

SUSTAINABILITY SCORES
---------------------
Overall Score: {overall_score}/100

Environment: {environment_score}/100
Mobility: {mobility_score}/100
Energy: {energy_score}/100
Waste: {waste_score}/100
Climate: {climate_score}/100

AI ACTION PLAN
--------------
1. Monitor local air-quality conditions.
2. Prefer sustainable transportation.
3. Reduce unnecessary energy consumption.
4. Reduce single-use plastics and recycle.
5. Adopt lower-carbon lifestyle choices.

PROJECT
-------
EcoSense AI
AI for Sustainability

Primary SDG:
SDG 11 - Sustainable Cities and Communities

Secondary SDGs:
SDG 12 - Responsible Consumption
SDG 13 - Climate Action

RESPONSIBLE AI
--------------
The sustainability score is a prototype indicator.
It should not be considered an official environmental
assessment.

DATA SOURCE
-----------
Open-Meteo Air Quality API
"""


st.download_button(
    "⬇️ Download Sustainability Report",
    data=report,
    file_name=f"EcoSense_{city}_Report.txt",
    mime="text/plain"
)


# =========================================================
# RESPONSIBLE AI
# =========================================================

st.header(
    "🛡️ Responsible AI"
)


responsible_col1, responsible_col2 = st.columns(2)


with responsible_col1:

    st.subheader(
        "🔍 Transparency"
    )

    st.write(
        "EcoSense AI explains the environmental context "
        "used for its recommendations."
    )

    st.subheader(
        "⚖️ Fairness"
    )

    st.write(
        "Recommendations are intended to be adaptable to "
        "different user circumstances."
    )


with responsible_col2:

    st.subheader(
        "🔐 Privacy"
    )

    st.write(
        "The prototype does not require personal identity "
        "information to provide sustainability insights."
    )

    st.subheader(
        "👤 Human Oversight"
    )

    st.write(
        "AI recommendations are advisory. Important "
        "environmental decisions should use verified sources."
    )


# =========================================================
# PROTOTYPE LIMITATIONS
# =========================================================

st.header(
    "⚠️ Prototype Limitations"
)


st.write(
    "• Mobility, energy, waste and climate values are "
    "prototype indicators rather than direct measurements."
)


st.write(
    "• Environmental conditions can change over time."
)


st.write(
    "• The sustainability score should not replace official "
    "environmental assessments."
)


st.write(
    "• Future versions can integrate additional real-time "
    "datasets and user-specific inputs."
)


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")


st.caption(
    "EcoSense AI | AI for Sustainability | SDG 11"
)


st.caption(
    "Environmental data source: Open-Meteo Air Quality API"
)