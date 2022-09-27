

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service())

#change to ixl url of your choice 
driver.get("ixl url here")
driver.implicitly_wait(30)
question = driver.find_element(By.CSS_SELECTOR, "go to second word on page and use extension to copy css path and paste it here and delet this text").get_attribute("textContent")
# go to second word on page and use extension to copy css path and paste it 
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
