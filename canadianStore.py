numberCheck = False

while numberCheck == False:
    try:
        cartTotal = float(input("Enter your cart's total: "))
    except:
        print("It looks like you didn't enter a valid number.")
    else:
        numberCheck = True

userCountry = input("Enter your country: ").upper()

generalSalesTax = 0.05
harmonizedSalesTax = 0.13
provincialSalesTax = 0.06

if userCountry == "CANADA":
    userProvince = input("Enter your province: ").upper()
    if userProvince == "ALBERTA":
        cartTotal += generalSalesTax * cartTotal
    elif userProvince == "ONTARIO" or "NEW BRUNSWICK" or "NOVA SCOTIA":
        cartTotal += harmonizedSalesTax * cartTotal
    else:
        cartTotal += (provincialSalesTax * cartTotal) + (generalSalesTax * cartTotal)

print("Your total is ${0:.2f}.".format(cartTotal))
