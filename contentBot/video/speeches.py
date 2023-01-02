import sys
import re
from ntpath import realpath
import requests, base64, random, argparse, os
from gtts import gTTS
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError, ProfileNotFound
import pyttsx3
from requests.exceptions import JSONDecodeError
import time as pytime
from datetime import datetime
from time import sleep


if sys.version_info[0] >= 3:
    from datetime import timezone


voices_name = [
    "Brian",
    "Emma",
    "Russell",
    "Joey",
    "Matthew",
    "Joanna",
    "Kimberly",
    "Amy",
    "Geraint",
    "Nicole",
    "Justin",
    "Ivy",
    "Kendra",
    "Salli",
    "Raveena",
]


def check_ratelimit(response: "Response"):
    """
    Checks if the response is a ratelimit response.
    If it is, it sleeps for the time specified in the response.
    """
    if response.status_code == 429:
        try:
            time = int(response.headers["X-RateLimit-Reset"])
            print(f"Ratelimit hit. Sleeping for {time - int(pytime.time())} seconds.")
            sleep_until(time)
            return False
        except KeyError:  # if the header is not present, we don't know how long to wait
            return False

    return True


def sleep_until(time):
    """
    Pause your program until a specific end time.
    'time' is either a valid datetime object or unix timestamp in seconds (i.e. seconds since Unix epoch)
    """
    end = time

    # Convert datetime to unix timestamp and adjust for locality
    if isinstance(time, datetime):
        # If we're on Python 3 and the user specified a timezone, convert to UTC and get the timestamp.
        if sys.version_info[0] >= 3 and time.tzinfo:
            end = time.astimezone(timezone.utc).timestamp()
        else:
            zoneDiff = pytime.time() - (datetime.now() - datetime(1970, 1, 1)).total_seconds()
            end = (time - datetime(1970, 1, 1)).total_seconds() + zoneDiff

    # Type check
    if not isinstance(end, (int, float)):
        raise Exception("The time parameter is not a number or datetime object")

    # Now we wait
    while True:
        now = pytime.time()
        diff = end - now

        #
        # Time is up!
        #
        if diff <= 0:
            break
        else:
            # 'logarithmic' sleeping to minimize loop iterations
            sleep(diff / 2)


#Google text to speech
class GTTS:
    def __init__(self):

        self.max_chars = 5000
        self.voices = ["en"]

    def tts(self, text: str, filename: str, speaker: str):
        gtts_tts = gTTS(text=text, lang=speaker, slow=False)
        gtts_tts.save(f".\\contentBot\\assets\\mp3\\{filename}.mp3")


#Amazon web services text to speech
#NOT WORKING WITHOUT CONFIGURED AWS CREDENTIALS
class AWSPolly:
    def __init__(self):
        self.max_chars = 3000
        self.voices = voices_name

    def tts(
        self,
        text: str,
        filename: str,
        speaker: str
        ):
        
        session = Session(profile_name="polly")
        polly = session.client("polly")
        voice = speaker
        
        response = polly.synthesize_speech(
            Text=text, OutputFormat="mp3", VoiceId=voice, Engine="neural"
        )
        
        file = open(f".\\contentBot\\assets\\mp3\\{filename}.mp3", "wb")
        file.write(response["AudioStream"].read())
        file.close()


#pyttsx text to speech
class PYTTSX:
    def __init__(self):
        self.max_chars = 5000
        self.voices = [0,1,2]

    def tts(
        self,
        text: str,
        filename: str,
        speaker: int 
    ):
        
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty(
            "voice", voices[speaker].id
        )  # changing index changes voices but ony 0 and 1 are working here
        engine.save_to_file(text, f"./contentBot/assets/mp3/{filename}.mp3")
        engine.runAndWait()


#Streamlabs text to speeh
class StreamLabsPolly:
    def __init__(self):
        self.url = "https://streamlabs.com/polly/speak"
        self.max_chars = 550
        self.voices = voices_name

    def tts(
        self,
        text: str,
        filename: str,
        speaker: str 
    ):

        body = {"voice": speaker, "text": text, "service": "polly"}
        response = requests.post(self.url, data=body)
        if not check_ratelimit:
            self.tts(text, filename, speaker)
        else:
            voice_data = requests.get(response.json()["speak_url"])
            file = open(f".\\contentBot\\assets\\mp3\\{filename}.mp3", "wb")
            file.write(voice_data.content)
            file.close()


#probably the right path:
# f".\\contentBot\\assets\\mp3\\{voice_clip_name}"
# f".\\contentBot\\assets\\mp3\\{filename}"

def main(text: str, filename: str, speaker, provider):

    text=re.sub('((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*', '', text)

    text = text.replace("+", "plus")
    text = text.replace("&", "and")
    text = text.replace("~", "")
    text = text.replace("_", "")
    text = text.replace(">", "")
    text = text.replace("<", "")
    text = text.replace("idk", "i don't know")

    if len(text) >= provider.max_chars:
        raise ValueError("too many characters!!!\ntoo many characters!!!\ntoo many characters!!!")

    provider.tts(text, filename, speaker)
    