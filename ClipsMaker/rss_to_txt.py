from libs.rss_reader import send_to_telegram
from libs.rss_fetch import get_twitch_rss_feed
from libs.settings import twitch_channel, twitch_channel_list
import time
import os

# call the functions to get twtich videos]\
for i in twitch_channel_list:
  print(i)
  get_twitch_rss_feed(i)

# send the URLs to telegram
take_file = open('libs/urls.rss' , 'r')
# print(take_file.readlines())
for i in take_file.readlines():
    # print(i)
    send_to_telegram('/VideoDownloadBot '+i)
    time.sleep(1.5)

# remove the RSS files 
if os.path.exists("libs/feed.rss"):
  os.remove("libs/feed.rss")
  print("nuked feed.rss")
else:
  print("The file does not exist")
if os.path.exists("libs/urls.rss"):
  os.remove("libs/urls.rss")
  print("nuked urls.rss")
else:
  print("The file does not exist")
