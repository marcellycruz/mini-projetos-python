#Crie um programa em Python que gere um número aleatório entre 1 e 100. O jogador deve tentar adivinhar qual é esse número.

from random import randint

numero = randint(1,100)
tentativas = 0

while True:
    try:
        numero_usuario = int(input('Escolha um número entre 1 e 100: '))
        tentativas += 1

        if numero_usuario == numero:
            print('PARABÉNS! Você acertou!')
            break
        else:
            if numero_usuario > numero:
                print('Muito Alto!. Tente Novamente.')
            elif numero_usuario < numero:
                print('Muito Baixo!. Tente Novamente.')
        
    except ValueError:
        print('Digite somente números entre 1 e 100!')

    except KeyboardInterrupt:
        print(f'\nO usuário desistiu de continuar jogando. O número sorteado era {numero}.')
        break

print(f'\nSeu número de tentativas foi {tentativas}.')
