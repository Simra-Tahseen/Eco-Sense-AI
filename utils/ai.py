import re


def analyze_question(question, aqi=None, pm25=None, city="your city"):
    """
    EcoSense AI rule-based sustainability reasoning layer.

    This provides a working fallback when an external
    generative AI API is not configured.
    """

    question = question.lower().strip()

    context = ""

    if aqi is not None:
        context += f"\nCurrent AQI for {city}: {aqi}"

    if pm25 is not None:
        context += f"\nCurrent PM2.5: {pm25} μg/m³"

    # -----------------------------------------------
    # AIR QUALITY
    # -----------------------------------------------

    if any(word in question for word in [
        "aqi",
        "air quality",
        "pollution",
        "air pollution"
    ]):

        if aqi is not None:

            if aqi <= 50:
                status = "good"

            elif aqi <= 100:
                status = "moderate"

            elif aqi <= 150:
                status = "unhealthy for sensitive groups"

            elif aqi <= 200:
                status = "unhealthy"

            else:
                status = "elevated"

            return f"""
### 🌫️ Air Quality Analysis

For **{city}**, the current AQI available to EcoSense AI is approximately
**{aqi:.0f}**, which falls in the **{status}** range.

{context}

### 🌱 Suggested Actions

- Prefer public transportation when practical.
- Avoid unnecessary vehicle idling.
- Consider walking or cycling for short trips when conditions are suitable.
- Support cleaner energy and low-emission community practices.
- Check official local air-quality information before making health-related decisions.

### 💡 EcoSense Insight

Air quality can change throughout the day because of weather,
traffic, industrial activity and other factors. A single AQI reading
should therefore be treated as a snapshot rather than a complete
description of city-wide conditions.
"""

        return """
### 🌫️ Air Quality

EcoSense AI needs current environmental data to provide
location-specific air-quality analysis.

Open the **Air Quality** page and select a monitoring location first.
"""


    # -----------------------------------------------
    # SUSTAINABLE TRANSPORT
    # -----------------------------------------------

    if any(word in question for word in [
        "transport",
        "travel",
        "vehicle",
        "car",
        "traffic",
        "transportation"
    ]):

        return """
### 🚲 Sustainable Transportation

Transportation can contribute significantly to urban emissions.

EcoSense AI recommends considering:

- 🚶 Walking for short practical trips
- 🚲 Cycling where safe infrastructure exists
- 🚌 Public transportation
- 🚗 Carpooling
- ⚡ Lower-emission transportation options

### 🌱 Practical Challenge

For your next suitable short-distance trip, consider replacing
a private vehicle journey with walking, cycling or public transport.
"""


    # -----------------------------------------------
    # ENERGY
    # -----------------------------------------------

    if any(word in question for word in [
        "energy",
        "electricity",
        "power",
        "solar"
    ]):

        return """
### ⚡ Energy Sustainability

Some practical ways to reduce unnecessary energy consumption include:

- Turn off unused lights and equipment.
- Use energy-efficient appliances.
- Reduce unnecessary air-conditioning usage.
- Prefer natural lighting when practical.
- Explore renewable-energy options where feasible.
- Monitor electricity consumption instead of relying only on estimates.

### 💡 EcoSense Insight

Energy efficiency can simultaneously support environmental
objectives and reduce avoidable resource consumption.
"""


    # -----------------------------------------------
    # WASTE
    # -----------------------------------------------

    if any(word in question for word in [
        "waste",
        "garbage",
        "plastic",
        "recycle",
        "recycling"
    ]):

        return """
### ♻️ Waste Management

A sustainable waste strategy can follow this sequence:

**Reduce → Reuse → Repair → Recycle → Dispose responsibly**

Practical actions:

- Avoid unnecessary single-use products.
- Carry reusable bottles and bags.
- Separate waste according to local rules.
- Reuse materials whenever possible.
- Recycle through appropriate collection systems.

### 🌱 Community Impact

Better waste practices can reduce unnecessary resource
consumption and support cleaner communities.
"""


    # -----------------------------------------------
    # CLIMATE
    # -----------------------------------------------

    if any(word in question for word in [
        "climate",
        "carbon",
        "emission",
        "emissions",
        "greenhouse"
    ]):

        return """
### 🌍 Climate Action

Climate-oriented sustainability actions can include:

- Improving energy efficiency
- Choosing lower-emission transportation
- Reducing unnecessary consumption
- Supporting renewable energy
- Reducing food and material waste
- Protecting and increasing urban greenery

### 🎯 SDG Connection

These actions can contribute to:

**SDG 11 — Sustainable Cities and Communities**

and

**SDG 13 — Climate Action**
"""


    # -----------------------------------------------
    # SDGs
    # -----------------------------------------------

    if "sdg" in question:

        return """
### 🎯 EcoSense AI — SDG Alignment

The primary SDG for this project is:

**SDG 11 — Sustainable Cities and Communities**

Secondary connections include:

**SDG 12 — Responsible Consumption and Production**

**SDG 13 — Climate Action**

EcoSense AI uses environmental information and AI-assisted
insights to support awareness and more informed sustainability decisions.
"""


    # -----------------------------------------------
    # DEFAULT RESPONSE
    # -----------------------------------------------

    return f"""
### 🤖 EcoSense AI

I can help you explore sustainability topics such as:

🌫️ Air quality and pollution

🚲 Sustainable transportation

⚡ Energy efficiency

♻️ Waste management

🌍 Climate action

🎯 SDGs

📊 Environmental data interpretation

Try asking something like:

> "How can I reduce pollution?"

> "What does AQI mean?"

> "How can students save energy?"

> "How can my city become more sustainable?"

{context}
"""