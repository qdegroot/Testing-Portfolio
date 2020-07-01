from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/")
    main_content = driver.find_element(By.ID, "content")
    for element in driver.find_elements(By.TAG_NAME, "a"):
        print(element.get_attribute("textContent"))


