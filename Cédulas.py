
print("    \n  'Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis no qual\n "
      " o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.\n "
      " 1A seguir mostre o valor lido e a relação de notas necessárias.'")

valor = int(input("\nDigite um valor inteiro: ... "))

lista_notas = [100, 50, 20, 10, 5, 2, 1]
qnt_notas = 0
resto = -1

print("\nMínimo de cédulas possível: ")
for i in range(len(lista_notas)):

    if resto == 0:
        qnt_notas = 0

    else:
        if i > 0:
            qnt_notas = resto/lista_notas[i]
            resto = (resto % lista_notas[i])
        else:
            qnt_notas = valor/lista_notas[i]
            resto = (valor % lista_notas[i])

    print(f" > {int(qnt_notas)} nota(s) de R$ {int(lista_notas[i])},00")






