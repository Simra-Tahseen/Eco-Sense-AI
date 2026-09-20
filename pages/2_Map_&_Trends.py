import streamlit as st
import pandas as pd
import pydeck as pdk

from utils.api import (
    get_air_quality,
    get_hourly_air_quality,
    get_air_status,
    get_status_emoji
)


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="EcoSense AI - Map & Trends",
    page_icon="🗺️",
    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================

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

.page-title {
    font-size: 42px;
    font-weight: 800;
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

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 15px;
}

.insight {
    padding: 24px;
    border-radius: 18px;
    background: linear-gradient(
        135deg,
        rgba(20,184,166,0.15),
        rgba(34,197,94,0.08)
    );

    border: 1px solid rgba(45,212,191,0.25);
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# HEADER
# ==================================================

st.markdown(
    '<div class="page-title">🗺️ Environmental Map & Trends</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Compare real-time environmental conditions across cities.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# ==================================================
# CITY DATABASE
# ==================================================

locations = {

    "Warangal, Telangana":
        (17.9689, 79.5941),

    "Hyderabad, Telangana":
        (17.3850, 78.4867),

    "Delhi, India":
        (28.6139, 77.2090),

    "Mumbai, Maharashtra":
        (19.0760, 72.8777),

    "Bengaluru, Karnataka":
        (12.9716, 77.5946),

    "Chennai, Tamil Nadu":
        (13.0827, 80.2707),

    "Pune, Maharashtra":
        (18.5204, 73.8567)
}


# ==================================================
# FETCH CURRENT DATA
# ==================================================

results = []

progress = st.progress(0)

for index, (city, coords) in enumerate(locations.items()):

    latitude, longitude = coords

    data = get_air_quality(
        latitude,
        longitude
    )

    if "error" not in data:

        current = data.get("current", {})

        aqi = current.get("us_aqi")

        pm25 = current.get("pm2_5")

        status = get_air_status(aqi)

        results.append({
            "City": city,
            "Latitude": latitude,
            "Longitude": longitude,
            "AQI": aqi,
            "PM2.5": pm25,
            "Status": status
        })

    progress.progress(
        (index + 1) / len(locations)
    )

progress.empty()


df = pd.DataFrame(results)


# ==================================================
# CITY COMPARISON
# ==================================================

st.markdown(
    '<div class="section-title">📊 Live City Comparison</div>',
    unsafe_allow_html=True
)

if not df.empty:

    display_df = df[
        ["City", "AQI", "PM2.5", "Status"]
    ].copy()

    display_df["AQI"] = display_df["AQI"].round(0)

    display_df["PM2.5"] = display_df["PM2.5"].round(1)

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.error(
        "Unable to retrieve city data."
    )


# ==================================================
# MAP
# ==================================================

st.markdown(
    '<div class="section-title">🌍 Live Environmental Map</div>',
    unsafe_allow_html=True
)

if not df.empty:

    # Remove missing AQI values
    map_df = df.dropna(
        subset=["AQI"]
    ).copy()

    # Size markers according to AQI
    map_df["radius"] = (
        map_df["AQI"].clip(lower=20, upper=300) * 150
    )

    layer = pdk.Layer(
        "ScatterplotLayer",

        data=map_df,

        get_position=[
            "Longitude",
            "Latitude"
        ],

        get_radius="radius",

        get_fill_color=[
            34,
            197,
            94,
            180
        ],

        get_line_color=[
            255,
            255,
            255,
            200
        ],

        pickable=True,

        auto_highlight=True
    )

    view_state = pdk.ViewState(
        latitude=20.5,
        longitude=78.9,
        zoom=4.3,
        pitch=25
    )

    deck = pdk.Deck(

        layers=[layer],

        initial_view_state=view_state,

        tooltip={
            "html":
            "<b>{City}</b><br/>"
            "AQI: {AQI}<br/>"
            "PM2.5: {PM2.5}<br/>"
            "Status: {Status}",

            "style": {
                "backgroundColor": "#0B211C",
                "color": "white"
            }
        }
    )

    st.pydeck_chart(
        deck,
        use_container_width=True
    )


# ==================================================
# AQI BAR CHART
# ==================================================

st.markdown(
    '<div class="section-title">📈 AQI Comparison</div>',
    unsafe_allow_html=True
)

if not df.empty:

    chart_df = df[
        ["City", "AQI"]
    ].dropna()

    chart_df = chart_df.set_index(
        "City"
    )

    st.bar_chart(
        chart_df
    )


# ==================================================
# TREND ANALYSIS
# ==================================================

st.markdown(
    '<div class="section-title">📈 24-Hour PM2.5 Trend</div>',
    unsafe_allow_html=True
)

selected_city = st.selectbox(
    "Select a city for trend analysis",
    list(locations.keys())
)


latitude, longitude = locations[
    selected_city
]


with st.spinner(
    "Loading environmental trend data..."
):

    hourly_data = get_hourly_air_quality(
        latitude,
        longitude
    )


if "error" not in hourly_data:

    hourly = hourly_data.get(
        "hourly",
        {}
    )

    times = hourly.get(
        "time",
        []
    )

    pm_values = hourly.get(
        "pm2_5",
        []
    )

    trend_df = pd.DataFrame({

        "Time": times,

        "PM2.5": pm_values

    })

    trend_df["Time"] = pd.to_datetime(
        trend_df["Time"]
    )

    trend_df = trend_df.dropna()

    # Last 24 records
    trend_df = trend_df.tail(24)

    trend_df = trend_df.set_index(
        "Time"
    )

    st.line_chart(
        trend_df["PM2.5"]
    )

else:

    st.warning(
        "Trend data could not be retrieved."
    )


# ==================================================
# AI-STYLE ENVIRONMENTAL INSIGHT
# ==================================================

st.markdown(
    '<div class="section-title">🤖 EcoSense Environmental Insight</div>',
    unsafe_allow_html=True
)

if not df.empty:

    valid_df = df.dropna(
        subset=["AQI"]
    )

    if not valid_df.empty:

        highest_city = valid_df.loc[
            valid_df["AQI"].idxmax()
        ]

        lowest_city = valid_df.loc[
            valid_df["AQI"].idxmin()
        ]

        st.markdown(
            f"""
            <div class="insight">

            <h3>🌱 Current Environmental Pattern</h3>

            <p>
            Among the monitored locations,
            <strong>{highest_city["City"]}</strong>
            currently has the highest observed AQI
            in this dashboard at approximately
            <strong>{highest_city["AQI"]:.0f}</strong>.
            </p>

            <p>
            <strong>{lowest_city["City"]}</strong>
            currently has the lowest observed AQI
            at approximately
            <strong>{lowest_city["AQI"]:.0f}</strong>.
            </p>

            <p>
            These values are snapshots and can change
            over time. They should be interpreted as
            environmental awareness information rather
            than a complete assessment of city-wide
            air quality.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ==================================================
# SUSTAINABILITY ACTIONS
# ==================================================

st.markdown(
    '<div class="section-title">🌱 Sustainable Actions</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="card">

    <h3>🚲 Sustainable Mobility</h3>

    <p>
    Prefer walking, cycling and public transportation
    when practical to reduce unnecessary emissions.
    </p>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="card">

    <h3>⚡ Energy Efficiency</h3>

    <p>
    Reduce unnecessary electricity consumption and
    prefer energy-efficient appliances.
    </p>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="card">

    <h3>🌳 Green Communities</h3>

    <p>
    Support urban greenery, responsible waste
    management and cleaner community practices.
    </p>

    </div>
    """, unsafe_allow_html=True)


# ==================================================
# DATA SOURCE
# ==================================================

st.markdown("---")

st.caption(
    "Environmental data source: Open-Meteo Air Quality API."
)

st.caption(
    "The dashboard provides informational environmental "
    "insights and does not replace official monitoring systems."
)