from seleniumwire import webdriver
#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from confirmation import extract_confirmation_code

def register_instagram(full_name, username, password, email, birthdate):
	proxy_url = f'http://dtgtsbnu:lmivadwkqvqt@185.199.228.220:7300'

	options = {
		'verify_ssl': True,
    }
	driver = webdriver.Chrome(seleniumwire_options=options)
	#driver = webdriver.Chrome()

	try:
		driver.get("https://www.instagram.com/accounts/emailsignup/")
		WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Allow all cookies']"))
		)
		accept_cookies = driver.find_elements(By.TAG_NAME, "button")
		for el in accept_cookies:
			if "Allow all cookies" in el.text:
				el.click()
		time.sleep(2)
		WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((By.NAME, "emailOrPhone"))
		)
		email_input = driver.find_element(By.NAME, "emailOrPhone")
		full_name_input = driver.find_element(By.NAME, "fullName")
		username_input = driver.find_element(By.NAME, "username")
		password_input = driver.find_element(By.NAME, "password")

		email_input.send_keys(email)		
		full_name_input.send_keys(full_name)
		username_input.send_keys(username)
		password_input.send_keys(password)

		time.sleep(2)		
		WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((By.XPATH, "//button[text()='Next']"))
		)
		next_button_birthday = driver.find_element(By.XPATH, "//button[text()='Next']")
		next_button_birthday.click()		

		birthdate_values = birthdate.split("/")
		WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//select[@title='Month:']"))
		)
		month_dropdown = Select(driver.find_element(By.XPATH, "//select[@title='Month:']"))
		day_input = Select(driver.find_element(By.XPATH, "//select[@title='Day:']"))
		year_input = Select(driver.find_element(By.XPATH, "//select[@title='Year:']"))	

		month_dropdown.select_by_value(birthdate_values[0])
		day_input.select_by_value(birthdate_values[1])
		year_input.select_by_value(birthdate_values[2])

		time.sleep(2)
		next_button_birthdate = driver.find_element(By.XPATH, "//button[text()='Next']")
		next_button_birthdate.click()		
		time.sleep(2)		

		time.sleep(2)
		confirmation_code = extract_confirmation_code(email)
		driver.switch_to.window(driver.window_handles[0])
		code_input = driver.find_element(By.NAME, "email_confirmation_code")		
		code_input.send_keys(confirmation_code)
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(2)
		WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Next']"))
		)
		next_button_final = driver.find_element(By.XPATH, "//div[text()='Next']")
		next_button_final.click()

	except Exception as e:
		print("An error occurred:", str(e))
	finally:
		print("Exiting the function")
	    #driver.quit()

register_instagram("Full Name", "Username", "Password", "Get_Temp_Mail_From_GmailNator_WithOnlyDomainOptionChecked", "12/6/1980")