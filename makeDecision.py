weather = input("Is it currently raining? ")
if weather == "Yes":
    print("You should take the bus.")
else:
    distance = int(input("How far do you need to travel? "))
    if distance > 10:
        print("You should take the bus.")
    elif (2 <= distance <= 10):
        print("You should ride your bike.")
    elif distance < 2:
        print("You should walk.")