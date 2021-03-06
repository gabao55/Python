
def limpar_cnpj(entrada):

    index = 0
    global limpo
    limpo = True

    for valor in entrada:
        if not valor.isnumeric():
            entrada = entrada[0:index] + entrada[index+1:]
            index -= 1

        index += 1

    return entrada

def add_caracteres(string, entrada, start, end):
    for i in range(start, end):
        string += entrada[i]

    return string

def add_caracter(string, caracter):
    string += str(caracter)

    return string

def formatar_cnpj(entrada):
    saida = ''
    saida = add_caracteres(saida, entrada, 0, 2)
    saida = add_caracter(saida, '.')
    saida = add_caracteres(saida, entrada, 2, 5)
    saida = add_caracter(saida, '.')
    saida = add_caracteres(saida, entrada, 5, 8)
    saida = add_caracter(saida, '/')
    saida = add_caracteres(saida, entrada, 8, 12)
    saida = add_caracter(saida, '-')
    saida = add_caracteres(saida, entrada, 12, 14)

    return saida

def calcular_digitos(entrada):

    entrada = entrada[0:-2]

    acumulador1 = 0
    acumulador2 = 0

    contador = 5

    for digito in entrada:
        acumulador1 += int(digito) * contador
        contador -= 1
        if contador == 1:
            break

    contador = 9

    for digito in entrada[4:]:
        acumulador1 += int(digito) * contador
        contador -= 1
        if contador == 1:
            break

    digito1 = 11 - (acumulador1 % 11)

    if digito1 > 9:
        digito1 = '0'

    else:
        digito1 = str(digito1)

    entrada += digito1

    contador = 6

    for digito in entrada:
        acumulador2 += int(digito) * contador
        contador -= 1
        if contador == 1:
            break

    contador = 9

    for digito in entrada[5:]:
        acumulador2 += int(digito) * contador
        contador -= 1
        if contador == 1:
            break

    digito2 = 11 - (acumulador2%11)

    if digito2 > 9:
        digito2 = '0'

    else:
        digito2 = str(digito2)

    saida = entrada + digito2

    return saida

def validar(cnpj_avaliado):
    cnpj_limpo = limpar_cnpj(cnpj_avaliado)
    cnpj_calculado = calcular_digitos(cnpj_limpo)

    if cnpj_limpo == cnpj_calculado:
       return print(f'O CNPJ {formatar_cnpj(cnpj_limpo)} é válido.')

    else:
        return print(f'O CNPJ {formatar_cnpj(cnpj_limpo)} é inválido.')

cnpj = input('Digite o CNPJ a ser validado: ')

validar(cnpj)