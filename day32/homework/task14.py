def vowel_count(sentence):
    count = 0
    vowels = "aeiouAEIOU"

    for char in sentence:
        if char in vowels:
            count += 1

    return count