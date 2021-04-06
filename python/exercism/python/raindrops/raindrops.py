def convert(number):
    factors = [(3, 'Pling'), (5, 'Plang'),(7, 'Plong')]
    sounds = [factor[1] for factor in factors if not number % factor[0]]
    return "".join(sounds) or str(number)
