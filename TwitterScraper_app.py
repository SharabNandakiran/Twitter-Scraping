import streamlit as st

def main():
  tweets = 0
  st.title("Twitter Scraping")
  # Menus used in Twitter Scrape web app -- 5 menus are used
  menu = ["Home","About","Search","Display","Download"]
  choice = st.sidebar.selectbox("Menu",menu)
