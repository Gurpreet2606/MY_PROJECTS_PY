print("===================================")
print("       WELCOME TO PYTHON KBC")
print("===================================")

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": 2,
        "prize": 1000
    },
    {
        "question": "Which language are we using?",
        "options": ["Java", "C++", "Python", "HTML"],
        "answer": 3,
        "prize": 2000
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": 2,
        "prize": 5000
    },
    {
        "question": "Which function gives index and value together?",
        "options": ["range()", "index()", "enumerate()", "items()"],
        "answer": 3,
        "prize": 10000
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": 2,
        "prize": 20000
    }
]

money = 0

for number, q in enumerate(questions, start=1):

    print("\nQuestion", number)
    print(q["question"])

    for option_number, option in enumerate(q["options"], start=1):
        print(option_number, ".", option)

    answer = int(input("Enter your answer (1-4): "))

    if answer == q["answer"]:
        money = q["prize"]
        print("✅ Correct!")
        print("You won ₹", money)

    else:
        print("❌ Wrong answer!")
        print("Game Over!")
        break

print("\n===================================")
print("        FINAL RESULT")
print("===================================")
print("You won ₹", money)
print("Thank you for playing!")
