import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up Chrome WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Update the path to chromedriver if needed

# Navigate to the registration page
driver.get('http://localhost:5000/register')  # Update with your app's registration URL

# Fill in the registration form
username_field = driver.find_element(By.NAME, 'username')  # Adjust 'username' if needed
email_field = driver.find_element(By.NAME, 'email')  # Adjust 'email' if needed
password_field = driver.find_element(By.NAME, 'password')  # Adjust 'password' if needed
confirm_password_field = driver.find_element(By.NAME, 'confirm_password')  # Adjust if necessary

username_field.send_keys('testuser')
email_field.send_keys('testuser@example.com')
password_field.send_keys('TestPassword123')
confirm_password_field.send_keys('TestPassword123')

# Submit the form
submit_button = driver.find_element(By.NAME, 'submit')  # Adjust 'submit' if needed
submit_button.click()

# Wait for the registration to process
time.sleep(5)  # Wait for 5 seconds to ensure the page has time to load

# Verify the registration was successful (this example assumes a success message)
success_message = driver.find_element(By.CLASS_NAME, 'success')  # Adjust the selector if needed
assert 'Registration successful' in success_message.text

# Close the browser
driver.quit()
