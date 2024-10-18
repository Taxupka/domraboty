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
    string = str(string)
    list_to_search = list(list_to_search)
    for word in list_to_search:
        if string.lower() in word.lower() or word.lower() in string.lower():
            print(True)
            break
        else:
            print(False)
            break
    countcalls()


is_contains('AAA', ['aa', 'aasd', 'aaa'])
is_contains('Hate', ['fata', 'hatE', 'HATE'])
string_info('Daddy')
string_info('asdasdasdadasdsda')
is_contains('ddd', ['ddd', 'assda', 'sdfdddf'])
is_contains('asd', ['asda', 'dsdf'])
print(calls)






