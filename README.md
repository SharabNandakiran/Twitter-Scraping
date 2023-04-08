# Twitter-Scraping
Data scraping from the twitter.
Built this app for Twitter Scraping by creating a web app using Streamlit. It scrapes the twitter data for the given hashtag/ keyword for the given period using snscrape library. The tweets are uploaded in MongoDB and can be dowloaded as CSV or a JSON file.

# Tech Stack
Language: Python Libraries: Snscrape, pandas, pickle, pymongo NoSQL Database:: MongoDB GUI Framework: Streamlit Web Hosting: Netlify

# Scraping the tweet
To scrap the data Snscrape python library is used. The TweetSearchScrape() method scrape the Twitter data without Twitter API. The method is passed with a query conating the hashtag to be search and the search dates (From start date to end date)

