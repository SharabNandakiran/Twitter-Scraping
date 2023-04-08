#import snscrape.modules.twitter as sntwitter
import streamlit as st
import pandas as pd
#import pymongo
#from pymongo import MongoClient
from PIL import Image
from datetime import date
import json



def main():
  tweets = 0
  st.title("Twitter Scraping")
  # Menus used in Twitter Scrape web app -- 5 menus are used
  menu = ["Home","About","Search","Display","Download"]
  choice = st.sidebar.selectbox("Menu",menu)
  # Menu 1 is Home page 
  if choice=="Home":
    st.write('''This app is a Twitter Scraping web app created using Streamlit. 
             It scrapes the twitter data for the given hashtag/ keyword for the given period.
             The tweets are uploaded in MongoDB and can be dowloaded as CSV or a JSON file.''')

  # Menu 2 is about the Twitter Scrape libraries, databases and apps
  elif choice=="About":
    # Info about Twitter Scrapper
    with st.expander("Twitter Scrapper"):
      st.write('''Twitter Scraper will scrape the data from Public Twitter profiles.
                    It will collect the data about **date, id, url, tweet content, users/tweeters,reply count, 
                    retweet count, language, source, like count, followers, friends** and lot more information 
                    to gather the real facts about the Tweets.''')

    # Info about Snscraper
    with st.expander("Snscraper"):
      st.write('''Snscrape is a scraper for social media services like *twitter, faceboook, instagram and so on*. 
                   It scrapes **user profiles, hashtages, other tweet information** and returns the discovered items from the relavent posts/tweets.''')

    # Info about MongoDB database
    with st.expander("Mondodb"):
      st.write('''MongoDB is an open source document database used for storing unstrcutured data. The data is stored as JSON like documents called BSON. 
                  It is used by developers to work esaily with real time data analystics, content management and lot of other web applications.''')

    # Info about Streamlit framework
    with st.expander("Streamlit"):
      st.write('''Streamlit is a **awesome opensource framwork used for buidling highly interactive sharable web applications*** in python language. 
                  Its easy to share *machine learning and datasciecne web apps* using streamlit.
                  It allows the app to load the large set of datas from web for manipulation and  performing expensive computations.''')
