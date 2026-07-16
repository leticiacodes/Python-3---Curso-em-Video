#ler o sexo mas deve aceita apenas 'M' ou 'F'
#se estiver errado peça a digitação novamente até
#o valor coreto
#apenas para uma pessoa até digitar M ou F



while True:
    sexo = str(input('Digite o sexo [F/M]: ')).upper()
    
    if sexo == 'M' or sexo == 'F':
        if sexo == 'F':
            print("Sexo feminino registrado com sucesso")
        else:
            print("Sexo masculino registrado com sucesso")
        break

#guanabara
'''
sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor informe o sexo: ')).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso") 
'''
