#Crie um programa que organize cadastros de alunos. No cadastro do aluno é necessário ser informado o seu nome, email e idade. Faça a organização e validação desses dados.

# O programa deve (essa parte deve ser organizada em funções): 

#- Validar os e-mails (considerar válido apenas se tiver @ e .).

#- Separar os alunos em maiores e menores de idade.

#- Gerar uma lista apenas com os cadastros válidos(cadastros válidos são aqueles onde o email é válido e a idade é maior que 0).

# - No final, ele deve exibir um relatótrio contendo:
        #- Total de cadastros válidos

        # -Quantidade de menores de idade

        #- Quantidade de maiores de idade


def validar_email(email):
    return '@' in email and '.' in email

def validar_idade(idade):
    return idade > 0

def validar_cadastro(email, idade):
    return validar_email(email) and validar_idade(idade)

def criar_relatorio(cadastro_valido):
    total = len(cadastro_valido)
    maior = 0
    menor = 0

    for item in cadastro_valido:
        if item['idade'] >= 18:
            maior += 1
        else:
            menor += 1

    print('\n============== RELATÓRIO FINAL ==============')
    print(f'Total de cadastros válidos: {total}')
    print(f'Alunos maiores de idade: {maior}')
    print(f'Alunos menores de idade: {menor}')


cadastros_alunos = []
print('================ CADASTRO DE ALUNOS ================')

while True:
    print('Informe os dados do aluno: ')

    nome = input('Nome: ')
    email = input('Email: ')
    idade = int(input('Idade: '))

    aluno = {'nome': nome, 'email': email, 'idade': idade}

    if validar_cadastro(email, idade):
        cadastros_alunos.append(aluno)
        print('Cadastro realizado com sucesso!')
    else:
        print('Cadastro inválido! Verifique o email ou idade do aluno.')

    resp = input('Quer continuar cadastrando alunos? [S/N] ').upper()

    if resp == 'N':
        break

criar_relatorio(cadastros_alunos)