from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

path = "/Users/srishtik/Downloads/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_xpath('//*[@id="bigCookie"]')

start = time.time()
n = 1 
i = 1
while time.time() - start < 300:
    cookie.click()
    my_cookies = driver.find_element_by_css_selector("#cookies")

    products = driver.find_elements_by_css_selector(".storeSection .unlocked")
    pr = [ele.text for ele in products]
    l = len(pr) - 1

    if (time.time() - start) > n*i :
        driver.find_element_by_xpath('//*[@id="product'+f'{l}"]').click()
        i += 1




