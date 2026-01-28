#Exercicio python no qual é criado um jogo de perguntas e respostas (quiz) no terminal. O jogo faz perguntas, recebe a resposta do jogador, soma pontos e mostra o resultado final.

from time import sleep

quiz = [
    {
        'pergunta': 'O que significa HTML?',
        'opções': ['Hyperlinks and Text Markup Language', 'Home Tool Markup Language', 'HyperText Markup Language', 'High Text Machine Language'],
        'resposta_correta': 3
    },

    {
        'pergunta': 'Qual dessas linguagens é usada principalmente para estilizar páginas web?',
        'opções': ['HTML', 'Java', 'CSS', 'Python'],
        'resposta_correta': 3
    },

    {
        'pergunta': 'O que é um banco de dados?',
        'opções': ['Um programa para criar sites', 'Um local físico para guardar computadores', 'Uma coleção organizada de dados', 'Um tipo de linguagem de programação'],
        'resposta_correta': 3
    },

    {
        'pergunta': 'Qual tecnologia é mais utilizada para tornar páginas web interativas?',
        'opções': ['SQL', 'JavaScript', 'CSS', 'PHP'],
        'resposta_correta': 2
    }, 

    {
        'pergunta': 'O que significa a sigla API?',
        'opções': ['Application Programming Interface', 'Advanced Program Internet', 'Applied Programming Input', 'Application Process Integration'],
        'resposta_correta': 1
    }
]

print('Seja bem-vindo ao quiz sobre tecnologia!')
print('Vamos às perguntas: ')
print()

pontuacao = 0
for pergunta in quiz:
    print(pergunta['pergunta'])

    for i, opcao in enumerate(pergunta['opções']):
        print(f'\033[94m{i+1}\033[0m - \033[93m{opcao}\033[0m')

    while True:
        try:
            resposta = int(input('Qual a opção correta?: '))

            if 1 <= resposta <= len(pergunta['opções']):
                if resposta == pergunta['resposta_correta']:
                    print('\033[32mPARABÉNS!\033[0m')
                    pontuacao += 1  
                else:
                    print(f'\033[31mVOCÊ ERROU! A resposta correta era a opção {pergunta['resposta_correta']}\033[0m')
                break
            
            else:
                print('\033[31mDigite um número dentro das opções!\033[0m')

        except ValueError:
            print('\033[31mEntrada inválida! Digite apenas números entre 1 e 5\033[0m')

print(f'\nQuiz Finalizado!')
print('Carregando resultados...')
sleep(2)
print(f'\033[1;33mVocê acertou {pontuacao} de {len(quiz)} perguntas\033[0m')
