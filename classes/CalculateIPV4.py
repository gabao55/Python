import re

class CalculateIPV4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        self._calculate_broadcast()
        self._calculate_rede()

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        return self._prefixo

    @ip.setter
    def ip(self, value):
        if not self._valida_valor(value):
            raise ValueError('IP inválido.')

        self._ip = value
        self._ip_bin = self._convert_dec_to_bin(value)

    @mascara.setter
    def mascara(self, value):
        if not value:
            return

        if not self._valida_valor(value):
            raise ValueError('Máscara inválida.')


        self._mascara = value
        self._mascara_bin = self._convert_dec_to_bin(value)

        if not hasattr(self, 'prefixo'):
            self._prefixo = self._mascara_bin.count('1')

    @prefixo.setter
    def prefixo(self, value):
        if not value:
            return False

        if not str(type(value)) == "<class 'int'>":
            raise TypeError('Prefixo não é um inteiro.')

        if value > 32:
            raise ValueError('Prefixo pode ter no máximo 32 bits')

        self._prefixo = value

        self._mascara_bin = ''
        for i in range(value//8):
            self._mascara_bin += 8*'1' + ' '

        self._mascara_bin += (value%8)*'1'

        contador = 0

        for i in range(4 - value//8):
            if contador == 0:
                self._mascara_bin += (8 - value%8)*'0'

            else:
                self._mascara_bin += ' ' + 8*'0'

            contador += 1

        if not hasattr(self, 'mascara'):
            self._mascara = self._convert_bin_to_dec(self._mascara_bin)

    @staticmethod
    def _valida_valor(valor):
        regexp = re.compile(r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$')

        if regexp.search(valor):
            return True

    @staticmethod
    def _convert_dec_to_bin(valor):
        octetes = valor.split('.')
        octetes_bin = [bin(int(x))[2:].zfill(8) for x in octetes]
        return ' '.join(octetes_bin)

    @staticmethod
    def _convert_bin_to_dec(valor):
        octetes = valor.split(' ')
        octetes_dec = [str(int(x, 2)) for x in octetes]
        return '.'.join(octetes_dec)

    def _calculate_broadcast(self):
        inicio_ip_bin = ''
        for i in range(self._prefixo//8):
            inicio_ip_bin += self._ip_bin[i*9:i*9+9]

        inicio_ip_bin += self._ip_bin[(self._prefixo//8*9):(self._prefixo//8*9+self._prefixo%8)]

        contador = 0

        for i in range(4 - self._prefixo // 8):
            if contador == 0:
                inicio_ip_bin += (8 - self._prefixo % 8) * '1'

            else:
                inicio_ip_bin += ' ' + 8 * '1'

            contador += 1

        self._broadcast_bin = inicio_ip_bin
        self._broadcast = self._convert_bin_to_dec(inicio_ip_bin)

    def _calculate_rede(self):
        inicio_ip_bin = ''
        for i in range(self._prefixo // 8):
            inicio_ip_bin += self._ip_bin[i * 9:i * 9 + 9]

        inicio_ip_bin += self._ip_bin[(self._prefixo // 8 * 9):(self._prefixo // 8 * 9 + self._prefixo % 8)]

        contador = 0

        for i in range(4 - self._prefixo // 8):
            if contador == 0:
                inicio_ip_bin += (8 - self._prefixo % 8) * '0'

            else:
                inicio_ip_bin += ' ' + 8 * '0'

            contador += 1

        self._rede_bin = inicio_ip_bin
        self._rede = self._convert_bin_to_dec(inicio_ip_bin)

    def _calculate_number_IPs(self):