# Imports the system and name attributes from the os module
# to clear the screen before our final output prints
from os import system, name

nameList = []
personName = ""
attempt = False

while personName != "Stop":
    if attempt == False:
        print("Enter names. Enter Stop to stop. ")
        attempt = True
    else:
        personName = input("").capitalize()
        nameList.append(personName)

nameList.remove("Stop")
nameList.sort()

# Checks the operating system's name to determine
# which command is pushed to the system
if name == "nt":
    run = system("cls")
else:
    run = system("clear")

print("The names entered, in order, were: ")

for listItem in nameList:
    print(listItem)