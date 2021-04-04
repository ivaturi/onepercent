def find_anagrams(word, candidates):
    # check length
    return [candidate for candidate in candidates if word.lower() != candidate.lower() and sorted(word.lower()) == sorted(candidate.lower())]
