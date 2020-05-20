# Prompting user input
loanAmount = float(input("Enter the cost of the loan: "))
interestRate = float(input("Enter the interest rate: "))
numberOfYears = int(input("Enter the number of years for the loan: "))

# Calculating the monthly payment
monthlyPayment = loanAmount * (interestRate * (1 + interestRate) * numberOfYears) / ((1 + interestRate) * numberOfYears - 1)

# Printing a message to the user
print("Your loan payment is ${0:.2f} a month for {1:d} years.".format(monthlyPayment, numberOfYears))
