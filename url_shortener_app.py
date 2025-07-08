import streamlit as st
import pyshorteners as pyst

st.set_page_config(page_title="Url Shortner",page_icon="🔗",)
shortener=pyst.Shortener()

st.markdown("<h1 style='text-align:center;'>URL SHORTENER</h1>",unsafe_allow_html=True)
form=st.form("Name")
url=form.text_input("Place URL HERE")
s_btn=form.form_submit_button("search")
if s_btn:
  shortener_url=shortener.tinyurl.short(url)
  st.markdown("### Shortened URL")
  st.markdown(f"<h6 style='text-align:center;'>{shortener_url}</h6>",unsafe_allow_html=True)
  
  