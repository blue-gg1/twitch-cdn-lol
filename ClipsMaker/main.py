import requests
from libs.secrets import api_token_cookie, auth_token_cookie,login_cookie,name_cookie
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://www.twitch.tv/videos/1978136480")
# driver.add_cookie({
#     "name": "key", 
#     "value": "value"})
driver.delete_all_cookies()

# driver.add_cookie(auth_token_cookie)

assert "Twitch" in driver.title
driver.add_cookie(api_token_cookie)
driver.add_cookie(auth_token_cookie)
driver.add_cookie(login_cookie)
driver.add_cookie(name_cookie)
# driver.close()