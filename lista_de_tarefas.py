"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""

def comando_invalido():
    print('Comando inválido.\n')
    return

def add(argumento, lista):
    return lista.append(argumento)

def undo(lista1, lista2):
    if not lista1:
        comando_invalido()

    else:
        lista2.append(lista1[-1])
        lista1.pop()

def redo(lista1, lista2):
    if not lista2:
        comando_invalido()

    else:
        lista1.append(lista2[-1])
        lista2.pop()

def list(lista):
    print(f'Tarefas: {", ".join(lista)}\n')

tarefas = []
refaz = []

while True:
    tarefa = input('Opções de tarefa:\nAdicionar tarefa\nListar tarefas\nDesfazer\nRefazer\nNova tarefa: ')

    if not tarefa:
        break

    elif tarefa == 'Adicionar tarefa':
        task = input('Insira a tarefa: ')
        add(task, tarefas)

    elif tarefa == 'Listar tarefas':
        list(tarefas)

    elif tarefa == 'Desfazer':
        undo(tarefas, refaz)

    elif tarefa == 'Refazer':
        redo(tarefas, refaz)

    else:
        comando_invalido()