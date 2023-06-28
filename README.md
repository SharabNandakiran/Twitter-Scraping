# Twitter-Scraping
Data scraping from the twitter.
Built this app for Twitter Scraping by creating a web app using Streamlit. It scrapes the twitter data for the given hashtag/ keyword for the given period using snscrape library. The tweets are uploaded in MongoDB and can be dowloaded as CSV or a JSON file.

# Tech Stack
Language: Python Libraries: Snscrape, pandas, pymongo NoSQL Database:: MongoDB, GUI Framework: Streamlit Web

# Scraping the tweet
To scrap the data Snscrape python library is used. The TweetSearchScrape() method scrape the Twitter data without Twitter API. The method is passed with a query conating the hashtag to be se search datarch and thees (From start date to end date)

# Upload thge data into Mongodb
Tweets that are scraped using the Snscrape library is inserted into the MongoDB database by establishing the client connection. The tweet datas are strored under the twitter db collections.

# Creating GUI
Used Streamlit app for creating the GUI for Twitter Scraping. Used menus for searching, dispalying the tweets and to download.

Menu 1 -- Home
Home page of the UI contains title of the app

Menu 2 -- About
Contains small description about the Twitter Scraping, Snscrape librray, MongoDB and Streamlit framework.

Menu 3 -- Search
Search menu which is used to search the tweet data using the #hashtag for given dates. Everytime the search menu deletes the existing datas while searching the new tweet in order to retrive the tweet information correctly.

Menu 4 -- Display
The scraped data from the MongoDB database are dispalyed as a DataFrame

Menu 5 -- Download
The scraped data from the MongoDB database is downloaded as CSV/ JSON file formats as per the requirement.

# Demo
Demo for the Twitter Scraping app can be find using the following linkedin link.https://www.linkedin.com/posts/nanda-kiran-b31071159_create-a-streamlit-app-for-scraping-twitterdata-activity-7050849729047367680-RQdo?utm_source=share&utm_medium=member_desktop
