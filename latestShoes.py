import os 
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver = "/Users/devinsuttles/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
url = raw_input("Enter URL:")
driver.maximize_window()
driver.get(url)
wait = WebDriverWait(driver,10)

#refreshes the page if it's not ressponding
driver.set_page_load_timeout(30)

#opening size dropdown
size_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".exp-pdp-size-and-quantity-container a.exp-pdp-size-dropdown")))
actions = ActionChains(driver)
actions.move_to_element(size_button).click().perform()

# selecting size
size = wait.until(EC.visibility_of_element_located((By.XPATH, "//li[contains(@class, 'nsg-form--drop-down--option') and normalize-space(.) = '9.5']")))
actions = ActionChains(driver)
actions.move_to_element(size).click().perform()

#add to cart
driver.find_element_by_id("buyingtools-add-to-cart-button").click()        


