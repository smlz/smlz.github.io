
done = False

worklist =  ['zähne putzen', 'zimmer lüften', 'frühstücken', 'schulzeug richten']

while not done:
    if len(worklist) == 0 :
        done = True
    else:
        task = worklist.pop()
        print("Mache:", task)
