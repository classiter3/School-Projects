#
# Student Name: Craig Lassiter
# Date: 9/23/2022
# This problem will test your ability to use the Python module matplotlib. For
#

import matplotlib.pyplot as plt


def main():
    line_graph_title = str(input("Enter the line graph title: "))
    x_axis_label = str(input("Enter the label for the x-axis: "))
    y_axis_label = str(input("Enter the label for the y-axis: "))
    tick1_name = str(input("Enter the name for tick 1: "))
    tick1_value = float(input("Enter the value for tick 1: "))
    tick2_name = str(input("Enter the name for tick 2: "))
    tick2_value = float(input("Enter the value for tick 2: "))
    tick3_name = str(input("Enter the name for tick 3: "))
    tick3_value = float(input("Enter the value for tick 3: "))
    tick4_name = str(input("Enter the name for tick 4: "))
    tick4_value = float(input("Enter the value for tick 4: "))
    tick5_name = str(input("Enter the name for tick 5: "))
    tick5_value = float(input("Enter the value for tick 5: "))

    x_values = [1, 2, 3, 4, 5]  # Graphing 5 values across x-axis
    contributions = [tick1_value, tick2_value, tick3_value, tick4_value, tick5_value]

    days = [tick1_name, tick2_name, tick3_name, tick4_name, tick5_name]

    plt.plot(x_values, contributions, marker='o')
    plt.plot(x_values, contributions)

    # Add a title
    plt.title(line_graph_title)

    # Add labels for the axes
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)

    # Add the tick mark labels for x
    plt.xticks(x_values, days)

    # Add a grid.
    plt.grid(True)

    # Display the line graph
    plt.show()


main()
