from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Configure Chrome options
chrome_options = ChromeOptions()

# Launch Chrome
chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_driver.get("https://www.google.com/?hl=es") 

# Close Chrome
chrome_driver.quit()

# Configure Firefox options
firefox_options = FirefoxOptions()

# Launch Firefox
firefox_driver = webdriver.Firefox(options=firefox_options)
firefox_driver.get("https://www.amazon.com/") 

# Close Firefox
firefox_driver.quit()