from selenium import webdriver
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Navigate to Google
driver.get("https://www.google.com")

# Wait for 3 seconds to allow the page to load
time.sleep(3)

# Check the title
expected_title = "Google"
actual_title = driver.title

if actual_title == expected_title:
    print("Test Passed")
else:
    print("Test Failed")
    print("Expected:", expected_title)
    print("Actual:", actual_title)

# Close browser
driver.quit()
