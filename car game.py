command = ""
started = False
while True:
    command = input(">..").lower()
    if command == "start":
        if started:
            print("Car is already to started!")
        else:
            started = True
            print("Car Started...")
    elif command == "stop":
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start ...To start the car
stop ...To stop the car
quit ...To end the game
        """)
    elif command == "quit":
        break
    else:
        print("""
Sorry i don't understand
Type help
        """)


first_name = input("First Name: ")
last_name = input("Last Name: ")
year_of_birth = input("Birth Year: ")

print(last_name + first_name)
year_of_birth = input("Birth Year: ")


name = input("NAME> ")
name = name.upper()
if name == 'BEN':
    print('Hello Ben')
elif name == 'ANITA':
    print('Hello Anita')
else:
    print('Name not found!')

ylist = [1,2,3,4,5,6,7,8,9,10]
for number in mylist:
    if number % 2 == 0:
        print(number)
    else:
        print(f"{number} is an odd number")

listsum = 0
for number in mylist:
    listsum += number
print(listsum)