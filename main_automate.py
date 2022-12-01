import contentBot.main
import multiprocessing
import datetime
import traceback
from time import sleep
from typing import Tuple, Callable, Dict

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from random import choices, randint


f_path = f"./log.txt"
f_path2 = f"./log2.txt"
multip_path = f"./multip_timeouts.txt"


def video_main(numb_of_uploads: int, provider: str, speaker_index: int, min_video_lenght: int, video_folder: str, gma: str, pas: str, saying: str, hashtags: str, tiktok_on: bool, tik_nam: str, tik_pas: str, subreddits: list, subreddits_weight: list, keywords= "incoming_upgrade"):

    driver = uc.Chrome(browser_executable_path="C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe",use_subprocess=True)
    #driver = uc.Chrome(use_subprocess=True)
    wait = WebDriverWait(driver, 45)

    try:
        if tiktok_on:
            driver.get("https://www.tiktok.com/")
            sleep(randint(3,13))
            driver.find_element(by='xpath', value='//button[@data-e2e="top-login-button"]').click()
            sleep(randint(1,7))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"Use phone / email / username")]'))).click()
            sleep(randint(3,7))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Log in with email or username")]'))).click()
            sleep(randint(6,17))
            wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="username"]'))).click()
            sleep(randint(1,3))
            wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="username"]'))).send_keys(tik_nam)
            sleep(randint(3,14))
            wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).click()
            sleep(randint(1,3))
            wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).send_keys(tik_pas)
            sleep(randint(3,8))
            #wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-e2e="login-button"]'))).click()
            sleep(randint(1,4))

        #url = "https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
        url = "https://accounts.google.com/ServiceLogin/signinchooser?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
        driver.get(url)
        rand_time = randint(6,9)
        sleep(rand_time)
        wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).click()
        sleep(randint(1,3))
        wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(gma)
        rand_time = randint(1,3)
        sleep(rand_time)
        wait.until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).click()
        sleep(randint(1,3))
        wait.until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(pas)
        sleep(randint(2,4))
    except:
        driver.quit()
        current_time = datetime.datetime.now()
        file = open(f_path2, "a+")
        file.write(f"\n{current_time}: tiktok or youtube log in failed\n")
        file.close()


    for i in range(numb_of_uploads):

        while True:
            try:
                title = contentBot.main.main(provider, speaker_index, min_video_lenght, video_folder, subreddits, subreddits_weight)
                file = open("./contentBot/lenghtplustitle.txt", "a+")
                file.write(f"{len(title)}: {title}\n")
                file.close()
                break
            except:
                current_time = datetime.datetime.now()
                file = open(f_path, "a+")
                file.write(f"{current_time}: creating the final mp4 failed\n")
                file.close()
            

        try:
            video_title = title
            if len(title) > 100:
                video_title = saying
            #wait.until(EC.visibility_of_element_located((By.XPATH,  '//ytcp-button[id="create-icon"]'))).click()
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "style-scope ytd-topbar-menu-button-renderer"))).click()
            #driver.find_element_by_class_name("style-scope ytd-topbar-menu-button-renderer").click()
            sleep(randint(1,3))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "style-scope ytd-compact-link-renderer"))).click()
            #driver.find_element_by_class_name("style-scope ytd-compact-link-renderer").click()
            #driver.find_element_by_name("Filedata").send_keys("C:/Users/tsul/Desktop/automate/contentBot/assets/final_video.mp4")
            sleep(randint(1,4))
            wait.until(EC.presence_of_element_located((By.NAME, "Filedata"))).send_keys("C:/Users/tsul/Desktop/automate/contentBot/assets/final_video.mp4")
            rand_time = randint(6,12)
            sleep(rand_time)
            rand_del = randint(14,23)
            wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"))).click()
            sleep(randint(1,3))
            wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"))).send_keys(Keys.BACKSPACE*rand_del)
            sleep(randint(1,3))
            wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"))).send_keys(video_title)
            #wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"))).send_keys('Redditors telling some "REAL LIFE" advice and experiences. #shorts')
            sleep(randint(2,5))
            wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"))).click()
            sleep(randint(1,3))
            wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"))).send_keys(hashtags)
            sleep(randint(1,4))
            wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]"))).click()
            next_button = "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]"
            sleep(randint(1,3))
            wait.until(EC.element_to_be_clickable((By.XPATH, next_button))).click()
            sleep(randint(1,3))
            wait.until(EC.element_to_be_clickable((By.XPATH, next_button))).click()
            sleep(randint(1,3))
            wait.until(EC.element_to_be_clickable((By.XPATH, next_button))).click()
            sleep(randint(1,3))
            wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[2]"))).click()
            rand_time = randint(148,211)
            sleep(rand_time)
            wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]"))).click()
            rand_time = randint(14,22)
            sleep(rand_time)
            #wait.until(EC.element_to_be_clickable((By.XPATH, '//ytcp-button[id="close-button"]')))
            sleep(10)
            if tiktok_on:
                video_title = title
                if len(title) > 150:
                    video_title = saying
                driver.get("https://www.tiktok.com/")
                sleep(randint(3,13))
                wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-e2e="upload-icon"]'))).click()
                sleep(randint(1,7))
                wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/input'))).click()
                sleep(randint(1,4))
                wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/input'))).send_keys(video_title)
                sleep(randint(1,4))
                wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@type="file"]'))).send_keys("C:/Users/tsul/Desktop/automate/contentBot/assets/final_video.mp4")
                sleep(randint(1,3))
                wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="tiktok-switch__switch-inner"]'))).click()
                sleep(randint(65,89))
                wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "Post")]'))).click()
                sleep(randint(3,7))
            driver.get("https://www.youtube.com")
            sleep(randint(3,7))
        except:
            current_time = datetime.datetime.now()
            file = open(f_path2, "a+")
            file.write(f"{current_time}: tiktok or youtube video uploading failed")
            file.close()
            break
    try:
        driver.quit()
    except:
        pass



# TIMEOUT IMPLEMENTED WITH MULTIPROCESSING
# FORK FROM: https://flipdazed.github.io/blog/quant%20dev/parallel-functions-with-timeouts


def _lemmiwinks(func: Callable, args: Tuple[object], kwargs: Dict[str, object], q: multiprocessing.Queue):
    """lemmiwinks crawls into the unknown"""
    q.put(func(*args, **kwargs))

# current video folder choices: "citites-walking-drones","gtav","gym-fitness","minecraft-vaults","games"
# provider choices: "streamlabs", "google", "pyttsx"
def main_with_timeout(numb_of_uploads: int, timeout: int, provider: str, voice: int, min_video_lenght: int, video_folder: str, gma: str, pas: str, saying: str, hashtags: str, tiktok_on: bool, tik_nam: str, tik_pas: str, subreddits: list, subreddits_weight: list):

    try:
        q_worker = multiprocessing.Queue()
        proc = multiprocessing.Process(target=_lemmiwinks, args=(video_main, (numb_of_uploads,provider,voice,min_video_lenght,video_folder,gma,pas,saying,hashtags,tiktok_on,tik_nam,tik_pas,subreddits,subreddits_weight,), {}, q_worker))
        proc.start()      
        q_worker.get(timeout=timeout)
        proc.terminate()
        q_worker.close()
    except:
        print("timeout or error")
        print(traceback.print_exc())
        current_time = datetime.datetime.now()
        file = open(multip_path, "a+")
        file.write(f"\n{current_time}: multiprocessing timed out")
        file.close()
        proc.terminate()
        q_worker.close()


def instagram_upload(nam: str, pas: str):
    pass


def facebook_upload(nam: str, pas: str):
    pass


# def youtube_upload(gma: str, pas: str, saying: str, hashtags: str, subreddits= "incoming_upgrade", videos_file= "incoming_upgrade", keywords= "incoming_upgrade"):
    
#     while True:

#         try:
#             f = open("title.txt", "r")
#             title = f.read()
#             if title == 'TLDR' or title == "" or title == " ":
#                 title = saying

#             email = gma+'\n' # replace email
#             password = pas+'\n' # replace password

#             driver = uc.Chrome(use_subprocess=True)
#             wait = WebDriverWait(driver, 45)
#             #url = "https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
#             url = "https://accounts.google.com/ServiceLogin/signinchooser?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
#             driver.get(url)
#             rand_time = randint(6,9)
#             sleep(rand_time)

#             #driver.find_element_by_name("identifier").send_keys(email)
#             #driver.find_element_by_name("password").send_keys(password)
#             wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email)
#             wait.until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(password)

#             wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "style-scope ytd-topbar-menu-button-renderer"))).click()
#             #driver.find_element_by_class_name("style-scope ytd-topbar-menu-button-renderer").click()
#             wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "style-scope ytd-compact-link-renderer"))).click()
#             #driver.find_element_by_class_name("style-scope ytd-compact-link-renderer").click()
#             #driver.find_element_by_name("Filedata").send_keys("C:/Users/tsul/Desktop/automate/contentBot/assets/final_video.mp4")
#             wait.until(EC.presence_of_element_located((By.NAME, "Filedata"))).send_keys("C:/Users/tsul/Desktop/automate/contentBot/assets/final_video.mp4")
#             rand_time = randint(6,12)
#             sleep(rand_time)
#             rand_del = randint(14,23)
#             wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"))).send_keys(Keys.BACKSPACE*rand_del)
#             wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"))).send_keys(title)
#             #wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"))).send_keys('Redditors telling some "REAL LIFE" advice and experiences. #shorts')
#             wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"))).send_keys(hashtags)
#             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]"))).click()
#             next_button = "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]"
#             wait.until(EC.element_to_be_clickable((By.XPATH, next_button))).click()
#             wait.until(EC.element_to_be_clickable((By.XPATH, next_button))).click()
#             wait.until(EC.element_to_be_clickable((By.XPATH, next_button))).click()
#             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[2]"))).click()
#             rand_time = randint(148,211)
#             sleep(rand_time)
#             wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]"))).click()
#             rand_time = randint(14,22)
#             sleep(rand_time)
#             driver.quit()
#             current_time = datetime.datetime.now()
#             file = open(f_path2, "a+")
#             file.write(f"\n{current_time}: video uploading WORKED\n")
#             file.close()
#             break
#         except:
#             current_time = datetime.datetime.now()
#             file = open(f_path2, "a+")
#             file.write(f"\n{current_time}: video uploading FAILED")
#             file.close()

if __name__ == "__main__":

    current_time = datetime.datetime.now()
    print(f"start of the program: {current_time}")
    print(f"start of the program: {current_time}")
    print(f"start of the program: {current_time}")

    yt_file = open("accounts_yt.txt")
    yt_line = yt_file.readlines()
    yt_file.close()

    tik_file = open("accounts_tik.txt")
    tik_line = tik_file.readlines()
    tik_file.close()

    #while True:
    
    main_with_timeout(9,7200,"streamlabs",0,25,"citites-walking-drones",yt_line[0],yt_line[1],"#fedora #gentlemen #fedorafacts #shorts #reddit","#reddit #shorts #stories #story #redditstories #askreddit #fyp #foryou #foryoupage",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(9,7200,"streamlabs",0,40,"games",yt_line[2],yt_line[3],"#buzzbuzzbuzz #heartratespiking #redditors #reddit #shorts","#reddit #shorts #stories #story #redditstories #askreddit #fyp #foryou #foryoupage",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(9,7200,"streamlabs",0,30,"games",yt_line[4],yt_line[5],"#browhat #redditor #reddit #shorts","#reddit #shorts #stories #story #redditstories #askreddit #fyp #foryou #foryoupage",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(9,7200,"streamlabs",0,40,"gym-fitness",yt_line[6],yt_line[7],"#reddit #shorts #skippedlegday","#reddit #shorts #stories #story #redditstories #askreddit #redditmemes #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(9,7200,"streamlabs",0,30,"citites-walking-drones",yt_line[8],yt_line[9],"Answers from Redditors #backinmyday #reddit #shorts","#reddit #shorts #stories #story #redditstories #askreddit #redditmemes #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])
        
    main_with_timeout(9,7200,"streamlabs",0,35,"gtav",yt_line[10],yt_line[11],"#reddit #shorts #leredditarmie","#reddit #shorts #stories #story #redditstories #askreddit #redditmemes #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(4,3600,"streamlabs",0,40,"gtav",yt_line[12],yt_line[13],"#reddit #shorts","#reddit #shorts #stories #story #redditstories #askreddit #redditmemes #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(4,3600,"streamlabs",0,40,"gtav",yt_line[14],yt_line[15],"#shorts #reddit","#reddit #shorts #stories #story #redditstories #askreddit #redditmemes #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(4,3600,"streamlabs",0,40,"games",yt_line[16],yt_line[17],"#shorts #progamer #reddit","#reddit #shorts #stories #story #redditstories #askreddit #redditmemes #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(4,3600,"streamlabs",0,25,"games",yt_line[18],yt_line[19],"reddit is a meme #shorts #meme #reddit #redditmeme","#reddit #shorts #stories #story #redditstories #askreddit #redditmemes #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(4,3600,"streamlabs",0,40,"gtav",yt_line[20],yt_line[21],"lifes bussin #shorts #bussin #einsteinwaszoomer","#reddit #shorts #stories #story #redditstories #askreddit #redditmemes #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(4,3600,"streamlabs",0,35,"games",yt_line[22],yt_line[23],'reddit "in real life" experiences #shorts #reddit #internet',"#shorts #reddit #stories #story #redditstories #askreddit #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(4,3600,"streamlabs",0,35,"citites-walking-drones",yt_line[24],yt_line[25],"hmm its a mystery #shorts #reddit","#shorts #reddit #stories #story #redditstories #askreddit #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])
    
    main_with_timeout(4,3600,"streamlabs",0,40,"citites-walking-drones",yt_line[26],yt_line[27],"reddit be capping a lot #shorts #reddit #redditor","#shorts #reddit #stories #story #redditstories #askreddit #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(4,3600,"streamlabs",0,40,"citites-walking-drones",yt_line[28],yt_line[29],"welcome to the reddit-rice-fields mfkas #shorts #reddit","#shorts #reddit #stories #story #redditstories #askreddit #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(4,3600,"streamlabs",0,40,"citites-walking-drones",yt_line[30],yt_line[31],"buy twitter blue! #reddit #shorts","#shorts #reddit #stories #story #redditstories #askreddit #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(4,3600,"streamlabs",0,40,"citites-walking-drones",yt_line[32],yt_line[33],"#shorts #reddit","#shorts #reddit #stories #story #redditstories #askreddit #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(4,3600,"streamlabs",0,25,"citites-walking-drones",yt_line[34],yt_line[35],"just merican things #reddit #shorts","#shorts #reddit #stories #story #redditstories #askreddit #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    main_with_timeout(4,3600,"streamlabs",0,25,"citites-walking-drones",yt_line[36],yt_line[37],"#shorts #reddit","#shorts #reddit #stories #story #redditstories #askreddit #FYP #foryou #foryoupage #viral",False,tik_line[0],tik_line[1],["AskReddit","AskMen","AskWomen"],[5,1,1])

    current_time = datetime.datetime.now()
    print(f"end of the program: {current_time}")
    print(f"end of the program: {current_time}")
    print(f"end of the program: {current_time}")