def consoantes(x):
    x=x.lower()
    consoantes=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','y','w','z']
    if x in consoantes:
        return True
    else:
        return False
x=input()
resultado=consoantes(x)
print(resultado)