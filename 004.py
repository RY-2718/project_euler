def makePalindromicNumber(string):
    return int(string + string[::-1])

print(makePalindromicNumber("123"))
