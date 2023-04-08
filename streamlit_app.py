#import snscrape.modules.twitter as sntwitter
import streamlit as st
import pandas as pd
import pymomgo
#from pymongo import MongoClient
from PIL import Image
from datetime import date
import json


def main():
    tweets = 0
    st.title("Twitter Scraping")
    menu = ["Home", "About", "Search", "Display", "Download"]
    choice = st.sidebar.selectbox("Menu", menu)
