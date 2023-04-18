from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver import Chrome

#ws to enter mobile number in redbus.com
driver = Chrome()
driver.get("https://www.redbus.in/")
driver.maximize_window()
driver.find_element("xpath", "//i[@id='i-icon-profile']").click()
# test comment
#test comment1
# driver.find_element("xpath", "//li[.='Sign In/Sign Up']").click()
# sleep(2)
# frm = driver.find_element("xpath", "(//iframe[contains(@src, '/login?offer')])[1]")
# driver.switch_to.frame(frm)
# driver.find_element("id", "mobileNoInp").send_keys("1234567896")