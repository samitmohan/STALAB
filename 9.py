from selenium import webdriver
from selenium.webdriver.common.by import By
with webdriver.Chrome() as driver:
    print("Launching chrome")
    driver.get("http://demo.guru99.com/test/newtours/")
    driver.find_element(By.NAME, "userName").send_keys("userName")
    driver.find_element(By.NAME, "password").send_keys("password")
    driver.execute_script("document.getElementsByName('submit')[0].click();")
    print(driver.title)
    print("All test cases passed" if driver.title == "Login: Mercury Tours" else "Login Failed")
print("Closed chrome")
