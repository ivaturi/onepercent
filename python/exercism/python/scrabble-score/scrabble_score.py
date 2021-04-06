
def score(word):
    letter_scores = {'aeioulnrst' : 1, 'dg' : 2, 'bcmp' : 3, 'fhvwy' : 4, 'k' : 5, 'jx' : 8, 'qz' : 10}
    letter_score = lambda letter:sum(letter_scores[key] for key in letter_scores if letter in key)
    return sum(letter_score(letter) for letter in word.lower())
