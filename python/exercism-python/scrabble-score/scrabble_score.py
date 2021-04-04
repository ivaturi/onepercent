def score(word):
    def get_letter_score(letter):
        if letter in 'aeioulnrst':
            return 1
        elif letter in 'dg':
            return 2
        elif letter in 'bcmp':
            return 3
        elif letter in 'fhvwy':
            return 4
        elif letter == 'k':
            return 5
        elif letter in 'jx':
            return 8
        else:
            return 10
    return sum([get_letter_score(letter) for letter in word.lower()])

def score(word):
    letter_scores = {'aeioulnrst' : 1, 'dg' : 2, 'bcmp' : 3, 'fhvwy' : 4, 'k' : 5, 'jx' : 8, 'qz' : 10}
    letter_score = lambda letter:sum(letter_scores[key] for key in letter_scores if letter in key)
    return sum(letter_score(letter) for letter in word.lower())
