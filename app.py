from IPV4.classes.CalculateIPV4 import CalculateIPV4

ip = input('Insira o IP da rede: ')
mascara = input('Insira a máscara da rede (se não tiver, [Enter]): ')
prefixo = int(input('Insira o prefixo da rede (se não tiver, [Enter]): '))

calculate_IPV4 = CalculateIPV4(ip=ip, mascara=mascara, prefixo=prefixo)

print(f'IP: {calculate_IPV4.ip}')
print(f'Máscara: {calculate_IPV4.mascara}')
print(f'Rede: {calculate_IPV4.rede}')
print(f'Broadcast: {calculate_IPV4.broadcast}')
print(f'Prefixo: {calculate_IPV4.prefixo}')
print(f'Número de IPs: {calculate_IPV4.num_ips}')

# '192.168.0.1'
# '255.255.255.192'
# 26