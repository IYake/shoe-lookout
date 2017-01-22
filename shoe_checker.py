# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 13:35:10 2017

@author: Ian
"""

import requests, bs4

correctShoe = "Nike SB Zoom Stefan Janoski Premium High Tape"

def updateShoe():
    shoe = ""
    res = requests.get('http://store.nike.com/us/en_us/pw/new-mens-shoes/meZ7puZoi3?sortOrder=publishdate|desc')
    res.raise_for_status()
    nikeSoup = bs4.BeautifulSoup(res.text, "lxml")

    products = nikeSoup.select('.product-display-name')
    shoe = products[0].text

    return str(shoe) #shoe datatype is default as unicode
    
