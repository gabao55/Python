conversion_factors = [128, 64, 32, 16, 8, 4, 2, 1]

def convert_dec_to_bin(valor):
    bin = ''
    valor = int(valor)

    for power in conversion_factors:
        if valor >= power:
            bin += '1'
            valor -= power

        else:
            bin += '0'

    return bin

def convert_bin_to_dec(valor):
    dec = 0
    index = 0

    for binary in valor:
        if str(binary) == '1':
            dec += conversion_factors[index]

        index += 1

    return dec

IP = '192.168.100.15'
print('IP: ', IP)
IP_list = []
dec = ''

for i in IP:
    if i.isnumeric():
        dec += i

    else:
        IP_list.append(dec)
        dec = ''
IP_list.append(dec)

IP_bin = ''
contador = 0
for octete in IP_list:
    IP_bin += convert_dec_to_bin(octete)

    if contador == (len(IP_list) - 2):
        break

    IP_bin += ' '
    contador += 1

print('IP em bits:', IP_bin)

