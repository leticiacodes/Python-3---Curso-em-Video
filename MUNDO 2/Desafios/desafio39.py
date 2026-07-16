#ler o ano de nascimento
#informar a idade
#se ainda vai se alistar no serviço militar
#se é a hr de se alistar
#se já passou o tempo de alistamento
#mostrar o tempo que falta ou qunato já passou do prazo

from time import localtime
#from datetime import date
#atual = date.today().year
atual = localtime().tm_year

nascimento = int(input('Digite o ano do seu nascimento: '))
idade = atual - nascimento
sexo = str(input('Digite seu sexo: '))
print('Sua idade é: {} anos'.format(idade))

sexo = sexo.strip().lower()
if sexo == 'femino':
    print('Não tem possui alistamento militar obrigatório')
else:
    if idade < 18:
        print('Ainda vai se alistar')
        print('Tempo restante para se alistar: {} anos'.format(18 - idade))
        print('Seu alistamento será em {}'.format(atual + (18 - idade)))
    elif idade == 18:
        print('Hora de se alistar!')
    elif idade > 18:
        print('Já passsou o tempo do alistamento')
        print('Já passou {} anos'.format(idade - 18))
        print('Seu alistamento foi em {}'.format(atual - (idade - 18)))    