def letras_numeros(x):
    letras_numeros=['0','1','2','3','4','5','6','7','8','9']
    if x.isalpha()or x in letras_numeros:
        return True
    else:
        return False
x=input()
resultado=letras_numeros(x)
print(resultado)