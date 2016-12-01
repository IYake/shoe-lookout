import requests, bs4
import os 
from selenium import webdriver

chromedriver = "/Users/devinsuttles/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
url = raw_input("Enter URL:")

driver.get(url)
driver.set_page_load_timeout(25)
driver.implicitly_wait(20)

#Need to figure out how to click on this add to cart button as the last step 
<button id="buyingtools-add-to-cart-button" type="submit" class="js-add-to-cart add-to-cart nsg-button nsg-grad--nike-orange">
ADD TO CART </button>
driver.find_element_by_xpath('//*[contains(text(),"ADD TO CART")]').click()          


res = requests.get('http://store.nike.com/us/en_us/pw/new-mens-shoes/meZ7puZoi3?sortOrder=publishdate|desc')
res.raise_for_status()
nikeSoup = bs4.BeautifulSoup(res.text)


products = nikeSoup.select('.product-name')
print products[0].text
