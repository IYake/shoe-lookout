import requests, bs4

res = requests.get('http://store.nike.com/us/en_us/pw/new-mens-shoes/meZ7puZoi3?sortOrder=publishdate|desc')
res.raise_for_status()
nikeSoup = bs4.BeautifulSoup(res.text)


products = nikeSoup.select('.product-name')
print products[0].text