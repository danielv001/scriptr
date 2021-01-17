import re                      # regular expression
import requests
import numpy as np             # for algebric functions
import os                      # to import files 
import pandas as pd
import key
import csv
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
DEVELOPER_KEY = key
youtube = build("youtube", "v3", developerKey=DEVELOPER_KEY.key)
playlist_id = "PLBDA2E52FB1EF80C9"

request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=25,
        playlistId=playlist_id
    )
response = request.execute()
video_ids = list()

for i in response["items"]:
        if(i["kind"] == "youtube#playlistItem"):
            video_ids.append(i["snippet"]["resourceId"]["videoId"])

while("nextPageToken" in response):
    nextPageToken = response["nextPageToken"]
    response = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=25,
        playlistId=playlist_id,
        pageToken=nextPageToken
    ).execute()
    for i in response["items"]:
        if(i["kind"] == "youtube#playlistItem"):
            video_ids.append(i["snippet"]["resourceId"]["videoId"])

print(video_ids)
transcripts = YouTubeTranscriptApi.get_transcripts(video_ids)
print(transcripts)
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['','transcript','subject'])
    for i in transcripts:
        string = ""
        id = -1
        for j in i:
            string = string + j["text"]
            id += 1

        writer.writerow([id,string,'world history'])


