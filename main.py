from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build
import key
DEVELOPER_KEY = key
VIDEO_ID = "UkXI-zPcDIM"

# def parseJSON(file):

def transcriptify(video_id):
    youtube = build("youtube", "v3", developerKey=DEVELOPER_KEY.key)
    return YouTubeTranscriptApi.get_transcript(video_id)

print(transcriptify(VIDEO_ID))
