calls = 0


def countcalls():
    global calls
    calls += 1


def string_info(string):
    string = str(string)
    a = len(string)
    b = string.upper()
    c = string.lower()
    rezult = (a, b, c)
    print(rezult)
    countcalls()


def is_contains(string, list_to_search):
    countcalls()
    string = str(string)
    list_to_search = list(list_to_search)
    for word in list_to_search:
        if string.lower() in word.lower() or word.lower() in string.lower():
            print(True)
            break
        else:
            print(False)
            break



string_info('Daddy')
string_info('Bingobongo')
is_contains('Urban', ['ban', 'BaNaN', 'uBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)






