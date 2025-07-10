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

