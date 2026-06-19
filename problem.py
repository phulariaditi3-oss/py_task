power = int(input("Enter power: "))

if power >= 80:
    print("Dragon allows entry")
else:
    print("Dragon rejects you")


    score = int(input("Enter score: "))

if score >= 1000:
    print("Pro Gamer")
elif score >= 500:
    print("Intermediate Gamer")
else:
    print("Beginner Gamer")

age = int(input("Enter age: "))
fitness = input("Fit? (yes/no): ")

if age >= 18:
    if fitness == "yes":
        print("Mission Accepted")
    else:
        print("Fitness Test Failed")
else:
    print("Too Young")


key = input("Do you have key? (yes/no): ")
password = input("Enter password: ")

if key == "yes":
    if password == "magic123":
        print("Castle Opened")
    else:
        print("Wrong Password")
else:
    print("No Key")


fuel = int(input("Enter fuel percentage: "))
weather = input("Weather good? (yes/no): ")

if fuel >= 70:
    if weather == "yes":
        print("Launch Successful")
    else:
        print("Launch Delayed Due To Weather")
else:
    print("Not Enough Fuel")