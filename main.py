import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Setup the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Navigate to
    driver.get("https://code-maze.com/latest-posts-on-code-maze/")

    # Wait for the page to load
    time.sleep(3)

    # select h2 tags with class entry-title
    titles = driver.find_elements(By.CSS_SELECTOR, "h2.entry-title")

    # get the href value of the first <a> element in the <h2> element
    for title in titles:
        #print the text of the a element
        print(title.find_element(By.CSS_SELECTOR, "a").text)
        #print the href value of the a element
        print(title.find_element(By.CSS_SELECTOR, "a").get_attribute("href"))


    #wait 2 seconds
    time.sleep(2)



finally:
    # Close the browser after a short delay to see the result
    time.sleep(5)
    driver.quit()