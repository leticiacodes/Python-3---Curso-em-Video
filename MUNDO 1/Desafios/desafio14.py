#conversão de temperatura
# de celsius para fahrenheit
c = float(input('Digite a temperatura em graus Celsius: '))
f = (c * (9/5)) + 32
print('{} graus celsius em fahrenheit é {}\n'.format(c,f))

#de fahrenheit para celsius
gf = float(input('Digite a temperatura em graus Fahrenheit: '))
gc = (gf - 32) / ((9/5))
print('{} graus fahrenheit em graus celsius é {}'.format(gf,gc))