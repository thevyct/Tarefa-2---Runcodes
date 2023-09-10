def simbolos(y):
    if y.isalpha() or y.isdecimal():
        return False
    else:
        return True
y=input()
resultado=simbolos(y)
print(resultado)