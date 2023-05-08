#Programa que valide si un número es primo

def primo(n):

    #Divisible entre el mismo y 1 unicamente
    
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
for i in range (-10, 101):
    print(i, "", primo(i))
