# Você irá criar um gerenciador simples de senhas no terminal, usando Python. O foco é praticar listas, dicionários, funções, laços e validações. 
# Desenvolva um programa que permita ao usuário armazenar, visualizar, buscar e remover senhas de forma simples.

senhas = []

while True:
    print('\n=============== MENU ===============')
    print('O que você deseja fazer? ')
    print('1 - Adicionar nova senha')
    print('2 - Listar todos os serviços cadastrados')
    print('3 - Buscar senha de um serviço')
    print('4 - Remover um serviço')
    print('5 - Sair do programa')
    op = int(input('Escolha uma opção: '))

    if op == 1:
        while True:
            servico = input('Qual o serviço? ').lower()

            #verifica se o serviço existe
            existe = False 
            for item in senhas:
                if item['servico'] == servico:
                    existe = True
                    break

            if existe:
                print('Serviço já existente. Tente Novamente.')
            else:
                print('Serviço cadastrado com sucesso!')
                break

        usuario = input('Qual o usuario? ')
        senha = input('Qual a senha? ')

        valores_usuarios = {
            'servico': servico,
            'usuario': usuario,
            'senha': senha
        }

        senhas.append(valores_usuarios)
        print('Nova senha adicionada com sucesso!')
        
    if op == 2:
        if not senhas:
            print('Nenhum serviço foi cadastrado ainda')
        else:
            print('Listando todos os serviços cadastrados: ')

            for item in senhas:
                print(item['servico'])

    if op == 3:
        while True:
            #Buscando a senha de um serviço
            servico_usuario = input('Informe o nome de um serviço: ').lower()

            existe = False
            for item in senhas:
                if item['servico'] == servico_usuario:
                    existe = True
                    print(f"Usuário: {item['usuario']}, Senha: {item['senha']}")
                    break
            
            if existe:
                print('Fim da busca de senha do serviço digitado.')
                break
            else:
                print('Este serviço não existe. Tente novamente.')
            
    if op == 4:
        #Remover um serviço
        while True:
            remover_servico = input('Informe o serviço que deseja remover: ').lower()

            existe = False
            for item in senhas:
                if item['servico'] == remover_servico:
                    existe = True
                    break

            if existe:
                resp_usuario = input(f'Deseja mesmo remover o serviço {remover_servico} [S/N]? ').upper()

                if resp_usuario == 'S':
                    for item in senhas:
                        if item['servico'] == remover_servico:
                            senhas.remove(item)
                            break
                    print('Serviço removido com sucesso!')

                else:
                    print('Serviço não removido')
                break
            else:
                print('Serviço não encontrado. Tente novamente.')

    if op == 5:
        print('Saindo do programa...')
        break

