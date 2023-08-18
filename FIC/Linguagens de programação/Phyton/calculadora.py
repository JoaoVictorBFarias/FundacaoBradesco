operacao = int(input('Escolha o tipo de operação \n 0-Sair \n 1-Soma \n 2-Subtração \n 3-Multiplicação'
                 '\n 4-Divisão \nDigite aqui: '))

while operacao != 0: 
    if operacao >= 0 and operacao <= 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        if operacao == 1:
            resultado = num1 + num2
        elif operacao == 2:
            resultado = num1 - num2
        elif operacao == 3:
            resultado = num1 * num2
        elif operacao == 4:
            resultado = num1 / num2
        print('O resultado é', resultado)
        operacao = int(input('Informe o tipo de operação \n 0-Sair \n 1-Soma \n 2-Subtração \n 3-Multiplicação \n 4-Divisão \nDigite aqui: '))
    else:
        print('Operação inválida!')  
        operacao = int(input('Informe o tipo de operação \n 0-Sair \n 1-Soma \n 2-Subtração \n 3-Multiplicação \n 4-Divisão \nDigite aqui: '))
print('Opção de saída realizada com sucesso!')
