numbers = [5, 15, 25, 35, 45, 15, 55, 65, 75, 85,
           15, 95, 105, 115, 125, 135, 145, 155, 165]

# Function 1: Sum
def sum_numbers(numbers):
    return sum(numbers)


# Function 2: Average / Mean
def average(numbers):
    return sum(numbers) / len(numbers)


# Function 3: Median
def median(numbers):
    numbers.sort()
    middle = len(numbers) // 2
    return numbers[middle]


# Function 4: Mode
def mode(numbers):
    return max(numbers, key=numbers.count)


# Display results
print("Numbers:", numbers)
print("Sum:", sum_numbers(numbers))
print("Average:", average(numbers))
print("Median:", median(numbers))
print("Mode:", mode(numbers))