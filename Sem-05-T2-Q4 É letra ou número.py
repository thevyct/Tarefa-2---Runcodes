#primeiro definimos um módulo (def)
def letras(c):
    #daremos o comando "if" = se "c" = nossa variável for letra
    if c.isalpha():
        #"return" = retornará como "True" = verdadeiro.
        return True
    #"else" é o comando para caso o "if" seja falso, retornar falso.
    else:
        return False

#No código principal denominamos nossa variável "c" com input fazendo a leitura do teclado.
c = input()
#denominamos que "c" recebe "c.lower" = para converter todos os caracteres em minúsculos (caso a entrada seja Maiúscula)
c = c.lower()
#criaremos uma variável "resultado" para receber nossa função na variável "c".
resultado = letras(c)
#imprimimos o resultado.
print(resultado)