def two_fer(name = "you"):
    return "One for {}, one for me.".format(name if name else "Alice")