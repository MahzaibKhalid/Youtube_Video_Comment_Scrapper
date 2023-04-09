from youtube_comment_scraper_python import *
import pandas as pd
import time

url = input("Enter the video URL:")
file = input("Enter the output file name: ")


youtube.open(url)
allcomments= []
for i in range(0,1):    
    result = youtube.video_comments()
    data = result['body']
    allcomments.extend(data)
    
df= pd.DataFrame(allcomments)
time.sleep(5)
df.to_csv(file)