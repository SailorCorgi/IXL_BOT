# install the latest driver https://sites.google.com/chromium.org/driver/ and put it in c drive → program files x86
# install python 3 (duh)
# install selenium by doing pip install Selenium in cmd
# Path = where chromedriver located should be program files x86

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service())

#change to ixl url
driver.get("https://www.ixl.com/math/grade-7/find-the-number-of-outcomes-word-problems")
driver.implicitly_wait(30)
question = driver.find_element(By.CSS_SELECTOR, "main#practice-page-container section > section > div > div > div").get_attribute("textContent")
# go to second word on page and use extension to change url
# https://chrome.google.com/webstore/detail/copy-css-selector/kemkenbgbgodoglfkkejbdcpojnodnkg/related
print(question)
#new tab and switch
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(30)
driver.get("https://www.google.com/search?q=" + question + "&rlz=1C1CHBD_enUS916US917&oq=lol&aqs=chrome..69i57"
                                                           ".1824j0j7&sourceid=chrome&ie=UTF-8")
driver.implicitly_wait(2.5)
links = driver.find_elements(By.CLASS_NAME, 'r')  # I went on Google Search and found the container class for the link
driver.find_element(By.CSS_SELECTOR, "div#rso div > div > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e > ""div > a > h3").click()
#TODO auto save answers
#TODO Bypass Captcha


# NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE
# NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE


#TODO automation after starting scripts are finished