sabor = int(input('Olá! Informe o sabor desejado: \n 1-Chocolate \n 2-Morango \n 3-Sair \nDigite aqui: '))

while sabor != 3: 
    if sabor > 0 and sabor < 3:
        if sabor == 1:
            qdtbolas = int(input('Insira a quantidade de bolas desejada: '))
            if qdtbolas > 3:
                print('Parabéns! Você acabou de ganhar 10% de desconto!')
            elif qdtbolas > 0 and qdtbolas < 3:
                print('Parabéns! Você acabou de ganhar 5% de desconto!')
            else:
                print('Ops! Opção inexistente, tente novamente.')            
        elif sabor == 2:
            qdtbolas = int(input('Insira a quantidade de bolas desejada: '))
            if qdtbolas > 0: 
                print('Sorvete sem desconto!')
                print('Esperamos que tenha gostado da experiência, até a próxima!')
            else:
                print('Ops! Opção inexistente, tente novamente.')
        else:
            print('Ops! Opção inexistente, tente novamente.')
        sabor = int(input('Olá! Informe o sabor desejado: \n 1-Chocolate \n 2-Morango \n 3-Sair \nDigite aqui: '))
    else:
        print('Ops! Opção inexistente, tente novamente.')
        sabor = int(input('Olá! Informe o sabor desejado: \n 1-Chocolate \n 2-Morango \n 3-Sair \nDigite aqui: '))
print('huuum... Não foi dessa vez, deixa pra próxima, esperamos por você!')
