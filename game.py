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
        ]

main()
