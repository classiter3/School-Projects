
#
# Craig Lassiter
# Aug 24, 2022
#
# Trish at Bargain Used Books has decided to add a discount program for her loyal customers and for customers that buy a lot.
# Here's how it works:
# If a customer is in her loyalty program and buy $100 or less, they get a 15% discount.
# If a customer is in her loyalty program AND they buy over $100, they get a 25% discount.
# If a customer is not in her loyalty program, but they buy over $100, they get a 5% discount.
#


discount = 0
# Ask the user to enter the total purchase amount. NOTE: This number could be a floating point number.
purAmount = float(input('Enter the total purchase amount: '))

# Ask the user if the customer is in the loyalty program
isLoyaltyProMem = input('Is the customer a loyalty program member (y/n): ')

# Calculate the total after discounts
if isLoyaltyProMem == "y" and purAmount <= 100:
    discount = .15
    print(f'Total after discount ${purAmount - (purAmount * discount):.2f}')

# Calculate the total after discounts
elif isLoyaltyProMem == "y" and purAmount >= 100:
    discount = .25
    print(f'Total after discount ${purAmount - (purAmount * discount):.2f}')

elif isLoyaltyProMem == "n" and purAmount >= 100:
    discount = .05
    print(f'Total after discount ${purAmount - (purAmount * discount):.2f}')

else:
    print('not eligible for discount')

# Calculate the total after discounts.
purchaseAfterDiscount = purAmount - (purAmount * discount)

# Calculate the amount of sales tax on the total.
salesTax = purchaseAfterDiscount * 0.06

# Calculate the total after discounts and tax.
afterTax = salesTax + purAmount - (purAmount * discount)

# Output the total after discounts, the sales tax, and the total after discounts and tax.
print(f'Sales Tax ${salesTax:.2f}')
print(f'Total after tax ${afterTax:.2f}')
