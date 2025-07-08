# url-shortener
shortening the url


# URL Shortener App

A simple web application built with Streamlit and `pyshorteners` to quickly shorten long URLs.

## ✨ Features

* **Easy to Use:** Intuitive interface for quick URL shortening.
* **Powered by TinyURL:** Utilizes the TinyURL service for reliable URL shortening.
* **Instant Result:** Get your shortened URL immediately after submission.
* **Copy Button:** Attempts to copy the shortened URL to your clipboard (see important note below).

## 🚀 How to Run Locally

Follow these steps to get the URL Shortener running on your local machine:

### 1. Prerequisites

Make sure you have Python installed (Python 3.7+ is recommended).

### 2. Prepare your Application Code

Save your Streamlit application code as `url_shortener_app.py` (or any other `.py` file).

```python
import streamlit as st
import pyshorteners as pyst
import pyperclip

shortener=pyst.Shortener()

# Define the copying function
# This function uses pyperclip to copy to the system clipboard
def copying():
    # Ensure shortener_url is accessible; in Streamlit's rerun model,
    # this might need careful handling if shortener_url isn't global or passed.
    # For this specific setup, it's captured from the global scope within the if s_btn block.
    try:
        pyperclip.copy(st.session_state.get('last_shortened_url', ''))
        st.toast("URL copied to clipboard!")
    except pyperclip.PyperclipException as e:
        st.error(f"Failed to copy to clipboard. Error: {e}. Pyperclip may not be supported on this system/environment.")
        st.info("You may need to manually copy the URL or ensure required clipboard utilities are installed.")


st.markdown("<h1 style='text-align:center;'>URL SHORTENER</h1>",unsafe_allow_html=True)

# Use st.form for grouping input and button
with st.form("url_shortener_form"):
    url=st.text_input("Place URL HERE")
    s_btn=st.form_submit_button("Shorten URL") # Changed button text for clarity

Here's the README.md file specifically for the exact code you've provided:

URL Shortener App
A straightforward web application built with Streamlit and pyshorteners to shorten URLs.

✨ Features
Easy URL Shortening: Quickly convert long URLs into shorter ones using the TinyURL service.

Simple Interface: A clean and intuitive design for ease of use.

Copy Button: Includes a button to attempt copying the shortened URL to the clipboard.

🚀 How to Run Locally
Follow these steps to set up and run the URL Shortener on your local machine:

1. Prerequisites
Ensure you have Python installed (Python 3.7+ is recommended).

2. Prepare your Application Code
Save the following code into a file named url_shortener_app.py:

Python

import streamlit as st
import pyshorteners as pyst
import pyperclip

shortener=pyst.Shortener()

# Define the copying function
# Note: shortener_url must be accessible in this scope for on_click to work.
# In Streamlit, this often means it needs to be globally available or managed via session_state.
# In the provided structure, it relies on shortener_url being defined in the main script scope
# when copying() is called via on_click during a rerun.
def copying():
    # This function expects 'shortener_url' to be defined in the global scope
    # or passed in a way accessible here. Streamlit's rerun model makes global
    # variable access from on_click functions work, but can sometimes be less robust
    # than using st.session_state for persistent data.
    try:
        pyperclip.copy(shortener_url)
        st.toast("URL copied to clipboard!") # Added toast for user feedback
    except pyperclip.PyperclipException as e:
        st.error(f"Failed to copy: {e}. Pyperclip may not be supported in this environment.")
        st.info("Please manually copy the URL.")


st.markdown("<h1 style='text-align:center;'>URL SHORTENER</h1>",unsafe_allow_html=True)

# Use st.form for grouping input and button for better structure
with st.form("url_shortener_form"):
    url=st.text_input("Place URL HERE")
    s_btn=st.form_submit_button("search")

if s_btn:
    if url: # Ensure a URL is provided
        try:
            shortener_url=shortener.tinyurl.short(url)
            st.markdown("### Shortened URL")
            st.markdown(f"<h6 style='text-align:center;'>{shortener_url}</h6>",unsafe_allow_html=True)
            
            # The copy button, using on_click to call the copying function
            st.button("copy",on_click=copying)
        except Exception as e:
            st.error(f"An error occurred while shortening the URL: {e}")
            st.info("Please ensure the URL is valid and accessible.")
    else:
        st.warning("Please enter a URL to shorten.")

3. Install Dependencies
Create a file named requirements.txt in the same directory as your url_shortener_app.py file. Add the following lines to it:

streamlit
pyshorteners
pyperclip
Then, install these dependencies from your terminal:

pip install -r requirements.txt

4. Run the Streamlit App
Navigate to the directory where you saved your files in your terminal or command prompt, and execute:


streamlit run url_shortener_app.py
Your web browser should automatically open the application (usually at http://localhost:8501).

