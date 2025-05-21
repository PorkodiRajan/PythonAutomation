# test_open_example.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# Set up driver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


""" ChromeDriverManager().install()
Downloads the latest compatible ChromeDriver and returns its path.
Service(...)
Sets up a ChromeDriver service using that path.
webdriver.Chrome(...)
Launches a new Chrome browser window controlled by Selenium. """

# Test steps
driver.get("https://dev.vosynverse.com/auth?type=login")

time.sleep(3)
actual_title = driver.title
expected_title = "VosynVerse"

# Assert and print result
print("Actual Title:", actual_title)
if actual_title == expected_title:
    print("Result: Pass")
else:
    print("Result: Fail")

# Screenshot
driver.save_screenshot("session1.png")

# Close browser
driver.quit()