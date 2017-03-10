def isPalindrome(word):
    if len(word) <= 1:
        return True

    if word[0] != word[-1]:
        return False
    innerWord = word[1:-1]
    result = isPalindrome(innerWord)
    return result

word = input("Ein Satz: ").lower().replace(' ', '')
print("isPalindrome: ", isPalindrome(word))
