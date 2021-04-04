def is_pangram(sentence):
    s = 'abcdefghijklmnopqrstuvwxyz'
    return set(sentence.lower()) >= set(s)