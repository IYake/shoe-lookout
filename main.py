import cart, shoeNotification, shoe_checker as SC

correctShoe = "Nike SB Zoom".lower()

count = 1
shoesMatch = False
latestShoe = SC.updateShoe().lower()

while (not shoesMatch):
    print "checking " + str(count)
    
    if SC.isWordInString(correctShoe, latestShoe, 0, 0):
        shoesMatch = True
    else:
        count += 1
        
    if count == 72000: #stop checking if between 10 and 20 hours
        shoesMatch = True
              
    latestShoe = SC.updateShoe().lower()
        
cart.checkout()

shoeNotification.notify('iangyake@gmail.com')
