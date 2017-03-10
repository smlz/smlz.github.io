def isPalindrome(word):
    for index in range(len(word) // 2):
        if word[index] != word[-index-1]:
            return False
    return True

def isPalindromRekursiv(word):
    if len(word) <= 1: # simple Fälle
        return True
    else:
        if word[0] != word[-1]:
            return False
        else:
            return word[1:-1]   istDasInnereEinPalindrome???

woerter = [] #'asna Anna kurt wasitacatisaw level'.split()
for word in woerter:
    if isPalindrome(word):
        print('"{}" ist ein Palindrom'.format(word))
    else:
        print('"{}" ist KEIN Palindrom'.format(word))

word = input("Gib ein Satz ein: ")
word = word.lower().replace(' ', '')  # Sanitize input
print(isPalindrome(word))
