def gerenciador_simples():
    numeros = []
    
    while True:
        print('Gerenciador de números')
        print('Digite um número se deseja adicionar a lista. ')
        print("Digite 'sair' se deseja sair.")
        entrada = input("Número (ou 'sair'): ").lower()
        if entrada == 'sair':
            break
        try:
            numeros.append(float(entrada))
        except ValueError:
            print("Inválido!")

    if numeros:
        print(f"Lista: {numeros}")
        print(f"Soma: {sum(numeros)}")
        print(f"Média: {sum(numeros)/len(numeros):.2f}")
        print(f"Maior: {max(numeros)} | Menor: {min(numeros)}")
    else:
        print("Vazio.")

gerenciador_simples()