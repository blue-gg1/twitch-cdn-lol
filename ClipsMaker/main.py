import requests
from libs.secrets import main_cookies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://example.com/some404page")
# driver.add_cookie({
#     "name": "key", 
#     "value": "value"})

driver.add_cookie(main_cookies)

assert "Twitch" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()