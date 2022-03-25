def outer(str1, str2):
    if str1.upper() == str2.upper():
        return False
    str1 = sorted(str1.upper())
    str2 = sorted(str2.upper())
    if str1 == str2:
        return True
    else:
        return False
print(outer('ate', 'eat'))
print(outer('run', 'run'))