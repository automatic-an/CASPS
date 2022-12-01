import contentBot.video.speeches
from pathlib import Path
from mutagen.mp3 import MP3
from contentBot.utils.console import print_step, print_substep
from rich.progress import track
from random import choice


#which text to speech library is being used

#provider choices: "streamlabs", "google", "pyttsx"

#connects the reddit content to the tts provider
def save_text_to_mp3(reddit_obj, provider: str, post_description: bool, voice_index: int, min_video_lenght: int):

    if provider.strip().lower() == "streamlabs":
        ttsProvider = contentBot.video.speeches.StreamLabsPolly()
    
    if provider.strip().lower() == "google":
        ttsProvider = contentBot.video.speeches.GTTS()
    
    if provider.strip().lower() == "pyttsx":
        ttsProvider = contentBot.video.speeches.PYTTSX()

    the_speaker = ttsProvider.voices[voice_index]

    # if the voice index is 6969, the voice will be generated randomly
    if voice_index == 6969:
        the_speaker = choice(ttsProvider.voices)
    

    print_step("Saving Text to MP3 files...")
    length = 0

    # Create a folder for the mp3 files.
    Path("contentBot/assets/mp3").mkdir(parents=True, exist_ok=True)

    #try:
        #Path(f"contentBot/assets/mp3/title.mp3").unlink()
    #except:
        #print("!!error title deleting!!")


    contentBot.video.speeches.main(reddit_obj["thread_title"], "title", the_speaker, ttsProvider)
    
    length += MP3(f"contentBot/assets/mp3/title.mp3").info.length

    #try:
        #Path(f"contentBot/assets/mp3/posttext.mp3").unlink()
    #except:
        #print("!!error post thread deleting!!")

# BUGGY RIGHT NOW SO DONT USE THIS
# this is the post's description. You can choose if you want the wall of text to your video or not.
    if post_description and reddit_obj["thread_post"] != "":

        contentBot.video.speeches.main(reddit_obj["thread_post"], "posttext", the_speaker, ttsProvider)

        length += MP3(f"contentBot/assets/mp3/posttext.mp3").info.length

    #try:
        #for i in range(0,20):
            #Path(f"contentBot/assets/mp3/{i}.mp3").unlink()
    #except:
        #print("!!error index deleting!!")

    for idx, comment in track(enumerate(reddit_obj["comments"]), "Saving..."):
        # ! Stop creating mp3 files if the length is greater than 50 seconds. This can be longer, but this is just a good starting point
        if length > min_video_lenght:
            break

        contentBot.video.speeches.main(comment["comment_body"], f"{idx}", the_speaker, ttsProvider)
        
        length += MP3(f"contentBot/assets/mp3/{idx}.mp3").info.length

    print_substep("Saved Text to MP3 files successfully.", style="bold green")
    #return the index so we know how many screenshots of comments we need to make.
    return length, idx
