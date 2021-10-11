from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user = "username"
password = "password"

driver = webdriver.Chrome(r"C:\Users\Basu Jindal\chromedriver.exe")
driver.set_page_load_timeout(10)

driver.get("https://netaccess.iitm.ac.in/account/login/")

elem = driver.find_element_by_id("username")
elem.send_keys(user)

elem = driver.find_element_by_id("password")
elem.send_keys(password)

elem1 = driver.find_element_by_name("submit")
elem1.send_keys(Keys.RETURN)

driver.get("https://netaccess.iitm.ac.in/account/approve")

day1 = driver.find_element_by_id("radios-1").click()

approve = driver.find_element_by_name("approveBtn").click()

driver.quit()
print('task completed')
