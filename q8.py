from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as driver:
    print("Launching Chrome")
    driver.get("http://demo.guru99.com/test/newtours/")
    driver.implicitly_wait(10)
    print("Waited for 10 seconds")
    driver.find_element(By.NAME, "userName").send_keys("userName")
    driver.find_element(By.NAME, "password").send_keys("password")
    print("Waiting")
    driver.find_element(By.NAME, "userName").submit()
    print("Waiting over")
    print("Check")
    print(driver.title)
    print("All Test Cases pass")
    assert "Welcome: Mercury Tours" in driver.title
