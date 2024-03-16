# Problem 1
def dp_make_weight(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # Base case: If target_weight is 0, no eggs needed
    if target_weight == 0:
        return 0

    # Base case: If no egg weights available or target weight is negative, return infinity
    if not egg_weights or target_weight < 0:
        return float('inf')

    # If memoization contains result, return it
    if (egg_weights, target_weight) in memo:
        return memo[(egg_weights, target_weight)]

    # Recursive case: Choose the minimum between using the first egg weight or not using it
    use_egg = 1 + dp_make_weight(egg_weights, target_weight - egg_weights[0], memo)
    lose_egg = dp_make_weight(egg_weights[1:], target_weight, memo)
    result = min(use_egg, lose_egg)

    # Memoize the result
    memo[(egg_weights, target_weight)] = result
    return result

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Test Case 1:")
    print("Egg weights:", egg_weights)
    print("n =", n)
    print("Expected output: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    # New test case
    egg_weights_new = (1, 3, 4)
    n_new = 6
    print("Test Case 2:")
    print("Egg weights:", egg_weights_new)
    print("n =", n_new)
    print("Expected output: 2 (2 * 3 = 6)")
    print("Actual output:", dp_make_weight(egg_weights_new, n_new))
    print()
