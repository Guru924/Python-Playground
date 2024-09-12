# Question: Who invented the telephone? Answer: Alexander Graham Bell.

# Question: What is the capital city of Australia? Answer: Canberra.

# Question: Who painted the Mona Lisa? Answer: Leonardo da Vinci.

# Question: Which planet is known as the Red Planet? Answer: Mars.

# Question: Who wrote the play "Romeo and Juliet"? Answer: William Shakespeare.

# Question: What is the largest organ in the human body? Answer: The skin.

# Question: What is the longest river in the world? Answer: The Nile River.

# Question: Which country is known as the Land of the Rising Sun? Answer: Japan.

# Question: Who was the first President of the United States? Answer: George Washington.

# Question: What is the chemical symbol for water? Answer: H2O.


questions = ["Who invented the telephone?", "What is the capital city of Australia?", "Who painted the Mona Lisa?", "Which planet is known as the Red Planet?", "Who wrote the play \"Romeo and Juliet\"?", "What is the largest organ in the human body?", "What is the longest river in the world?", "Which country is known as the Land of the Rising Sun?", "Who was the first President of the United States?", "What is the chemical symbol for water?"]

ans = ["Alexander Graham Bell", "Canberra", "Leonardo da Vinci", "Mars", 'William Shakespeare', 'The skin', 'The Nile River', 'Japan', 'George Washington', 'H2O']


price = [1000, 5000, 10000, 20000, 50000, 100000, 150000, 300000, 500000, 1000000]

def KBC ():
    won = 0
    i = 0
    print("Welcome to this Game of KBC...")
    while i < len(questions):
        # if i%2 == 0:
        #     pass
        # else:
        print(str(i+1)+ ".", "Question for you"+ "\tPrice:", price[i])
        print(questions[i])
        res = input("Enter your answer: ")
        if res.lower().rstrip() == ans[i].lower():
            print("Right answer! You Won: ",price[i])
        else:
            print("Wrong answer! Better Luck Next Time")
            break
        i = i+1
    if i == len(questions):
        print("Congo! You Won Price of total:",price[i-1], "in KBC")

KBC()