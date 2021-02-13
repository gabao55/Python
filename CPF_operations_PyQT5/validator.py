def CPF_validate(novo_cpf):
    lista = []

    for i in novo_cpf:
        if i.isnumeric():
            lista.append(i)

    if not lista or len(lista) > 11:
        return 'Invalid value.'

    feedback = ''.join(lista)

    lista.pop(), lista.pop()
    c = 10
    acumulador = 0

    for valor in lista:
        mult = int(valor)*c
        acumulador += mult
        c -= 1

    digito_1 = 11 - (acumulador%11)

    if digito_1 > 9:
        digito_1 = 0

    lista.append(str(digito_1))
    acumulador = 0
    c = 11

    for valor in lista:
        mult = int(valor)*c
        acumulador += mult
        c -= 1

    digito_2 = 11 - (acumulador%11)

    if digito_2 > 9:
        digito_2 = 0

    lista.append(str(digito_2))
    awnser = ''.join(lista)
    cpf = f'{awnser[0]}{awnser[1]}{awnser[2]}.{awnser[3]}{awnser[4]}{awnser[5]}.' \
          f'{awnser[6]}{awnser[7]}{awnser[8]}-{awnser[9]}{awnser[10]}'

    return f'O CPF {cpf} é válido.' if (feedback == awnser) else f'O CPF {novo_cpf} é inválido.'