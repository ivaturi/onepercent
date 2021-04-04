def classify(number):
    
    # Positive numbers only
    if number <= 0:
        raise ValueError("Number must be greater than zero")

    # find all factors
    all_factors = [factor for i in range(1, int(number ** 0.5) + 1) if not number % i for factor in (i, number // i)]
    
    # If 1 is a factor, all_factors also includes the number itself.
    overflow = sum(set(all_factors)) - 2 * number
    
    return "perfect" if overflow == 0 else "abundant" if overflow > 0 else "deficient"