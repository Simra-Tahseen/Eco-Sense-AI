import streamlit as st
import os
import base64


# =========================================================
# GLOBAL DESIGN
# =========================================================

def apply_global_style():

    st.markdown(
        """
        <style>

        /* ================================
           MAIN APP
           ================================ */

        .stApp {
            background:
                radial-gradient(
                    circle at 85% 10%,
                    rgba(20, 184, 166, 0.08),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 10% 80%,
                    rgba(34, 197, 94, 0.06),
                    transparent 30%
                ),
                #061512;

            color: #F0FDF4;
        }


        /* ================================
           CONTENT WIDTH
           ================================ */

        .block-container {
            max-width: 1400px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }


        /* ================================
           SIDEBAR
           ================================ */

        section[data-testid="stSidebar"] {

            background:
                linear-gradient(
                    180deg,
                    #061411,
                    #071A17
                ) !important;

            border-right: 1px solid #183D35;
        }

        section[data-testid="stSidebar"] * {
            color: #D1FAE5 !important;
        }


        /* ================================
           HEADINGS
           ================================ */

        h1 {
            color: #F0FDF4 !important;
            font-weight: 800 !important;
        }

        h2 {
            color: #5EEAD4 !important;
            font-weight: 750 !important;
        }

        h3 {
            color: #A7F3D0 !important;
        }

        p {
            color: #D1FAE5;
        }


        /* ================================
           HERO
           ================================ */

        .eco-hero {

            position: relative;

            min-height: 300px;

            padding: 50px;

            border-radius: 28px;

            overflow: hidden;

            background:
                linear-gradient(
                    135deg,
                    rgba(5, 35, 28, 0.98),
                    rgba(7, 29, 24, 0.96)
                );

            border: 1px solid #24584B;

            box-shadow:
                0 20px 60px rgba(0, 0, 0, 0.30);

            margin-bottom: 35px;
        }


        .eco-hero-content {

            position: relative;

            z-index: 2;

            max-width: 58%;
        }


        .eco-hero-image {

            position: absolute;

            right: 0;

            top: 0;

            width: 45%;

            height: 100%;

            object-fit: cover;

            opacity: 0.72;

            mask-image:
                linear-gradient(
                    to right,
                    transparent,
                    black 25%
                );
        }


        .hero-label {

            color: #5EEAD4;

            font-size: 13px;

            font-weight: 800;

            letter-spacing: 2px;

            margin-bottom: 15px;
        }


        .hero-title {

            font-size: 58px;

            line-height: 1.05;

            font-weight: 850;

            background:
                linear-gradient(
                    90deg,
                    #22C55E,
                    #5EEAD4
                );

            -webkit-background-clip: text;

            -webkit-text-fill-color: transparent;

            margin-bottom: 18px;
        }


        .hero-description {

            font-size: 18px;

            line-height: 1.7;

            color: #CDE8DF;

            max-width: 700px;
        }


        /* ================================
           BADGE
           ================================ */

        .eco-badge {

            display: inline-block;

            padding: 7px 14px;

            border-radius: 999px;

            background: rgba(20, 184, 166, 0.10);

            border: 1px solid #24584B;

            color: #5EEAD4;

            font-size: 12px;

            font-weight: 700;

            letter-spacing: 1px;

            margin-bottom: 20px;
        }


        /* ================================
           CARDS
           ================================ */

        .eco-card {

            background:
                linear-gradient(
                    145deg,
                    #102D27,
                    #0C241F
                );

            border: 1px solid #24584B;

            border-radius: 20px;

            padding: 26px;

            min-height: 175px;

            transition:
                transform 0.25s ease,
                border-color 0.25s ease,
                box-shadow 0.25s ease;

            margin-bottom: 20px;
        }


        .eco-card:hover {

            transform: translateY(-5px);

            border-color: #2DD4BF;

            box-shadow:
                0 12px 35px
                rgba(0, 0, 0, 0.25);
        }


        .eco-card-icon {

            font-size: 34px;

            margin-bottom: 15px;
        }


        .eco-card-title {

            color: #F0FDF4;

            font-size: 21px;

            font-weight: 750;

            margin-bottom: 10px;
        }


        .eco-card-text {

            color: #B9DCD1;

            line-height: 1.65;
        }


        /* ================================
           IMAGE BOX
           ================================ */

        .eco-image-box {

            border-radius: 22px;

            overflow: hidden;

            border: 1px solid #24584B;

            box-shadow:
                0 15px 45px
                rgba(0, 0, 0, 0.25);

            background: #102D27;
        }


        /* ================================
           INSIGHT
           ================================ */

        .eco-insight {

            background:
                linear-gradient(
                    135deg,
                    #0E3028,
                    #102D27
                );

            border-left: 4px solid #2DD4BF;

            border-radius: 15px;

            padding: 20px;

            margin: 12px 0;
        }


        .eco-insight-title {

            color: #5EEAD4;

            font-weight: 750;

            margin-bottom: 6px;
        }


        .eco-insight-text {

            color: #CDE8DF;

            line-height: 1.6;
        }


        /* ================================
           ACTION CARDS
           ================================ */

        .eco-action {

            background: #0D2821;

            border: 1px solid #24584B;

            border-radius: 18px;

            padding: 22px;

            margin-bottom: 15px;
        }


        .eco-action-number {

            color: #22C55E;

            font-weight: 850;

            font-size: 13px;

            letter-spacing: 1px;
        }


        .eco-action-title {

            color: #F0FDF4;

            font-size: 19px;

            font-weight: 700;

            margin-top: 5px;

            margin-bottom: 8px;
        }


        .eco-action-text {

            color: #B9DCD1;

            line-height: 1.6;
        }


        /* ================================
           BUTTONS
           ================================ */

        .stButton button {

            background:
                linear-gradient(
                    90deg,
                    #166534,
                    #0F766E
                ) !important;

            color: #FFFFFF !important;

            border: 1px solid #2DD4BF !important;

            border-radius: 12px !important;

            font-weight: 700 !important;
        }


        .stButton button:hover {

            background:
                linear-gradient(
                    90deg,
                    #15803D,
                    #0D9488
                ) !important;

            color: #FFFFFF !important;

            border-color: #5EEAD4 !important;
        }


        /* ================================
           FOOTER
           ================================ */

        .eco-footer {

            margin-top: 60px;

            padding: 25px;

            text-align: center;

            border-top: 1px solid #183D35;

            color: #7FAFA2;

            line-height: 1.8;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# HERO COMPONENT
# =========================================================

def hero(
    label,
    title,
    description,
    image_path=None
):

    image_html = ""

    if image_path and os.path.exists(image_path):

        image_html = f"""
        <img
            src="{image_path}"
            class="eco-hero-image"
        >
        """

    st.markdown(
        f"""
        <div class="eco-hero">

            {image_html}

            <div class="eco-hero-content">

                <div class="hero-label">
                    {label}
                </div>

                <div class="hero-title">
                    {title}
                </div>

                <div class="hero-description">
                    {description}
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# BADGE
# =========================================================

def badge(text):

    st.markdown(
        f"""
        <div class="eco-badge">
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# CARD
# =========================================================

def card(icon, title, text):

    st.markdown(
        f"""
        <div class="eco-card">

            <div class="eco-card-icon">
                {icon}
            </div>

            <div class="eco-card-title">
                {title}
            </div>

            <div class="eco-card-text">
                {text}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# INSIGHT
# =========================================================

def insight(title, text):

    st.markdown(
        f"""
        <div class="eco-insight">

            <div class="eco-insight-title">
                {title}
            </div>

            <div class="eco-insight-text">
                {text}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# ACTION
# =========================================================

def action(number, title, text):

    st.markdown(
        f"""
        <div class="eco-action">

            <div class="eco-action-number">
                {number}
            </div>

            <div class="eco-action-title">
                {title}
            </div>

            <div class="eco-action-text">
                {text}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

def footer():

    st.markdown(
        """
        <div class="eco-footer">

            🌱 <b>EcoSense AI</b>

            <br>

            AI for Sustainability • SDG 11 • SDG 12 • SDG 13

            <br>

            Real-Time Environmental Intelligence

        </div>
        """,
        unsafe_allow_html=True
    )