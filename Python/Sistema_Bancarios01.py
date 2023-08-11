import datetime


menu = """
Bem Vindo ao melhor banco digital do mundo!
Qual operação deseja realizar?

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """
valor = 0
saldo = 0
limite = 700
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
dt = datetime.datetime.now().strftime("%d/%m/%Y Hora %I:%M%p" )


while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            dt = datetime.datetime.now().strftime("%d/%m/%Y Hora %I:%M%p" )
            extrato += f"Depósito: R$ {valor:.2f} - Data: {dt} \n"            

        else:
            print("Falha na operação! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Falha na operação! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Falha na operação! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            dt = datetime.datetime.now().strftime("%d/%m/%Y Hora %I:%M%p" )
            extrato += f"Saque: R$ {valor:.2f} - Data: {dt} \n"
            numero_saques += 1

        else:
            print("Falha na operação! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        dt = datetime.datetime.now().strftime("%d/%m/%Y Hora %I:%M%p" )
        print(f"\nSaldo: R$ {saldo:.2f} - Data: {dt} " )
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")