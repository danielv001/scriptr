# YouTube Transcript/Subtitle API (including automatically generated subtitles)

This is an python API which allows you to get the transcripts/subtitles for a given YouTube video. It also works for automatically generated subtitles and it does not require a headless browser, like other selenium based solutions do!

## Install (testing)

It is recommended to [install this module by using pip](https://pypi.org/project/youtube-transcript-api/):

```
pip install youtube_transcript_api
```

If you want to use it from source, you'll have to install the dependencies manually:

```
pip install -r requirements.txt
```

## How to use it

You could either integrate this module into an existing application, or just use it via an CLI

### In code

To get a transcript for a given video you can do:

```python
from youtube_transcript_api import YouTubeTranscriptApi

YouTubeTranscriptApi.get_transcript(video_id)
```

This will return a list of dictionaries looking somewhat like this:

```python
[
    {
        'text': 'Hey there',
        'start': 7.58,
        'duration': 6.13
    },
    {
        'text': 'how are you',
        'start': 14.08,
        'duration': 7.58
    },
    # ...
]
```

To get transcripts for a list fo video ids you can call:

```python
YouTubeTranscriptApi.get_transcripts(video_ids)
```

### CLI

Execute the CLI script using the video ids as parameters and the results will be printed out to the command line:

```
youtube_transcript_api <first_video_id> <second_video_id> ...
```

If you would prefer to write it into a file or pipe it into another application, you can also output the results as json using the following line:

```
youtube_transcript_api --json <first_video_id> <second_video_id> ... > transcripts.json
```

## Warning

This code uses an undocumented part of the YouTube API, which is called by the YouTube web-client. So there is no guarantee that it won't stop working tomorrow, if they change how things work. I will however do my best to make things working again as soon as possible if that happens. So if it stops working, let me know!
