# == for loop nested ==
    # Outed Loop
    # Inner Loop
    
for numero1 in range(1, 6):
    print ('Produto ' + str(numero1)) # irá imprimir de 0 a 4 - Outed Loop
    for numero2 in range(5):
        print (numero1, numero2)  # Inner Loop
    