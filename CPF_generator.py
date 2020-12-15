from random import randint

validez = 's'

while validez != 'n':

    numero = str(randint(0, 99999999999))

    if len(numero) < 11:

        numero = str(numero)

        while len(numero) < 11:

            numero = '0' + numero

    n = numero

    novo_cpf = f'{n[0]}{n[1]}{n[2]}.{n[3]}{n[4]}{n[5]}.{n[6]}{n[7]}{n[8]}-{n[9]}{n[10]}'

    lista = []

    for i in novo_cpf:

        if i.isnumeric():
           lista.append(int(i))

    lista.pop(), lista.pop()

    c = 10
    acumulador = 0

    for valor in lista:

        mult = valor*c
        acumulador += mult
        c -= 1

    digito_1 = 11 - (acumulador%11)

    if digito_1 > 9:

        digito_1 = 0

    lista.append(digito_1)

    acumulador = 0
    c = 11

    for valor in lista:

        mult = valor*c
        acumulador += mult
        c -= 1

    digito_2 = 11 - (acumulador%11)

    if digito_2 > 9:

        digito_2 = 0

    lista.append(digito_2)

    l = lista

    cpf = f'{l[0]}{l[1]}{l[2]}.{l[3]}{l[4]}{l[5]}.{l[6]}{l[7]}{l[8]}-{l[9]}{l[10]}'

    if novo_cpf == cpf:

        print(f'CPF gerado: {cpf}')
        validez = input('Quer continuar ([s] ou [n]? ')


