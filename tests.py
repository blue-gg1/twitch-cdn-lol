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
# user_url = sys.argv[1]

def download_m3u8_via_ytdlp(url):
    print(url)
    subprocess.run(['/usr/bin/yt-dlp', url])
    print("test")

download_m3u8_via_ytdlp('https://dgeft87wbj63p.cloudfront.net/7a87a653eedf41c2a0c5_trashfuturepodcast_39959329333_1694721629/chunked/index-dvr.m3u8')