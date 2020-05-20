def line(str1):
    lnot = str1.find('not')
    lpoor = str1.find('poor')
    if lpoor > lnot and lnot > 0 and lpoor > 0:
        str1 = str1.replace(str1[lnot:(lpoor + 4)], 'good')
        return str1
    else:
        return str1
print(line('The lyrics is not that poor!'))
print(line('The lyrics is poor!'))
