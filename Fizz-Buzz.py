
def tizz_buzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return 'tizzbuzz'
    if x % 3 == 0:
        return 'tizz'
    if x % 5 == 0:
        return 'buzz'
    else:
        return x

print(tizz_buzz(15))

