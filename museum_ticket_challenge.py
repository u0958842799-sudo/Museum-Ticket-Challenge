import winsound

tickets = 0
score = 0
lives = 3

print("Welcome to the Museum!")
print("Collect 3 tickets to open the main door.\n")

# -------------------------------
# Question 1
# -------------------------------

answer = input("1. What is the name of this ancient vase? (A, B, C): ")

if answer.upper() == "A":
    score += 1
    tickets += 1
    print("Correct!\n")
else:
    lives -= 1
    print("Wrong!\n")

# -------------------------------
# Question 2
# -------------------------------

answer = input("2. What does this sculpture represent? (A, B, C): ")

if answer.upper() == "A":
    score += 1
    tickets += 1
    print("Correct!\n")
else:
    lives -= 1
    print("Wrong!\n")

# -------------------------------
# Question 3
# -------------------------------

answer = input("3. What material did the ancient Greeks use? (A, B, C): ")

if answer.upper() == "A":
    score += 1
    tickets += 1
    print("Correct!\n")
else:
    lives -= 1
    print("Wrong!\n")

# -------------------------------
# Open Door
# -------------------------------

if tickets == 3:

    print("\nThe main door is OPEN!")

    # Repeat 3 times
    for i in range(3):
        winsound.Beep(1000, 300)

else:
    print("\nThe main door remains CLOSED.")

print("\nScore :", score)
print("Tickets:", tickets)
print("Lives :", lives)