import cart, shoeNotification, shoe_checker

#Check if shoes are correct
#Go to shoe product page
#Add shoe to Cart
#Notify
correctShoe = "Nike SB Zoom Stefan Janoski Premium High Tape"

count = 0
shoesMatch = False
latestShoe = shoe_checker.updateShoe()

while (not shoesMatch):
    print "checking " + str(count)
    ##Get the latest shoe and update latestShoe variable
    if (correctShoe == latestShoe):
        shoesMatch = True
    else:
        count += 1
        
    latestShoe = shoe_checker.updateShoe()
    
    #stop if between 10 and 20 hours
    if count == 72000:
        shoesMatch = True
        
cart.checkout()

shoeNotification.notify('iangyake@gmail.com')
