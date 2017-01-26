"""
Created on Tue Oct 25 13:41:09 2016
@author: Devin Suttles
"""

import os 
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#creating the chrome driver 
chromedriver = "/Users/Ian/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)


def checkout():
	wait = WebDriverWait(driver,10)
	driver.set_page_load_timeout(15)
	try:
		driver.get("http://swoo.sh/2j8FWMT")
	except TimeoutException:
		driver.execute_script("window.stop();")

	driver.find_element_by_class_name('product-display-name').click()
#get size 
 	try: 
		size_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".exp-pdp-size-and-quantity-container a.exp-pdp-size-dropdown")))
	except TimeoutException:
		driver.execute_script("window.stop();")
		size_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".exp-pdp-size-and-quantity-container a.exp-pdp-size-dropdown")))
	actions = ActionChains(driver)
	actions.move_to_element(size_button).click().perform()
	
	size = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[contains(@class, 'nsg-form--drop-down--option') and normalize-space(.) = '9.5']")))
	actions = ActionChains(driver)
	actions.move_to_element(size).click().perform()
 
  	save = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".pdp-mylocker")))
	actions = ActionChains(driver)
	actions.move_to_element(save).click().perform()
 
	login = driver.find_element_by_name("emailAddress")
	actions = ActionChains(driver)
	actions.move_to_element(login).click().perform()
	login.clear()
	login.send_keys(file.username)
 
 	passw = driver.find_element_by_name("password")
	actions = ActionChains(driver)
	actions.move_to_element(passw).click().perform()
	passw.clear()
	passw.send_keys(file.password)
 
	login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".nike-unite-submit-button")))
	actions = ActionChains(driver)
	actions.move_to_element(login_button).click().perform()
