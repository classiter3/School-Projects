#
# Student Name: Craig Lassiter
# Date: 9/14/2022
# Number Analysis Program
#
import random


def main():
    # List to store numbers
    number_list = []

    # The user must enter an odd number here.
    number_count = int(input('How many numbers? '))
    while number_count % 2 != 1:  # Check the number is NOT odd
        print('Please enter an odd number.')
        number_count = int(input('How many numbers? '))

    for i in range(number_count):
        # Generate a random number between 1-100 inclusive
        number = random.randint(1, 100)    # "Fill-this-in"
        print(f'Entry {i + 1}: {number}')
        # TODO: Fill this in
        number_list.append(number)  # Make a function call that will append number to number_list

    low = min(number_list)
    high = max(number_list)
    total = sum(number_list)
    average = total / len(number_list)

    # The median is the number that is directly in the middle of the
    # sorted list. Implement these three steps to get the median:
    number_list.append(number)
    median_index = (len(number_list) - 1) // 2  # This will get the middle index
    median = number  # TODO: Assign the element in number_list with the
                            # median_index to the variable median.

    print('--------------')
    print(f'Low: {low}')
    print(f'High: {high}')
    print(f'Total: {total:.2f}')
    print(f'Average: {average:.2f}')
    print(f'Median: {median}')


# Call the main function.
main()
