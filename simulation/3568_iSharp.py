import string

typ, *args = input()[:-1].split()
for arg in args:
    arg = arg.rstrip(',')
    var = ''
    typee = ''
    for ch in arg:
        if ch in string.ascii_letters:
            var += ch
        elif ch == '[':
            typee += ']['
        elif ch == ']':
            continue
        else:
            typee += ch

    print(typ+typee[::-1], var+';')