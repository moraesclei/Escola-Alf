"""Este código é para exemplificar uma estrutura de cálculo de média."""


print('-'*30)
print('AVALIAÇÃO FINAL ')
print('-'*30)

aluno = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira Nota: '))
nota2 = float(input('Digite a segunda Nota: '))
media = (nota1+nota2) / 2


AP = 'Aprovado'
RP = 'Reprovado'

print(aluno + ' teve a média: ' + str(media))

if media >= 7:
    print('Situação: ', AP)
else:
    print('Situação: ', RP)
