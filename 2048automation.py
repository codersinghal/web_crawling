import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Path to your Driver
browser = webdriver.Chrome('/home/harshit/Downloads/chromedriver_linux64/chromedriver')


browser.get("https://gabrielecirulli.github.io/2048/")

bodyElem = browser.find_element_by_tag_name("body")
gameOver=0
while gameOver==0:
	try:
		browser.find_element_by_class_name("game-over")
		gameOver=1
	except:
		bodyElem.send_keys(Keys.UP)
		bodyElem.send_keys(Keys.RIGHT)
		bodyElem.send_keys(Keys.DOWN)
		bodyElem.send_keys(Keys.LEFT)
