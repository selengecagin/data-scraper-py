import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Setup the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Navigate to Google Turkey
    driver.get("https://code-maze.com/")

    # Wait for the page to load
    time.sleep(3)

    # select h2 tags with class entry-title
    titles = driver.find_elements(By.CSS_SELECTOR, "h2.entry-title")






finally:
    # Close the browser after a short delay to see the result
    time.sleep(5)
    driver.quit()