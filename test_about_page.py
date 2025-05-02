from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("http://54.162.154.10:80")
    time.sleep(1)

    driver.find_element(By.LINK_TEXT, "About").click()
    time.sleep(1)

    assert "About Us" in driver.page_source
    print("✅ Test Passed: 'About Us' text is visible.")

except Exception as e:
    print("❌ Test Failed:", e)

finally:
    driver.quit()

