def common_letters(lst):
    common = set(lst[0])
    for word in lst[1:]:
        common = common.intersection(set(word))
    return sorted(list(common))

words = ["bella","label","roller"]
print(common_letters(words)) # ['e', 'l', 'l']
words = ["cool","lock","cook"]
print(common_letters(words)) # ['c', 'o']