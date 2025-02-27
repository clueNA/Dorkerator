import streamlit as st
import json

# Define Google Dorking options
def google_dork(query, site=None, filetype=None, intitle=None, inurl=None, intext=None):
    dork = query
    if site:
        dork += f" site:{site}"
    if filetype:
        dork += f" filetype:{filetype}"
    if intitle:
        dork += f" intitle:{intitle}"
    if inurl:
        dork += f" inurl:{inurl}"
    if intext:
        dork += f" intext:{intext}"

st.title("Dorkerator: Google Dork Generator")
st.write("Generate Google Dorks for advanced Google searches.")

query = st.text_input("Query")
site = st.text_input("Site (e.g., .com, .edu, .org)")
filetype = st.text_input("Filetype (e.g., pdf, docx)")
intitle = st.text_input("Intitle (e.g., 'index of')")
inurl = st.text_input("Inurl (e.g., 'admin')")
intext = st.text_input("Intext (e.g., 'password')")

if st.button("Generate Dork"):
    dork = google_dork(query, site, filetype, intitle, inurl, intext)
    st.write("Generated Google Dork:")
    st.code(dork)
    st.markdown(f"[Search on Google](https://www.google.com/search?q={dork})", unsafe_allow_html=True)

st.write("Examples of Google Dorks:")
st.code('site:example.com')
st.code('filetype:pdf')
st.code('intitle:"index of"')
st.code('inurl:admin')
st.code('intext:password')
