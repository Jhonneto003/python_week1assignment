# Create an empty list called my_list.
# Append the following elements to my_list: 10, 20, 30, 40.
# Insert the value 15 at the second position in the list.
# Extend my_list with another list: [50, 60, 70].
# Remove the last element from my_list.
# Sort my_list in ascending order.
# Find and print the index of the value 30 in my_list.


# my_list= []
# my_list.append(10)
# my_list.append(20)
# my_list.append(30)
# my_list.append(40)
# my_list.insert(1, 15)
# my_list.extend([50,60,70])
# last_element= my_list[-1]
# my_list.remove(last_element)
# my_list.sort()
# print("Index of 30:", my_list.index(30))


# Create a function named calculate_discount(price, discount_percent) 
# that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price , discount_percent):
    discount_amount= discount_percent/100 * price
    final_price = price - discount_amount
    message = (
        f"Original price: ${price:.2f}\n"
        f"Discount: {discount_percent: .0f}%\n"
        f"Discount Amount: ${discount_amount: .2f}\n"
        f"Final Price: ${final_price:.2f}"
    )
    if discount_percent >= 20:
        return final_price, message
    
    else:
        return price, f"Discount not applied: {discount_percent} less than 20% threshold"


final_price, message=calculate_discount(50, 15)
print(message)





# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage.
#  Print the final price after applying the discount, or if no discount was applied, print the original price.

def calculate_discount(price , discount_percent):
    discount_amount= discount_percent/100 * price
    final_price = price - discount_amount
    message = (
        f"Original price: ${price:.2f}\n"
        f"Discount: {discount_percent: .0f}%\n"
        f"Discount Amount: ${discount_amount: .2f}\n"
        f"Final Price: ${final_price:.2f}"
    )
    if discount_percent >= 20:
        return final_price, message
    
    else:
        return price, f"Discount not applied: {disc"

price = int(input("Enter the original price of the item: "))
discount_percent = int(input('Enter the discount: '))
final_price, message=calculate_discount(price, discount_percent)
print(message)

