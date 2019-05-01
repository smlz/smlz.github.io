

def gruppieren(text, anzahl):
    elemente = []

    for i in range(0, len(text), anzahl):
        elemente.append(text[i:i + anzahl])

    return elemente


assert(gruppieren("abcdefgh", 3) == ['abc', 'def', 'gh'])
