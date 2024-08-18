import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Setup the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Open the JSONL file in append mode
    with open("titles.jsonl", "a") as f:
        for page in range(1, 21):  # Loop through the first 20 pages
            # Navigate to the page
            url = f"https://code-maze.com/latest-posts-on-code-maze/page/{page}/"
            driver.get(url)
            print(f"Navigating to: {url}")

            # Wait 2 seconds
            time.sleep(2)

            # Find <h2> elements with class "entry-title"
            titles = driver.find_elements(By.CSS_SELECTOR, "h2.entry-title")

            # Get the href value of the first <a> element in the <h2> element
            for title in titles:
                try:
                    # Print the text of the <a> element
                    title_text = title.find_element(By.CSS_SELECTOR, "a").text
                    print(title_text)

                    # Print the href attribute of the <a> element
                    title_link = title.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                    print(title_link)

                    # Save the data to a JSONL file
                    json_line = json.dumps({"title": title_text, "link": title_link})
                    f.write(json_line + "\n")
                except Exception as e:
                    print(f"Error processing title: {e}")


                # click the <a> tag with the link specified in the image using JavaScript to go to the next page
                try:
                    next_link = driver.find_element(By.CSS_SELECTOR, "div.nav-link.nav-link-prev > a")
                    driver.execute_script("arguments[0].click();", next_link)
                    print("Navigating to the next page")
                    time.sleep(2)
                except Exception as e:
                    print(f"Error navigating to the next page: {e}")
                    break

finally:
    # Close the browser after a short delay to see the result
    time.sleep(5)
    driver.quit()