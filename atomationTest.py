import pyautogui
from selenium import webdriver


driver = webdriver.Chrome()

driver.get('https://www.twitch.tv/')


searchbox = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/nav/div/div[2]/div/div/div/div/div[1]/div/div/div/input')
searchbox.send_keys("xqc")

searchButton = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/nav/div/div[2]/div/div/div/div/div[1]/div/div/div/input')
searchButton.click()
pyautogui.press('enter')
