# ----------------------
def trivia_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("=========")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1


    display_score(correct_guesses, guesses)

# ----------------------
def check_answer(answer, guess):
    if answer == guess
        print("CORRECT")
        return 1
    else:
        print("WRONG!")
        return 0



# ----------------------

def display_score(correct_guesses, guesses):
    print("=======")
    print("Results: ")
    print("=======")
    print("Answer: ", end="")


# ----------------------

def play_again():
    pass


questions = {
    "Who found the Turkey?: ": "Ataturk",
    "When the Turkey found?: ": 1923,
    "Who is the most famous celebrity: ": "Cem Yilmaz",
}

options = [["A. Ataturk", "B. Fatih Sultan Mehmet", "C. Alparslan", "D. Abdulhamit"],
           ["A. 1071", "B. 1923", "C. 1881", "D. 1829"],
            ["A. Haluk Bilginer", "B. Yilmaz Guney", "C. Cem Yilmaz", "D. Sertap Erener"],
           ]


trivia_game()
