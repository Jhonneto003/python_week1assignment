#     Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.


def cal_num():
    num_1= input("Pick a number: ")
    num_2 = input("Pick a second number: ")
    sum_result = int(num_1) + int(num_2)

    print (f"{num_1} + {num_2} = {sum_result}")


cal_num()