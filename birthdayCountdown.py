import datetime

# Converting user input into a date
birthday = input("Enter your birthday in mm/dd/yyyy format: ")
birthday = datetime.datetime.strptime(birthday, "%m/%d/%Y").date()

# Assigning today's date to a variable
todaysDate = datetime.date.today()

# Calculating the difference between today and the user's birthday
timeLeft = (todaysDate - birthday).days

print(f"You have {timeLeft} until your birthday!")
