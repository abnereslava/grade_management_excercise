#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

from time import sleep

lista = []
lista_geral = []
continuar = 's'

while continuar != 'n':
    print('')
    try:
        nome = input('Nome: ').capitalize()
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        lista = [nome, nota1, nota2]
        lista_geral.append(lista[:])
    except ValueError:
        print('Cadastro não realizado. Tente novamente.\n')
        continue
    while True:
        continuar = input('Gostaria de continuar? [s/n]: ').lower()
        if continuar == 's' or continuar == 'n':
            break
        else:
            print('Resposta inválida. Tente novamente.\n')

print('')              
print('=-' * 30)
print(f'{"Nº":<4}{"Nome":<20}{"MÉDIA":>6}')

for indice, aluno in enumerate(lista_geral):
    print(f'{indice :<4} {aluno[0]:<20} {(aluno[1] + aluno[2]) / 2:>6}')
    sleep(0.5)

while True:
    try:
        notas = int(input('Digite o número do aluno para exibir suas notas, ou digite "999" para sair: '))
        sleep(0.5)
        print(f'As notas de {lista_geral[notas][0]} foram: {lista_geral[notas][1]} e {lista_geral[notas][2]}')
        print('')
        if notas == 999:
            break
    except:
        print('Número inválido. Tente novamente.\n')

print('\nEncerrando programa...')
