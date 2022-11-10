#
# Student Name:Craig Lassiter
# Date: 9/4/2022
# This Python program will catch data entry errors that are made and give the user a chance to reenter the data.
# If the user enters a negative number, or goes above the maximum for a particular item
# The program should continue to ask the user to enter a number until it is valid.
#

workBooks = 8.50
textBooks = 24.00
magazines = 5.95

while True:
    num_workbooks = int(input('Enter number of Workbooks? '))
    if num_workbooks > 0 and num_workbooks < 40:
        break
    print("Number of workbooks must be between 0 and 40.")

while True:
    num_textbooks = int(input('Enter number of Textbooks? '))
    if num_textbooks > 0 and num_textbooks < 10:
        break
    print("Number of textbooks must be between 0 and 10.")

while True:
    num_magazines = int(input('Enter number of Magazines? '))
    if num_magazines > 0 and num_magazines < 25:
        break
    print("Number of magazines must be between 0 and 25.")

subtotal_wb = workBooks * num_workbooks
subtotal_tb = textBooks * num_textbooks
subtotal_mag = magazines * num_magazines

subtotal = subtotal_tb + subtotal_wb + subtotal_mag

salestax_wb = workBooks * num_workbooks * 0.06
salestax_tb = textBooks * num_textbooks * 0.06
salestax_mag = magazines * num_magazines * 0.06

salestax = salestax_tb + salestax_wb + salestax_mag

aftertax = subtotal + salestax

# Display before tax total.
print(f'Cost before tax {subtotal:.2f}')
print(f'Sales Tax {salestax:.2f}')
print(f'Cost after tax {aftertax:.2f}')
