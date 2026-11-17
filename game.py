def main():
    print("Starting a new Trivia game...")
    user_name = input("Enter your name: ")
    print(f"Welcome, {user_name}!")

    trivia = [
          { 'question': "Who was the first president of the United States?",
            'answer': 'George Washington',
            'options': ['Abraham Lincoln', 'Thomas Jefferson', 'Andrew Jackson', 'George Washington'],
          },
          { 'question': "What year did World War 2 end?",
            'answer': '1945',
            'options': ['1865', '1940', '1947', '1945'],
          },
          { 'question': "Which civilizations built the pyramids in Giza?",
            'answer': 'Ancient Egyptians',
            'options': ['Ancient Russians', 'Ancient Romans', 'Ancient Greeks', 'Ancient Egyptians'],
          },
          { 'question': "Who was president famous for abolishing slavery?",
            'answer': 'Abraham Lincoln',
            'options': ['George Washington', 'Herbert Hoover', 'Theodore Roosevelt', 'Abraham Lincoln'],
          },
          { 'question': "What year did the Titanic sink?",
            'answer': '1912',
            'options': ['1912', '1876', '1920', '2017'],
          },
          { 'question': "Which Greek city is known as the birthplace of Democracy?",
            'answer': 'Athens',
            'options': ['Athens', 'Patras', 'Larissa', 'Piraeus'],
          },
          { 'question': "Which year was the Declaration of Independence formally adopted?",
            'answer': '1776',
            'options': ['1775', '1776', '1823', '1618'],
          },
          { 'question': "What year did the Berlin Wall fall?",
            'answer': '1989',
            'options': ['1991', '1989', '2003', '2019'],
          },
          { 'question': "Which year did World War 1 start? ",
            'answer': '1914',
            'options': ['1917', '1991', '1914', '1910'],
          },
          { 'question': "What year did the Space Race start?",
            'answer': '1955',
            'options': ['1955', '1990', '1952', '1947'],
          }
    ]

    def ask_question(question, options, answer):
        print("\n" + question)

        letters = ["A", "B", "C", "D"]

        for i in range(len(options)):
          print(letters[i] + ". " + options[i])

        choice = input("Enter your answer. Choose A, B, C, or D.").strip().upper()

        while choice not in letters:
           print("That is incorrect. Please choose A, B, C, or D.")
           choice = input("Enter your answer: ").upper()

        selected_answer = options[letters.index(choice)]

        if selected_answer == answer:
          print("Correct answer")
          return True
        else:
           print("Incorrect answer")
           return False
        
    for i in range(len(trivia)):
      correct = ask_question(
        trivia[i]["question"],
        trivia[i]["options"],
        trivia[i]["answer"]
    )

    if correct == True:
       score += 1

    print(f"Your final score is {score}/{len(trivia)}")
       
main()
