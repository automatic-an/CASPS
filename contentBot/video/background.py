import random
from os import listdir, environ
from pathlib import Path
from random import randrange
from yt_dlp import YoutubeDL
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from contentBot.utils.console import print_step, print_substep


def get_start_and_end_times(video_length, length_of_clip):

    # new value is 30, old value was 5 and no plus 5 to video_length
    random_time = randrange(20, int(length_of_clip) - (int(video_length)+5))
    return random_time, random_time + video_length

def download_background():
    """Downloads the background video from youtube.

    Shoutout to: bbswitzer (https://www.youtube.com/watch?v=n_Dv4JMiwK8)
    """

    if not Path("contentBot/assets/mp4/background.mp4").is_file():
        print_step(
            "We need to download the Minecraft background video. This is fairly large but it's only done once."
        )

        print_substep("Downloading the background video... please be patient.")

        ydl_opts = {
            "outtmpl": "contentBot/assets/mp4/background.mp4",
            "merge_output_format": "mp4",
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download("https://www.youtube.com/watch?v=n_Dv4JMiwK8")

        print_substep("Background video downloaded successfully!", style="bold green")


def chop_background_video(video_length, video_folder: str):
    print_step("Finding a spot in the background video to chop...")
    choice = random.choice(listdir(f"contentBot/assets/backgrounds/{video_folder}"))
    #environ["background_credit"] = choice.split("-")[0]

    background = VideoFileClip(f"contentBot/assets/backgrounds/{video_folder}/{choice}")
    #background = VideoFileClip("contentBot/assets/mp4/background.mp4")

    start_time, end_time = get_start_and_end_times(video_length, background.duration)
    ffmpeg_extract_subclip(
        f"contentBot/assets/backgrounds/{video_folder}/{choice}",
        start_time,
        end_time,
        targetname=f"contentBot/assets/mp4/clip.mp4",
    )
    print_substep("Background video chopped successfully!", style="bold green")
 