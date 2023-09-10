car=input()
def eh_vogal(car):
    vogais=['a','e','i','o','u']
    car=car.lower()
    if car in vogais:
        return True
    else:
        return False
resultado=eh_vogal(car)
print(resultado)