from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

def execute_shortcut(shortcut):
    print(f"Executing..  :) {shortcut}...")

    # Start Chrome browser
    driver = webdriver.Chrome()

    # Open a new tab
    driver.execute_script("window.open();")

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])

    # Navigate to Google
    driver.get("https://www.google.com")

    # Wait for the page to load
    time.sleep(2)

    # Find the search bar
    search_bar = driver.find_element("name", "q")

    # Send the shortcut to the search bar with a bit of typing animation
    type_with_animation(search_bar, shortcut)

    # Press Enter to execute the shortcut
    search_bar.send_keys(Keys.ENTER)

    # Allow the browser to remain open
    input("Press Enter to close the browser...")

def type_with_animation(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # Add a random delay for a typing effect

# Example usage
print("Welcome to the Google Surfer!")
shortcut_description = input("Search Here: ")
execute_shortcut(shortcut_description)
