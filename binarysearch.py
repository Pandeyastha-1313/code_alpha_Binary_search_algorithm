def binary_search(start, end):
    if start > end:
        print("Invalid range. The starting value must be less than or equal to the ending value.")
        return

    # Initialize variables
    current = start
    result = []

    while current <= end:
        result.append(current)
        current += 2

    return result

def display_index(series, number):
    try:
        index = series.index(number)
        print(f"The index of {number} in the series is: {index}")
    except ValueError:
        print(f"{number} is not in the series.")

# Get user input for the range
start_range = int(input("Enter the starting value: "))
end_range = int(input("Enter the ending value: "))

# Perform binary search and display the result
result_list = binary_search(start_range, end_range)

if result_list:
    print(f"Resulting range with a difference of two: {result_list}")

    # Get user input for the desired number
    desired_number = int(input("Enter the number to find in the series: "))
    display_index(result_list, desired_number)
else:
    print("No valid range to display.")
