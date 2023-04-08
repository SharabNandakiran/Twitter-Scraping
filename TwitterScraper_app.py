#import snscrape.modules.twitter as sntwitter
import streamlit as st
import pandas as pd
import pymongo
from pymongo import MongoClient
from PIL import Image
from datetime import date
import json



def main():
  tweets = 0
  st.title("Twitter Scraping")
  # Menus used in Twitter Scrape web app -- 5 menus are used
  menu = ["Home","About","Search","Display","Download"]
  choice = st.sidebar.selectbox("Menu",menu)
