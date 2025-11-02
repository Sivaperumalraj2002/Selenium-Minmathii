import random

def generate_random_number_with_digits(digits):
    """
    Generates a random integer with the specified number of digits.
    Example: digits=4 → range 1000–9999
    """
    if digits <= 0:
        raise ValueError("Number of digits must be positive")

    lower = 10**(digits - 1)
    upper = (10**digits) - 1

    return random.randint(lower, upper)
# print(int("8"+str(generate_random_number_with_digits(9))))
print(generate_random_number_with_digits())