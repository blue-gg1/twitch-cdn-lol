import datetime
import hashlib
import os
import random
import re
from datetime import timedelta
import grequests
import requests
import sys
from bs4 import BeautifulSoup
from moviepy.editor import concatenate_videoclips, VideoFileClip
from natsort import natsorted
import subprocess
yt_dlp_path = '/usr/bin/ls'
# user_url = sys.argv[1]

def download_m3u8_via_ytdlp(url):
    if os.path.isfile(yt_dlp_path) is True:
        subprocess.run([yt_dlp_path, url])
    else:
        print("No yt-dlp. get yt-dlp or change the path")
    pass
    

download_m3u8_via_ytdlp('https://www.youtube.com/watch?v=dQw4w9WgXcQ')