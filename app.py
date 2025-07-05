import streamlit as st
from profanity_filter import censor_text

from model import is_profane  # Optional

st.title("🚫 Profanity Filter with ML")

comment = st.text_area("Enter your comment:")

if st.button("Check & Censor"):
    if comment:
        # Optional ML Prediction
        # if is_profane(comment):
        #     st.warning("⚠️ Profanity Detected!")

        censored = censor_text(comment)
        st.success("Censored Comment:")
        st.write(censored)
