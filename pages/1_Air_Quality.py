import streamlit as st
import pandas as pd
from datetime import datetime

from utils.api import (
    get_air_quality,
    get_air_status,
    get_status_emoji
)


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="EcoSense AI - Air Quality",
    page_icon="🌫️",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at top right,
            rgba(20,184,166,0.12),
            transparent 35%
        ),
        #071A17;
    color: white;
}

.title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    color: #A7F3D0;
    font-size: 17px;
}

.card {
    background: rgba(255,255,255,0.055);
    padding: 22px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.09);
}

.aqi-card {
    padding: 30px;
    border-radius: 22px;
    background: linear-gradient(
        135deg,
        rgba(20,184,166,0.18),
        rgba(34,197,94,0.08)
    );
    border: 1px solid rgba(45,212,191,0.25);
    text-align: center;
}

.aqi-number {
    font-size: 65px;
    font-weight: 800;
    color: #22C55E;
}

.aqi-status {
    font-size: 22px;
    font-weight: 600;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 35px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="title">🌫️ Real-Time Air Quality</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Monitor environmental conditions using live air-quality data.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# --------------------------------------------------
# LOCATION SELECTION
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📍 Select Monitoring Location</div>',
    unsafe_allow_html=True
)

locations = {

    "Warangal, Telangana": (17.9689, 79.5941),

    "Hyderabad, Telangana": (17.3850, 78.4867),

    "Delhi, India": (28.6139, 77.2090),

    "Mumbai, Maharashtra": (19.0760, 72.8777),

    "Bengaluru, Karnataka": (12.9716, 77.5946),

    "Chennai, Tamil Nadu": (13.0827, 80.2707),

    "Pune, Maharashtra": (18.5204, 73.8567)
}


selected_location = st.selectbox(
    "Choose a city",
    list(locations.keys())
)


latitude, longitude = locations[selected_location]


# --------------------------------------------------
# FETCH DATA
# --------------------------------------------------

with st.spinner("Fetching real-time environmental data..."):

    data = get_air_quality(
        latitude,
        longitude
    )


# --------------------------------------------------
# ERROR HANDLING
# --------------------------------------------------

if "error" in data:

    st.error(
        "Unable to retrieve live air-quality data."
    )

    st.code(data["error"])

    st.stop()


current = data.get("current", {})


# --------------------------------------------------
# EXTRACT VALUES
# --------------------------------------------------

pm25 = current.get("pm2_5")
pm10 = current.get("pm10")
co = current.get("carbon_monoxide")
no2 = current.get("nitrogen_dioxide")
so2 = current.get("sulphur_dioxide")
ozone = current.get("ozone")
aqi = current.get("us_aqi")


status = get_air_status(aqi)
emoji = get_status_emoji(status)


# --------------------------------------------------
# LOCATION INFO
# --------------------------------------------------

st.markdown(
    f"""
    <div class="card">

    <h3>📍 {selected_location}</h3>

    <p>
    Latitude: {latitude} |
    Longitude: {longitude}
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# AQI MAIN CARD
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🌍 Current Environmental Status</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        f"""
        <div class="aqi-card">

        <div class="aqi-number">
        {aqi if aqi is not None else "N/A"}
        </div>

        <div class="aqi-status">
        {emoji} {status}
        </div>

        <p>US Air Quality Index</p>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.metric(
        "PM2.5",
        f"{pm25:.1f} μg/m³" if pm25 is not None else "N/A"
    )

    st.metric(
        "PM10",
        f"{pm10:.1f} μg/m³" if pm10 is not None else "N/A"
    )


with col3:

    st.metric(
        "Nitrogen Dioxide",
        f"{no2:.1f} μg/m³" if no2 is not None else "N/A"
    )

    st.metric(
        "Ozone",
        f"{ozone:.1f} μg/m³" if ozone is not None else "N/A"
    )


# --------------------------------------------------
# POLLUTANT DASHBOARD
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🧪 Pollutant Breakdown</div>',
    unsafe_allow_html=True
)

pollutants = pd.DataFrame({

    "Pollutant": [
        "PM2.5",
        "PM10",
        "Carbon Monoxide",
        "Nitrogen Dioxide",
        "Sulphur Dioxide",
        "Ozone"
    ],

    "Value": [
        pm25,
        pm10,
        co,
        no2,
        so2,
        ozone
    ],

    "Unit": [
        "μg/m³",
        "μg/m³",
        "μg/m³",
        "μg/m³",
        "μg/m³",
        "μg/m³"
    ]
})


st.dataframe(
    pollutants,
    use_container_width=True,
    hide_index=True
)


# --------------------------------------------------
# VISUALIZATION
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📊 Pollutant Visualization</div>',
    unsafe_allow_html=True
)

chart_data = pollutants.set_index("Pollutant")["Value"]

st.bar_chart(chart_data)


# --------------------------------------------------
# AI-STYLE INSIGHT
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🤖 EcoSense Environmental Insight</div>',
    unsafe_allow_html=True
)


if aqi is not None:

    if aqi <= 50:

        message = """
        Current air-quality conditions are within the
        Good range. This indicates relatively low
        pollution levels at the selected location.

        Sustainable action:
        Continue using public transport, walking,
        cycling and energy-efficient practices.
        """

    elif aqi <= 100:

        message = """
        Air quality is currently in the Moderate range.
        Sensitive individuals may prefer limiting prolonged
        exposure during pollution peaks.

        Sustainable action:
        Reduce unnecessary vehicle use and avoid
        idling engines.
        """

    elif aqi <= 150:

        message = """
        Air quality may affect sensitive groups.

        Sustainable action:
        Prefer public transportation, reduce unnecessary
        outdoor exposure during pollution peaks and
        support low-emission mobility.
        """

    else:

        message = """
        Current pollution levels are elevated.

        Sustainable action:
        Minimize unnecessary outdoor exposure and
        reduce activities that contribute to emissions.
        """

    st.info(message)


# --------------------------------------------------
# DATA SOURCE
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Data source: Open-Meteo Air Quality API. "
    "Values are provided for environmental awareness "
    "and should not be treated as medical advice."
)

st.caption(
    f"Last retrieved: {datetime.now().strftime('%d %B %Y, %I:%M:%S %p')}"
)