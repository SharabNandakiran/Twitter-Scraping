#import snscrape.modules.twitter as sntwitter
#import streamlit as st
#import pandas as pd
#import pymongo
#from pymongo import MongoClient
#from PIL import Image
#from datetime import date
#import json


client = pymongo.MongoClient("mongodb://localhost:27017")
twtdb = client.TweetScrap
twtdb_main = twtdb.twitterproj

def main():
  tweets = 0
  st.title("Twitter Scraping")
  menu = ["Home","About","Search","Display","Download"]
  choice = st.sidebar.selectbox("Menu",menu)


  if choice=="Home":
    st.write('''This app is a Twitter Scraping web app created using Streamlit. 
             It scrapes the twitter data for the given hashtag/ keyword for the given period.
             The tweets are uploaded in MongoDB and can be dowloaded as CSV or a JSON file.''')

  
  elif choice=="About":
    with st.expander("Twitter Scrapper"):
      st.write('''Twitter Scraper will scrape the data from Public Twitter profiles.
                    It will collect the data about **date, id, url, tweet content, users/tweeters,reply count, 
                    retweet count, language, source, like count, followers, friends** and lot more information 
                    to gather the real facts about the Tweets.''')

    with st.expander("Snscraper"):
      st.write('''Snscrape is a scraper for social media services like *twitter, faceboook, instagram and so on*. 
                   It scrapes **user profiles, hashtages, other tweet information** and returns the discovered items from the relavent posts/tweets.''')

    with st.expander("Mondodb"):
      st.write('''MongoDB is an open source document database used for storing unstrcutured data. The data is stored as JSON like documents called BSON. 
                  It is used by developers to work esaily with real time data analystics, content management and lot of other web applications.''')

    with st.expander("Streamlit"):
      st.write('''Streamlit is a **awesome opensource framwork used for buidling highly interactive sharable web applications*** in python language. 
                  Its easy to share *machine learning and datasciecne web apps* using streamlit.
                  It allows the app to load the large set of datas from web for manipulation and  performing expensive computations.''')

  elif choice=="Search":
    twtdb_main.delete_many({})

    with st.form(key='form1'):
      st.subheader("Tweet searching Form")
      st.write("Enter the hashtag or keyword to perform the twitter scraping👇#")
      query = st.text_input('Hashtag or keyword')

      st.write("Enter the limit for the data scraping: Maximum limit is 1000 tweets")
      limit = st.number_input('Insert a number',min_value=0,max_value=1000,step=10)

      st.write("Enter the Starting date to scrap the tweet data")
      start = st.date_input('Start date')
      end = st.date_input('End date')
      
      submit_button = st.form_submit_button(label="Tweet Scrap")
    
    if submit_button:
      st.success(f"Tweet hashtag {query} received for scraping".format(query))

      for tweet in sntwitter.TwitterSearchScraper(f'from:{query} since:{start} until:{end}').get_items():
        if tweets == limit:
          break
        else:      
          new = {"date":tweet.date,"id":tweet.id, "url":tweet.url, "Content":tweet.content, "user":tweet.user.username, "replycount":tweet.replyCount, "retweetcount":tweet.retweetCount, "source":tweet.source, "likecount":tweet.likeCount}
          twtdb_main.insert_one(new)
          tweets += 1
      
      df = pd.DataFrame(list(twtdb_main.find()))
      cnt = len(df)
      st.success(f"Total number of tweets scraped for the input query is := {cnt}".format(cnt))

  elif choice=="Display":
    df = pd.DataFrame(list(twtdb_main.find()))
    st.dataframe(df)  

  else:
    col1, col2 = st.columns(2)

    with col1:
      st.write("Download the tweet data as CSV File")
      df = pd.DataFrame(list(twtdb_main.find()))
      df.to_csv('twittercsv.csv')
      def convert_df(data):
        return df.to_csv().encode('utf-8')
      csv = convert_df(df)
      st.download_button(
                        label="Download data as CSV",
                        data=csv,
                        file_name='twtittercsv.csv',
                        mime='text/csv',
                        )
      st.success("Successfully Downloaded data as CSV")

    with col2:
      st.write("Download the tweet data as JSON File")
      twtjs = df.to_json(default_handler=str).encode()
      obj = json.loads(twtjs)
      js = json.dumps(obj, indent=4)
      st.download_button(
                        label="Download data as JSON",
                        data=js,
                        file_name='twtjs.js',
                        mime='text/js',
                        )
      st.success("Successfully Downloaded data as JSON")

main()
