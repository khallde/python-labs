nameList = []
name = ""

while name != "Stop":
    name = input("Enter names. Enter Stop to stop. ").capitalize()
    nameList.append(name)

nameList.remove("Stop")
nameList.sort()

print(nameList)