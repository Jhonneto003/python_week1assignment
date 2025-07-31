# Create a program that asks for the user’s name and favorite color, 
# then prints a personalized greeting like: 
# “Hello, [Name]! Your favorite color, [Color], is awesome!”

# def personalized_greeting():
#     # Step 1: Ask the user for their name
#     name = input("What is your name? ")

#     # Step 2: Ask the user for their favorite color
#     color = input("What is your favorite color? ")

#     # Step 3: Print a personalized greeting
#     print(f"Hello, {name}! Your favorite color, {color}, is awesome!")


# personalized_greeting()

# simple quiz program
def simple_quiz():
    while True:
        score = 0
        correct = 0 

    # Create a multiple-choice quiz with questions about Python,
    #  movies, or any fun topic! 
    # Display scores at the end and allow the user to play again. 🏆
    
    

        print("Hello, Welcome to Pythonnaire")
        print("Answer the followng questions on pytion to win 1 million naira.\n There are five questions shown . Per question answered,you get the reward of 200,000 naira. \n Goodluck!!!!!!")

        num_1 = input("Who created Python? (a)Charles Babbage (b) Guido van Rossum ANS= " )
        num_2 = input("What is the output of this code? print(2 ** 3) (a)8  (b)6  ANS= ")
        num_3 = input("which keyword is used to define a function in Python? (a)function (b)def  ANS= ")
        num_4 = input("What will this print? print(type('10')) (a)<class 'float'> (b)<class 'int'> ANS= ")
        num_5 = input("What is the correct file extension for python file? (a).pyth  (b).py  ANS= ")

        if num_1.lower() == 'b':
            score += 200000
            correct += 1
    
        if num_2.lower() == 'a':
            score += 200000
            correct += 1

        if num_3.lower() == 'b':
            score += 200000
            correct += 1

        if num_4.lower() == 'b':
            score += 200000
            correct += 1

        if num_5.lower() == 'b':
            score += 200000
            correct += 1
            
        print (f"\n Congratulations! You got {correct} out of 5.")
        print(f"Therefore, your score is {score} naira")

        play_again = input("Do you want to try again? ")
        if play_again.lower() =="no":
            print("Thank you for playing! \n  ")
            break


simple_quiz()


# Build a program that stores a list of jokes and randomly selects one to display every time the user runs it. 
# Add a fun twist with jokes about Python or programming! 🐍💡

def random_joke():
    import random

    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why do Python programmers prefer snakes? Because they can handle exceptions! 🐍",
        "Why did the programmer quit his job? Because he didn't get arrays! 😂",
        "How do you comfort a JavaScript bug? You console it! 🖥️",
        "Why was the computer cold? It left its Windows open! ❄️"
    ]

    selected_joke = random.choice(jokes)
    print(f"Here's a joke for you: {selected_joke}")


        







