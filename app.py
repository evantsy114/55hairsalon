#app.py

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit.connections import ExperimentalBaseConnection
from streamlit_gsheets import GSheetsConnection
from PIL import Image
import pandas as pd
import datetime


if "center" not in st.session_state:
    layout = "wide"
else:
    layout = "centered" if st.session_state.center else "wide"

st.set_page_config(page_title="55 Hair Salon", page_icon=":tada:", layout=layout)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://cdn.vectorstock.com/i/500p/84/65/abstract-white-monochrome-background-vector-32028465.jpg")
}

[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.checkbox(
    "Viewing on a mobile?", key="center", value=st.session_state.get("center", False)
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

conn = st.connection("gsheets", type=GSheetsConnection)

lottie_location = load_lottieurl("https://lottie.host/90b18f67-1c3b-450c-b0fd-f90e65e4a4c2/Qtp5qm3GVa.json")

haircut_img = Image.open("haircut.jpg")
hairwash_img = Image.open("hairwash.jpg")
mencolour_img = Image.open("mencolour.jpeg")
womencolour_img = Image.open("womencolour.jpg")
menbleach_img = Image.open("menbleach.jpg")
womenbleach_img = Image.open("womenbleach.jpeg")
menperm_img = Image.open("menperm.jpeg")
womenperm_img = Image.open("womenperm.jpg")
rebond_img = Image.open("rebond.jpg")
treatment_img = Image.open("treatment.jpg")

selected = option_menu(
    menu_title=None,
    options=["Home","Services","Contact","Book Now"],
    icons=["house","cart","telephone","calendar3"],
    orientation="horizontal",
)

if selected == "Home":
    with st.container():
        st.subheader("Hi, Welcome to 55 Hair Salon :wave:")
        st.title("A Home-based Hair Salon | Since 2000")
        st.write("""
        Opening Hours:
        Mon, Thurs 9am-4pm
        Fri 9am-2pm
        Tues, Wed, Sat, Sun 9am-6pm
        (Appointment based)
        """)

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Location")
            st.write("#####")
            st.write("55, Lorong Greenwood 3C1, 93250 Kota Samarahan, Sarawak (near OUM)")
            st.write("[Google Map >](https://maps.app.goo.gl/mm9bm1QoDhXfEyZcA)")
        with right_column:
            st_lottie(lottie_location, height=300, key="location")
            
if selected == "Services":
    with st.container():
        st.title("Services")
        left_column,right_column = st.columns([1,2], gap="large")
        with left_column:
            st.image(haircut_img, width=350, caption=" ")
        with right_column:
            st.write("#####")
            st.subheader("Hair Cut")
            st.write("Estimated Time: 40 mins")
            st.write("Price (Kid / Adult): RM10 / RM12")

    with st.container():
        with left_column:
            st.image(hairwash_img, width=350, caption=" ")
        with right_column:
            st.write(" ")
            st.write(" ")
            st.write("#")
            st.subheader("Hair Wash")
            st.write("Estimated Time: 25 mins")
            st.write("Price (Men / Women): RM15 / RM18+")

    with st.container():
        with left_column:
            st.image(mencolour_img, width=350, caption=" ")
        with right_column:
            st.write(" ")
            st.write(" ")
            st.write("#")
            st.subheader("Colour (Men)")
            st.write("Estimated Time: 1 hour")
            st.write("Price: RM58+")

    with st.container():
        with left_column:
            st.image(womencolour_img, width=350, caption=" ")
        with right_column:
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.write("#")
            st.subheader("Colour (Women)")
            st.write("Estimated Time: 1 hour 30 mins")
            st.write("Price (Short / Mid / Long): RM68 / RM88 / RM108+")

    with st.container():
        with left_column:
            st.image(menbleach_img, width=350, caption=" ")
        with right_column:
            st.write(" ")
            st.write(" ")
            st.write("#")
            st.subheader("Bleach (Men)")
            st.write("Estimated Time: 45 mins")
            st.write("Price: RM30+")

    with st.container():
        with left_column:
            st.image(womenbleach_img, width=350, caption=" ")
        with right_column:
            st.write(" ")
            st.write(" ")
            st.write("#")
            st.subheader("Bleach (Women)")
            st.write("Estimated Time: 1 hour")
            st.write("Price (Short / Mid / Long): RM48 / RM68 / RM88+")

    with st.container():
        with left_column:
            st.image(menperm_img, width=350, caption=" ")
        with right_column:
            st.write(" ")
            st.write(" ")
            st.write("#")
            st.subheader("Perm (Men)")
            st.write("Estimated Time: 2 hours")
            st.write("Price: RM68+")

    with st.container():
        with left_column:
            st.image(womenperm_img, width=350, caption=" ")
        with right_column:
            st.write("##")
            st.subheader("Perm (Women)")
            st.write("Estimated Time: 3 hours")
            st.write("Price (Short / Mid / Long):")
            st.write("Cold Perm : RM68 / RM88 / RM128+")
            st.write("Digital Perm : RM88 / RM128 / RM188+")

    with st.container():
        with left_column:
            st.image(rebond_img, width=350, caption=" ")
        with right_column:
            st.write("##")
            st.subheader("Rebond")
            st.write("Estimated Time: 3 hours")
            st.write("Price (Short / Mid / Long): RM88 / RM128 / RM168+")

    with st.container():
        with left_column:
            st.image(treatment_img, width=350, caption=" ")
        with right_column:
            st.write("#")
            st.write(" ")
            st.write(" ")
            st.subheader("Treatment")
            st.write("Estimated Time: 40 mins")
            st.write("Price (Above / Below Shoulder): RM68 / RM88+")
    
if selected == "Contact":
    st.title("Contact")
    st.subheader("WhatsApp")
    st.write("[Click Me >](https://api.whatsapp.com/send/?phone=60104336314&text&type=phone_number&app_absent=0)")
    st.subheader("Instragram")
    st.write("[Click Me >](https://www.instagram.com/55hairsalon/)")

    
if selected == "Book Now":
    st.title("Book Now")
    existing_data = conn.read(worksheet="Sheet1",usecols=list(range(7)),ttl=5)
    existing_data = existing_data.dropna(how="all")

    SERVICES = [
        "Hair Cut",
        "Hair Wash",
        "Hair Colour",
        "Hair Bleach",
        "Hair Perm",
        "Hair Rebond",
        "Hair Treatment",
        ]

    with st.form(key="vendor_form"):
        name=st.text_input(label="Name*")
        email=st.text_input(label="Email")
        contact=st.text_input(label="Contact No.*")
        date=st.date_input("Appointment Date*", value=None)
        time=st.time_input("Appointment Time*", value=None)
        services=st.multiselect("Services*", options=SERVICES)

        st.markdown("**required*")

        submit_button = st.form_submit_button(label="Submit Appointment")

        if submit_button:
            if not name or not contact or not date or not time or not services:
                st.warning("Ensure all required fields are filled.")
                st.stop()
            else:
                st.write("Appointment Requested, Please Check Your Email or WhatsApp for Confirmation. Thank You.")
                vendor_data = pd.DataFrame(
                    [
                        {
                            "Name": name,
                            "Email": email,
                            "Contact No.": contact,
                            "Appointment Date": date,
                            "Appointment Time": time,
                            "Services": services,
                        }
                    ]
                )

                updated_df = pd.concat([existing_data, vendor_data], ignore_index=True)

                conn.update(worksheet="Sheet1", data=updated_df)
