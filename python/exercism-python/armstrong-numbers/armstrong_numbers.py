def is_armstrong_number(num):
    return num == sum(int(x) ** len(str(num)) for x in str(num))
