def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands are of unequal length!")
    return sum([a is not b for a,b in zip(strand_a, strand_b)])