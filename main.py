# import  sleep from time
from selenium import webdriver
from time import sleep
# driver=webdriver.Chrome(executable_path=r"C:\Users\HomeUser\PycharmProjects\Selenium by sunil\Drivers\chromedriver.exe")
driver=webdriver.Chrome(executable_path="./Drivers/chromedriver.exe")
# driver.quit()
# driver=webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
# from selenium.webdriver import Chrome
# driver=Chrome()
driver.get("https://www.facebook.com")
title=driver.title
print(title)
# url=driver.url
# print(url)
src=driver.page_source
print(src)

