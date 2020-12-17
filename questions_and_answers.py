'''

Criando um sistema de perguntas e respostas:

'''

perguntas = {
    'Pergunta 1' : {
        'pergunta' : 'Quanto é 2 + 2? ',
        'respostas' : {
            'a':'1',
            'b':'4',
            'c':'5',
            'd':'12',
            'e':'100',
            },
        'resposta certa': 'b'
    },
    'Pergunta 2' : {
        'pergunta' : 'Quanto é 3 * 2? ',
        'respostas' : {
            'a':'4',
            'b':'10',
            'c':'6',
            'd':'5',
            'e':'222',
            },
        'resposta certa': 'c',
    },
    'Pergunta 3' : {
        'pergunta' : 'Qual propriedade representa a menor temperatura na qual o produto se vaporiza em quantidade suficiente para formar com o ar uma mistura capaz de se inflamar momentaneamente quando sobre ela incide uma centelha?',
        'respostas' : {
            'a':'Número de cetano',
            'b':'Ponto de fuligem',
            'c':'Poder calorífico',
            'd':'Ponto de fulgor',
            'e':'Temperatura inicial de aparecimento de cristal',
            },
        'resposta certa': 'd'
    }
}

pontos = 0

for pk, pv in perguntas.items(): # O .items serve para acessar os dois valores respectivos do dicionário

    print(f'{pk}: {pv["pergunta"]}')

    for letra, resposta in pv['respostas'].items():

        print(f'{letra}) {resposta}')

    resposta_usuario = input('\nQual a sua resposta (a, b, c, d ou e)? ')

    if resposta_usuario == pv['resposta certa']:

        print('\nParabéns, você acertou!\n')

        pontos += 1

    else:

        print('\nVocê errou...\n')

porcentagem = pontos/len(perguntas) * 100

print(f'Você acertou {pontos}/{len(perguntas)} respostas.\n\nSua porcentagem de acerto foi de {porcentagem:.2f}%.')