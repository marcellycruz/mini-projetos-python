#Exercicio python que permite o usuário manipular suas tarefas como cadastrar, listar, marcar como concluída e remover

def menu():
    print('================ MENU ================')
    print('1 - Cadastrar Tarefas')
    print('2 - Listar Tarefas')
    print('3 - Marcar uma tarefa como conluida')
    print('4 - Remover uma tarefa')
    print('5 - Retornar as tarefas pendentes')
    print('6 - Sair do programa')


def cadastrar_tarefas(lst_tarefas, id_atual):
    
    titulo_tarefa = input('Digite o título da tarefa: ')
    conclusao_tarefa = input('A tarefa foi concluida [sim/não]? ')

    concluida = True if conclusao_tarefa == 'sim' else False

    tarefas_usuario = {
        'id': id_atual,
        'titulo': titulo_tarefa,
        'concluida': concluida
    }

    lst_tarefas.append(tarefas_usuario)
    print('Tarefa cadastrada com sucesso!')
    return id_atual + 1
    

def listar_tarefas(lst_tarefas):
    if not lst_tarefas:
        print('Nenhuma tarefa cadastrada.')
        return
    
    for tarefa in lst_tarefas:
        print(tarefa)

def mostrar_tarefas_concluidas(id, lst_tarefas):
    for item in lst_tarefas:
        if item['id'] == id:
            item['concluida'] = True
            print('Tarefa marcada como concluída!')
            return
 
    print('Tarefa não encontrada.')
            
def remover_tarefa(id, lst_tarefas):
    for item in lst_tarefas:
        if item['id'] == id:
            lst_tarefas.remove(item)
            print('Tarefa removida com sucesso!')
            return
        
    print('Tarefa não encontrada.')

def mostrar_tarefas_pendentes(lst_tarefas):
    pendentes = False
    for item in lst_tarefas:
        if not item['concluida']:
            print(item)
            pendentes = True

    if not pendentes:
        print('Não há tarefas pendentes.')
            

tarefas = []
id_atual = 1

while True:
    menu()
    op = int(input('Escolha uma opção: '))

    if op == 1:
        #cadastrar tarefas
        id_atual = cadastrar_tarefas(tarefas, id_atual)

    elif op == 2:
        #Listar tarefas
        listar_tarefas(tarefas)

    elif op == 3:
        #Marcar tarefa como conluida
        id_tarefa = int(input('Digite o id da tarefa para marca-la como concluída: '))
        mostrar_tarefas_concluidas(id_tarefa, tarefas)

    elif op == 4:
        #Remove tarefa pelo id
        id_tarefa = int(input('Digite o id da tarefa para removê-la: '))
        remover_tarefa(id_tarefa, tarefas)

    elif op == 5:
        #Retornar tarefas pendentes
        mostrar_tarefas_pendentes(tarefas)

    elif op == 6:
        print('Saindo do programa...')
        break
    
    else:
        print('Opção inválida! Tente Novamente.')
