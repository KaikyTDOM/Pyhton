from random import randint

numero = str(randint(100000000, 999999999))

novoCPF = numero
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

print(novoCPF)