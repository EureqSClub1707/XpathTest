import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.google.ru/")
questens = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
questens.send_keys("python")
questens.submit()

time.sleep(4)
link = driver.find_elements_by_xpath(".//div[@class='rc']/div[@class='r']/a[@target='_blank']")
for F in link:
    print(F.get_attribute("href"))