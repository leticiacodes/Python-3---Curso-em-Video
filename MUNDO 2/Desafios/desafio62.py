#melhorar o desafio 61
#perguntando ao usuario se ele quer mostrar mais alguns termos
#o programa encerra quando ele disser 0 termos

print("Gerador de PA")
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
mais = 1 #mais elementos
qtd = 10 #quantidade de inicio

while mais != 0:
    while cont <= qtd:
            print(f'{termo}->',end=' ')
            termo +=razao
            cont +=1
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar a mais? '))
    qtd += mais

print(f'Progressão finalizada com {qtd} termos')