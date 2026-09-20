import requests


def get_air_quality(latitude, longitude):
    """
    Fetch current air-quality data from Open-Meteo.
    """

    url = "https://air-quality-api.open-meteo.com/v1/air-quality"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "pm10",
            "pm2_5",
            "carbon_monoxide",
            "nitrogen_dioxide",
            "sulphur_dioxide",
            "ozone",
            "us_aqi"
        ],
        "timezone": "auto"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as e:

        return {
            "error": str(e)
        }


def get_hourly_air_quality(latitude, longitude):
    """
    Fetch recent hourly air-quality data.
    """

    url = "https://air-quality-api.open-meteo.com/v1/air-quality"

    params = {
        "latitude": latitude,
        "longitude": longitude,

        "hourly": [
            "pm2_5",
            "pm10",
            "us_aqi"
        ],

        "past_days": 1,

        "forecast_days": 1,

        "timezone": "auto"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as e:

        return {
            "error": str(e)
        }


def get_air_status(aqi):

    if aqi is None:
        return "Unknown"

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Moderate"

    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"

    elif aqi <= 200:
        return "Unhealthy"

    elif aqi <= 300:
        return "Very Unhealthy"

    else:
        return "Hazardous"


def get_status_emoji(status):

    mapping = {
        "Good": "🟢",
        "Moderate": "🟡",
        "Unhealthy for Sensitive Groups": "🟠",
        "Unhealthy": "🔴",
        "Very Unhealthy": "🟣",
        "Hazardous": "⚫"
    }

    return mapping.get(status, "⚪")