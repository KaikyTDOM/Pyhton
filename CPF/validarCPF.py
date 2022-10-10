while True:
    cpf = input("Digite um CPF: ")
    novoCPF = cpf[:-2]
    indexReverse = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novoCPF[index]) * indexReverse

        indexReverse -= 1
        if indexReverse < 2:
            indexReverse = 11
            digito = 11 - (total % 11)

            if digito > 9:
                digito = 0

            total = 0
            novoCPF += str(digito)

    sequencia = novoCPF == str(novoCPF[0]) * len(cpf) #Evita sequências como 11111111111

    if cpf == novoCPF and not sequencia:
        print("CPF válido")
    else:
        print("CPF inválido")
