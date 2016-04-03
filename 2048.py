# 2048 game by sending special keys

# These keys are present in selenium.webdriver.common.keys module

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://gabrielecirulli.github.io/2048/')

html_elem = browser.find_element_by_tag_name('body')

while True:

html_elem.send_keys(Keys.UP)
html_elem.send_keys(Keys.DOWN)
html_elem.send_keys(Keys.LEFT)
html_elem.send_keys(Keys.RIGHT)

