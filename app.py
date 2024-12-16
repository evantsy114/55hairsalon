#app.py

import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_location = load_lottieurl("https://lottie.host/90b18f67-1c3b-450c-b0fd-f90e65e4a4c2/Qtp5qm3GVa.json")

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
    st.title("Services")
if selected == "Contact":
    st.title("Contact")
if selected == "Book Now":
    st.title("Book Now")
