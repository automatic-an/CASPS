import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from random import choices, randint
from time import sleep


#  ---------- EDIT ----------
gma = 'gmail\n' # replace email
pas = 'account pas\n' # replace password
saying = "#reddit #shorts"
hashtags = "#reddit #shorts #stories #story #redditstories #askreddit #redditmemes #FYP #foryou #foryoupage #viral"
#  ---------- EDIT ----------

f = open("title.txt", "r")
title = f.read()
if title == 'TLDR' or title == "" or title == " ":
    title = saying

email = gma+'\n' # replace email
password = pas+'\n' # replace password

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 45)
url = "https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
driver.get(url)
rand_time = randint(4,8)
sleep(rand_time)

#driver.find_element_by_name("identifier").send_keys(email)
#driver.find_element_by_name("password").send_keys(password)
wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(password)

wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "style-scope ytd-topbar-menu-button-renderer"))).click()
#driver.find_element_by_class_name("style-scope ytd-topbar-menu-button-renderer").click()
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "style-scope ytd-compact-link-renderer"))).click()
#driver.find_element_by_class_name("style-scope ytd-compact-link-renderer").click()
#driver.find_element_by_name("Filedata").send_keys("C:/Users/tsul/Desktop/automate/contentBot/assets/final_video.mp4")
wait.until(EC.presence_of_element_located((By.NAME, "Filedata"))).send_keys("C:/Users/tsul/Desktop/automate/contentBot/assets/final_video.mp4")
rand_time = randint(6,12)
sleep(rand_time)
wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"))).send_keys(title)
#wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"))).send_keys('Redditors telling some "REAL LIFE" advice and experiences. #shorts')
wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"))).send_keys(hashtags)
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]"))).click()
next_button = "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]"
wait.until(EC.element_to_be_clickable((By.XPATH, next_button))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, next_button))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, next_button))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[2]"))).click()
rand_time = randint(49,71)
sleep(200)
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]"))).click()
rand_time = randint(8,13)
sleep(rand_time)