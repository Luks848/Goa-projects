#codewars 1
#URL-https://www.codewars.com/kata/65128732b5aff40032a3d8f0/train/python
def neutralise(s1, s2):
    result = ""
    for a, b in zip(s1, s2):
        if a == b:
            result += a
        else:
            result += "0"
    return result
def neutralise(s1, s2):
    result = ""
    for a, b in zip(s1, s2):
        if a == b:
            result += a
        else:
            result += "0"
    return result