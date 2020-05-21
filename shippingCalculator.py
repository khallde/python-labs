purchaseTotal = float(input("Enter your total: "))

if purchaseTotal < 50:
    purchaseTotal += 10
else:
    purchaseTotal += 0

print("Your total is ${0:.2f}.".format(purchaseTotal))
