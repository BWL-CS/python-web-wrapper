def main():
    print("Starting a new Trivia game...")
    user_name = input("Enter your name: ")
    print(f"Welcome, {user_name}!")

    trivia = [
          { 'Welcome to the trivia. This is the first question.': "Who was the first president of the United States?",
            'answer': 'George Washington',
            'options': ['Abraham Lincoln', 'Thomas Jaefferson', 'Andrew Jackson', 'George Washington'],
          },
          { 'This is the second question.': "What year did World War 2 end?",
            'answer': '1945',
            'options': ['1865', '1940', '1947', '1945'],
          }
          { 'This is your third question.': "Which civilizations built the pyramids in Giza?",
            'answer': 'Ancient Egyptians',
            'options': ['Ancient Russians', 'Ancient Romans', 'Ancient Greeks', 'Ancient Egyptians'],
          },
          { 'This is the fourth question.': "Who was president famous for abolishing slavery?",
            'answer': 'Abraham Lincoln',
            'options': ['George Washington', 'Herbert Hoover', 'Theodore Roosevelt', 'Abraham Lincoln'],
          }
        ]

main()
