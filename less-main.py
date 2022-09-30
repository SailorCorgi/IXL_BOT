from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pyperclip

#made to be able to do the same thing as the other code but with less code so its faster
driver = webdriver.Chrome(service=Service())

#change to ixl url
driver.get("https://www.ixl.com/math/grade-8/absolute-value-and-opposite-integers")
driver.implicitly_wait(30)
question = driver.find_element(By.CSS_SELECTOR,"main#practice-page-container section > section > div > div > div").get_attribute("textContent")
# go to second word on page and use extension to change url
# https://chrome.google.com/webstore/detail/copy-css-selector/kemkenbgbgodoglfkkejbdcpojnodnkg/related
print(question)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(30)
driver.get("https://www.google.com/search?q=" + question + "&rlz=1C1CHBD_enUS916US917&oq=lol&aqs=chrome..69i57"
                                                           ".1824j0j7&sourceid=chrome&ie=UTF-8")
# now because the questions are easy the first result should have answer
# because of that we are going to factor out non numbers and copy paste it to ixl
# Printing
driver.implicitly_wait(30)
check_1 = driver.find_elements(By.CSS_SELECTOR, '#rso > div:nth-child(2) > div > block-component > div > div.dG2XIf.XzTjhb > div > div > div > div > div.ifM9O > div > div > div.yp1CPe.wDYxhc.NFQFxe.viOShc.LKPcQc > div > div:nth-child(2) > div')


for value in check_1:
    print(value.text)

#it finnaly fucking worked
#delay is two long