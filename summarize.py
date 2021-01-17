import functions
from functions import *
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build
import key
import functions
import requests
import json

def summarize(video_id):
    DEVELOPER_KEY = key
    SMMRY_KEY = "4253DF69B4"
    PASTEBIN_KEY = "5dauh7RWr65Ni0m9atsDiL5UfAw3g1bU"
    VIDEO_ID = video_id
    youtube = build("youtube", "v3", developerKey=DEVELOPER_KEY.key)
    transcript = YouTubeTranscriptApi.get_transcript(VIDEO_ID)

    string = ""
    for i in transcript:
        string = string + i["text"] + " " 
    string = string.replace('\n', ' ')

    parameters = {'api_dev_key': PASTEBIN_KEY, 'api_paste_code': string, 'api_paste_private': 0, 'api_option': 'paste'}

    r = requests.post("https://pastebin.com/api/api_post.php", data=parameters)
    pasteURL = r.text.split("/")[-1]
    URL = "https://pastebin.com/raw/" + pasteURL

    parameters = {'SM_API_KEY':SMMRY_KEY,'SM_URL':URL}
    r = requests.get("https://api.smmry.com", params=parameters)
    r = json.loads(r.text)
    print(r["sm_api_content"])

    return 

