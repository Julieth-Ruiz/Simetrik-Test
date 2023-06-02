from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver 
driver = webdriver.Chrome()

# Define the web page
driver.get("https://landing.simetrik.com/esp")

# Find the header element li
header = driver.find_element(By.CSS_SELECTOR, "li")

# Get the header text
header_text = header.text

# Print header text
print(header_text)

# Close the browser
driver.quit()