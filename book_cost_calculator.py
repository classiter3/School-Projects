
#
# Craig Lassiter
# Aug 18, 2022
# This Python program that will help calculate what a customer should pay for books.
#

workBooks = 8.50
textBooks = 24.00
magazines = 5.95

num_workbooks = int(input('Enter number of Workbooks? '))
num_textbooks = int(input('Enter number of Textbooks? '))
num_magazines = int(input('Enter number of Magazines? '))

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

