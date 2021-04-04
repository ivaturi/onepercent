def steps(n):
    if n <= 0 or not isinstance(n, int):
        raise ValueError("Input must be a strictly positive integer")
    return 0 if n==1 else steps(3*n + 1 if n%2 else int(n/2)) + 1
