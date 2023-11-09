from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import re
import time


def extract_confirmation_code(gmailnator_email):
    # Open Gmailnator inbox
    driver = webdriver.Chrome()
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(f"https://www.emailnator.com/inbox/#{gmailnator_email}")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Consent')]"))
    )
    consent_button = driver.find_element(By.XPATH, "//p[contains(text(), 'Consent')]")
    print(consent_button)
    consent_button.click()
    time.sleep(10);
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Reload')]"))
    )
    reload_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Reload')]")
    reload_button.click()
    time.sleep(5)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "td"))
    )

    tds = driver.find_elements(By.TAG_NAME, "td")
    for el in tds:
        if "is your Instagram code" in el.text:
            confirmation_code = re.search(r"\d{6}", el.text).group(0)

    print(confirmation_code)
    driver.quit()
    return confirmation_code
