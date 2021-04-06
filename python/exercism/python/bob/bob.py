def response(hi):
    s = hi.strip()
    moods = [
        (lambda s:s=='', "Fine. Be that way!"),
        (lambda s:s.isupper() and s.endswith("?"), "Calm down, I know what I'm doing!"),
        (lambda s:s.isupper(), "Whoa, chill out!"),
        (lambda s:s.endswith("?"), "Sure.")
    ]
    for mood in moods:
        if mood[0](s):
            return mood[1]
    return "Whatever."