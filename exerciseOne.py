from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

# Use chrome as a testing browser
driver = webdriver.Chrome()
driver.maximize_window()

# Define the web page
driver.get("https://landing.simetrik.com/esp")  

# Time to wait for the page to load 
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Look for "a" tags elements
links = driver.find_elements(By.TAG_NAME, "a")

# Validate each elements in links array
for link in links:
    url = link.get_attribute("href")
    if url:
        response = requests.head(url)
        if response.status_code >= 400:
            print("Broken link:", url)

# Close the browser
driver.quit()