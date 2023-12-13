from selenium import webdriver
from selenium.webdriver.common.by import By
with webdriver.Chrome() as driver:
    driver.get("http://demo.guru99.com/test/newtours/")
    print("Number of links =", len(driver.find_elements(By.XPATH, "//a")))
