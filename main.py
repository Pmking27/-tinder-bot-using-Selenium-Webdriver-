import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

#THIS PROGRAM ONLY WORD ON IF OUR TINDER ACCOUNT IS LOGIN WITH YOUR FACKEBOOK ACCOUNT.
URL = "https://tinder.com/app/recs"
EMAIL_ID = "ENTER HERE YOUR FACEBOOK EMAIL FOR LOGIN TO TINDER"
PASSWORD = "ENTER HERE YOUR FACEBOOK PASSWORD FOR LOGIN TO TINDER"

#CHROME BROWSER DRIVER DOWNLOAD LINK:-https://chromedriver.chromium.org/
driver_path = Service('ENTER HERE YOUR chromedriver.exe PATH OR OTHER BROWSER DRIVER PATH')
driver = webdriver.Chrome(service=driver_path)
driver.maximize_window()

driver.get(URL)
time.sleep(5)

main_window = driver.current_window_handle

allow_cookies = driver.find_element(By.XPATH, '//*[@id="s1746966696"]/div/div[2]/div/div/div[1]/div[1]/button').click() #IF THIS XPATH IS NOT WORK THEN COPY AND PASTE YOUR XPATH

click_log_in = driver.find_element(By.LINK_TEXT, 'Log in').click()
time.sleep(3)
try:
    click_more_options = driver.find_element(By.XPATH, '//*[@id="s18585620"]/div/div/div[1]/div/div/div[3]/span/button').click() #IF THIS XPATH IS NOT WORK THEN COPY AND PASTE YOUR XPATH
except NoSuchElementException:
    pass
time.sleep(5)
try:
    log_in_facebook = driver.find_element(By.XPATH, '//*[@id="s18585620"]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click() #IF THIS XPATH IS NOT WORK THEN COPY AND PASTE YOUR XPATH

except NoSuchElementException:
    recovery_cancel = driver.find_element(By.XPATH, '//*[@id="s18585620"]/div/div/div[2]/button').click() #IF THIS XPATH IS NOT WORK THEN COPY AND PASTE YOUR XPATH
    time.sleep(2)
    click_log_in = driver.find_element(By.LINK_TEXT, 'Log in').click()
    time.sleep(2)
    log_in_facebook = driver.find_element(By.XPATH, '//*[@id="s18585620"]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click() #IF THIS XPATH IS NOT WORK THEN COPY AND PASTE YOUR XPATH

time.sleep(5)

for tab in driver.window_handles:
    if tab != main_window:
        driver.switch_to.window(tab)
        print(driver.title)
time.sleep(3)

add_email = driver.find_element(By.XPATH, '//*[@id="email"]')
add_email.send_keys(EMAIL_ID)
add_password = driver.find_element(By.XPATH, '//*[@id="pass"]')
add_password.send_keys(PASSWORD)
add_password.send_keys(Keys.ENTER)
time.sleep(20)

driver.switch_to.window(main_window)
time.sleep(2)

print(driver.title)
allow_location = driver.find_element(By.XPATH, '//*[@id="s18585620"]/div/div/div/div/div[3]/button[1]/span').click() #IF THIS XPATH IS NOT WORK THEN COPY AND PASTE YOUR XPATH
time.sleep(2)

disallow_notification = driver.find_element(By.XPATH, '//*[@id="s18585620"]/div/div/div/div/div[3]/button'
                                                      '[2]/span').click() #IF THIS XPATH IS NOT WORK THEN COPY AND PASTE YOUR XPATH
time.sleep(20)
click_dislike_button = driver.find_element(By.XPATH,'//*[@id="s1746966696"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button') #IF THIS XPATH IS NOT WORK THEN COPY AND PASTE YOUR XPATH


for i in range(20):
    try:
        time.sleep(3)
        click_dislike_button.click()

    except ElementClickInterceptedException:
        add_tinder_home_screen = driver.find_element(By.XPATH,'//*[@id="s18585620"]/div/div/div[2]/button[1]').click() #IF THIS XPATH IS NOT WORK THEN COPY AND PASTE YOUR XPATH

driver.quit()


# # create like button object
# click_like_button = driver.find_element(By.XPATH,
#                                         '//*[@id="s1746966696"]/div/div[1]/div/main/div[1]/div/div/div[1]'
#                                         '/div[1]/div/div[4]/div/div[4]/button') #IF THIS XPATH IS NOT WORK THEN COPY AND PASTE YOUR XPATH
# for i in range(20):
#     try:
#         # like a profile only if it is loaded
#         click_like_button.click()

#     except ElementClickInterceptedException:
#         try:
#             hide_its_a_match = driver.find_element(By.XPATH, '//*[@id="s1089923421"]/div/div/div[1]/div/div'
#                                                              '[4]/button').click() #IF THIS XPATH IS NOT WORK THEN COPY AND PASTE YOUR XPATH
#         except:
#             add_tinder_home_screen = driver.find_element(By.XPATH,
#                                                          '//*[@id="s18585620"]/div/div/div[2]/button[1]').click() #IF THIS XPATH IS NOT WORK THEN COPY AND PASTE YOUR XPATH

#         time.sleep(2)
#         click_like_button.click()

#     except NoSuchElementException:
#         time.sleep(3)
#         click_like_button.click()

#     time.sleep(7)