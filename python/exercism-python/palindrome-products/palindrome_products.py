def largest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError("Max should be greater than min")
    return loop(min_factor, max_factor, False)

def smallest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError("Max should be greater than min")
    return loop(min_factor, max_factor)


def loop(factor1, factor2, ascending = True):
    r = (factor1**2, factor2**2) if ascending else (factor2**2, factor1**2, -1)
    for p in range(*r):
        if p == int(str(p)[::-1]):
            factors = [(i, p//i) for i in range(factor1, factor2) if not p%i and factor1 <= p//i <= factor2] 
            if factors:
                return p, factors
    return None,[]
    
