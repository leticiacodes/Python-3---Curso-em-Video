#contagem regressiva de 0 a 10
#para estouro de fogos de artificios
#com um segundo de pausa 

from time import sleep

print('CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFICIO!')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FOGOS DE ARTIFICIO 🎆🎆🎆🎆🎆')