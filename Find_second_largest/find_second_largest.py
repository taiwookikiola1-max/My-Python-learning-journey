def find_second_largest(numbers):
    # Initialize largest and second largest with smallest possible number
    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest  # previous largest becomes second largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest

# Test cases
numbers1 = [10, 45, 22, 45, 30]
print("Second largest:", find_second_largest(numbers1))  # Output: 30

numbers2 = [5, 5, 5, 2]
print("Second largest:", find_second_largest(numbers2))  # Output: 5

numbers3 = [100, 200, 300, 400]
print("Second largest:", find_second_largest(numbers3))  # Output: 300

numbers4 = [-10, -20, -5, -15]
print("Second largest:", find_second_largest(numbers4))  # Output: -10

