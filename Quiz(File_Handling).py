result = {"DSA":0,"DBMS":0,"Python":0}

# Register a new user directly into the file
def register(filename):
    print("\n--- Register ---")
    username = input("Enter a username: ")
    with open(filename, 'r') as file:
        for line in file:
            existing_username, _ = line.strip().split(':')
            if existing_username == username:
                print("Username already exists. Please choose a different one.")
                break
        else:
            password = input("Enter a password: ")
            with open(filename, 'a') as file:
                file.write(f"{username}:{password}\n")
            print("Registration successful!")

# Login an existing user by checking the file
def login(filename):
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open(filename, 'r') as file:
        for line in file:
            existing_username, existing_password = line.strip().split(':')
            if existing_username == username and existing_password == password:
                print("Login successful!")
                return username
        else:
            print("Invalid username or password.")
            return None

# Load quiz data from file
def load_quiz_data(filename):
    quizzes = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                topic = parts[0]
                question = {
                    "question": parts[1],
                    "options": parts[2:6],
                    "answer": parts[6]
                }
                if topic not in quizzes:
                    quizzes[topic] = []
                quizzes[topic].append(question)
    except FileNotFoundError:
        print("Quiz data file not found.")
    return quizzes

# Function to take a quiz
def attempt_quiz(quizzes, username):
    print("\n--- Choose a topic ---")
    topics = list(quizzes.keys())
    for i, topic in enumerate(topics, start=1):
        print(f"{i}) {topic}")
    
    choice = int(input("Enter the number of the topic you want to take: "))
    selected_topic = topics[choice - 1]

    print(f"\nStarting the quiz on {selected_topic}!")
    score = 0
    for i, question in enumerate(quizzes[selected_topic], start=1):
        print(f"\nQuestion {i}: {question['question']}")
        for option in question['options']:
            print(option)
        
        user_answer = input("Your answer (A/B/C/D): ").upper()
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}")

    print(f"\n{username}, your final score for the {selected_topic} quiz is {score} out of {len(quizzes[selected_topic])}")
    result[selected_topic] += score

# Main program loop
def main():
    users_db_filename = "users_db.txt"
    quiz_data_filename = "quiz_data.txt"

    # Load quiz data from the file
    quizzes = load_quiz_data(quiz_data_filename)

    while True:
        print("\n--- Quiz Application ---")
        print("1) Register")
        print("2) Login")
        print("3) Attempt Quiz")
        print("4) Show result")
        print("5) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register(users_db_filename)
        elif choice == '2':
            user = login(users_db_filename)
        elif choice =='3':
            if user:
                attempt_quiz(user)
        elif choice == '4':
            for key,value in result.items():
                print(f"{key}:{value}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
