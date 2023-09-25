# create a boolean variable


print("Hello! Welcome to this Quiz")
while True:
    while True:
        playing = input("Do You Want To Play? _  ")
        if playing.lower() == "yes" or "y":
            print("Okay! Let's Play :)")
            break
        elif playing.lower() == "no" or "n":
            print("Ok! Have a nice Day")
            quit()
        else:
            print("Invalid!  Type 'Yes' or 'No'")


    score = 0

    answer1 = input("What does CPU stands for? ")
    if answer1.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incurrect")

    answer1 = input("What does GPU stands for? ")
    if answer1.lower() == "graphics processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incurrect")

    answer1 = input("What does RAM stands for? ")
    if answer1.lower() == "read access memory":
        print("Correct!")
        score += 1
    else:
        print("Incurrect")

    answer1 = input("What does PSU stands for? ")
    if answer1.lower() == "power supply unit":
        print("Correct!")
        score += 1
    else:
        print("Incurrect")

    answer1 = input("What does ROM stands for? ")
    if answer1.lower() == "read only memory":
        print("Correct!")
        score += 1
    else:
        print("Incurrect")

    print(f"You got {str(score)} questions correct")
    print(f"You got {str(score * 20)}%")
    if score == 5:
        print("Excellent!")
    elif score >= 3:
        print("Good!")
    elif score == 2:
        print("Pass!")
    else:
        print("Failed! Try again")

