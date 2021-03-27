def lassoLetter(letter, shiftAmount):
    aAscii = ord('a')
    alphabetSize = 26
    letterCode = ord(letter.lower())
    trueLetterCode = aAscii + \
        (((letterCode - aAscii) + shiftAmount) % alphabetSize)
    decodedLetter = chr(trueLetterCode)
    return decodedLetter


def lassoWord(word, shiftAmount):
    decodedWord = ""
    for letter in word:
        decodedLetter = lassoLetter(letter, shiftAmount)
        decodedWord = decodedWord + decodedLetter
    return decodedWord


print('Ncevy\t+13:\t' + lassoWord('Ncevy', 13))
print('gpvsui\t+25:\t' + lassoWord('gpvsui', 25))
print('ugflgkg\t-18:\t' + lassoWord('ugflgkg', -18))
print('wjmmf\t-1:\t' + lassoWord('wjmmf', -1))