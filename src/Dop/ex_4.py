
import random

name = ""  # Example name, empty for testing

question = "Will I win the lottery?"  # Example question

answer = ""

random_number = random.randint(1, 12)

if random_number == 1:
    answer = "Yes, definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
elif random_number == 10:
    answer = "Signs point to yes." 
elif random_number == 11:
    answer = "Cannot predict now."
elif random_number == 12:
    answer = "Concentrate and ask again."
else:
    answer = "Error."

if name == "":
    if question == "":
        print("You need to ask a question to get an answer from the Magic 8-Ball!")
    else:
        print(f"Question: {question}")
else:
    if question == "":
        print(f"{name} asks nothing, so the Magic 8-Ball remains silent.")
    else:
        print(f"{name} asks: {question}")

if question != "":
    print(f"Magic 8-Ball's answer: {answer}")
