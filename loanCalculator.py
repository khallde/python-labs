# Prompting user input.
# Remember that the interest rate is a percentage.
loanAmount = float(input("Enter the cost of the loan: "))
interestRate = float(input("Enter the interest rate: "))
numberOfYears = int(input("Enter the number of years for the loan: "))

# How do I get this to display only two decimal points?
monthlyPayment = loanAmount * (interestRate * (1 + interestRate) * numberOfYears) / ((1 + interestRate) * numberOfYears - 1)

print("Your loan payment is ${0:.2f} a month for {1:d} years.".format(monthlyPayment, numberOfYears))
