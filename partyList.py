nameList = []
name = ""
attemptCount = False

while name != "Stop":
    if attemptCount == False:
        name = input("Enter names. Enter Stop to stop. ").capitalize()
        attemptCount = True
    else:
        name = input("").capitalize()
    nameList.append(name)

nameList.remove("Stop")
nameList.sort()

print("The names entered were: ")

for listItem in nameList:
    print(listItem)