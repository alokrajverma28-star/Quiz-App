# Quiz App

score = 0

print("Welcome to Quiz App!\n")

# Question 1
print("1. What is the capital of India?")
print("a) Mumbai")
print("b) Delhi")
print("c) Kolkata")
ans = input("Enter your answer: ")

if ans == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is Delhi\n")

# Question 2
print("2. Which language is used for web development?")
print("a) Python")
print("b) HTML")
print("c) C")
ans = input("Enter your answer: ")

if ans == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer is HTML\n")

# Final Score
print("Your score is:", score)
