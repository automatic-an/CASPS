import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from random import choices, randint
from time import sleep


tik_nam = 'gamerbedrock1'
tik_pas = 'mihiHI36*'
video_title = "hi"

# chromedriver = r"C:/SeleniumDrivers/chromedriver.exe"
# brave = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
# option = uc.ChromeOptions()
# option.binary_location = brave
# driver = uc.Chrome(driver_executable_path=chromedriver, options=option)
# driver.get(url)

#driver = uc.Chrome(browser_executable_path="C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe",use_subprocess=True)
driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 45)
#driver.refresh()
#driver.maximize_window()
#driver.switch_to.default_content()
#driver.set_window_size(1024, 768)


driver.get("https://www.tiktok.com/")
driver.options.add_argument("window-size=1200x600")

sleep(randint(6,13))
print("numer 1")
iframe = driver.find_elements(By.TAG_NAME, "iframe")
print(iframe)
sleep(randint(1,3))
driver.find_element(by='xpath', value='//button[@data-e2e="top-login-button"]').click()
sleep(randint(1,3))
wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"Use phone / email / username")]'))).click()
sleep(randint(1,3))
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Log in with email or username")]'))).click()
sleep(randint(1,3))
wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="username"]'))).click()
sleep(randint(1,3))
wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="username"]'))).send_keys(tik_nam)
sleep(randint(1,3))
wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).click()
sleep(randint(1,3))
wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Password"]'))).send_keys(tik_pas)
sleep(randint(1,3))
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-e2e="login-button"]'))).click()
sleep(randint(5,11))
# srtHandle = driver.window_handles
# print(srtHandle)
# driver.switch_to.window(srtHandle[0])
wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-e2e="upload-icon"]'))).click()
print("hi")
sleep(randint(7,13))
#iframe = driver.find_element(By.XPATH, '//iframe[@src="https://www.tiktok.com/creator#/upload?lang=en"]')
srtHandle = driver.window_handles
print(srtHandle)
driver.switch_to.window(srtHandle[0])
print("numer 2")
iframe2 = driver.find_elements(By.TAG_NAME, "iframe")
print(iframe2[0])
wait.until(EC.frame_to_be_available_and_switch_to_it((iframe2[0])))
#driver.switch_to.frame(iframe2[0])
#driver.switch_to.parent_frame()
#driver.switch_to.default_content()
sleep(randint(7,13))

wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/input'))).send_keys("C:/Users/tsul/Desktop/automate/contentBot/assets/final_video.mp4")
sleep(randint(4,9))
#wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div'))).click()
#sleep(randint(1,3))
#wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/input'))).send_keys(Keys.BACKSPACE*14)
sleep(randint(1,3))
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/input'))).send_keys(video_title)
sleep(randint(16,24))
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[6]/div[2]'))).click()
sleep(randint(65,89))
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[8]/div[2]/button'))).click()

