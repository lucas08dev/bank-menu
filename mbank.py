saldo = 0
opcao = 0
historico = []

while opcao != 5:
    print("====== BANCO ======")
    print()
    print("1. Consultar saldo.")
    print("2. Depositar dinheiro.")
    print("3. Sacar dinheiro.")
    print("4. Ver histórico de operações.")
    print("5. Sair.")
    
    opcao = int(input("Digite a opção desejada: "))
    print()
    
    if opcao == 1:
        print(f"O seu saldo é de: R$ {saldo}")
        historico.append(f"Consulta de saldo: R$ {saldo}")
        print()
        
    if opcao == 2:
        deposito = int(input("Digite o valor do depósito: "))
        print()
        if deposito <= 0:
            print("Erro! Valor inválido.")
        else:
            saldo = saldo + deposito
            print("Deposito realizado com sucesso!")
            print()
            historico.append(f"Depósito de R$ {deposito}")
            print(f"O seu saldo atual é de: R$ {saldo}")
            print()
            
    if opcao == 3:
        saque = int(input("Digite o valor do saque: "))
        print()
        if saque > saldo:
            print("Não é possível realizar saques com valores maiores do que o saldo")
            print()
        elif saque < 0:
            print("Erro! Valor inválido.")
            print()
        else:
            saldo = saldo - saque
            print("Saque realizado com sucesso!")
            print()
            historico.append(f"Saque de R$ {saque}")
            print(f"O seu saldo é de: R$ {saldo}")
            print()
        
    if opcao == 4:
        if len(historico) == 0:
            print("Nenhuma operação realizada.")
        else:
            for operacao in historico:
                print(operacao)
