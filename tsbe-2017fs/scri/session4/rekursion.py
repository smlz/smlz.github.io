import inspect

def ist_ein_palindrom(wort):
    if len(wort) <= 1:
        for fi in reversed(inspect.stack()):
            print(f"File {fi.filename}:{fi.lineno}, in {fi.function}()")
            for key, val in fi.frame.f_locals.items():
                if val is not fi:
                    print(f"\t{key} = \t{val}")
        return True
    if wort[0] != wort[-1]:
        return False
    else:
        return ist_ein_palindrom(wort[1:-1])

wort = 'regallager'
resultat = ist_ein_palindrom(wort)
print(f"{wort}: {resultat}")
