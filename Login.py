import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import random
from selenium.webdriver.chrome.options import Options


# Configure ChromeOptions
options = Options()
options.add_argument("start-maximized")  # Start with a maximized window
options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass automation detection
options.add_argument("--disable-extensions")  # Disable extensions for better detection avoidance
options.add_argument("--disable-popup-blocking")  # Allow popups
options.add_argument("--incognito")  # Use incognito mode
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36")  # Mimic a regular user


s = Service("C:\\Windows\\WebDriver\\chromedriver.exe")
driver = webdriver.Chrome(service=s, options=options)
driver.maximize_window()
driver.get("https://suno.com/")

# Wait for the element to be visible
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[.//span[contains(text(), 'Sign In')]]"))
)
time.sleep(random.uniform(2, 5))
driver.find_element(By.XPATH, "//button[.//span[contains(text(), 'Sign In')]]").click()


google_button_xpath = "//button[.//img[@alt='Sign in with Google']]"
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, google_button_xpath))
).click()
time.sleep(random.uniform(2, 5))


checkbox_xpath = "//span[@class='cb-lb-t' and text()='Verify you are human']"
try:
    time.sleep(5)
    # Wait for the checkbox to be clickable and click it if found
    verifyHuman = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, checkbox_xpath))
    )
    verifyHuman.click()
    print("Human verification checkbox clicked.")
except TimeoutException:
    # If checkbox is not found within 10 seconds, move to next step
    print("Human verification checkbox not found, proceeding to next steps.")

time.sleep(random.uniform(2, 5))
print("Number of open windows:", len(driver.window_handles))


email_field_xpath = "//input[@type='email' and @id='identifierId']"
email = "<__YOUR_PASSWORD_HERE__>"  # Replace with your email
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, email_field_xpath))
).send_keys(email, Keys.RETURN)
time.sleep(5)

print("Current URL:", driver.current_url)
print("Page Source Snippet:", driver.page_source[:1000])
