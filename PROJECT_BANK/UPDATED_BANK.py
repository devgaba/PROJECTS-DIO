import textwrap


# Operações referentes à conta bancária: sacar, depositar, exibir_extrato              ---------->>>> 1° Parte
def withdraw(*, balance, value, extract, average, qt_withdraw, limit_withdraw):
    exceded_balace = value > balance
    exceded_average = value > average
    exceded_withdraw = qt_withdraw > limit_withdraw

    if exceded_balace:
        print("\n@@@ Failed Operation! Balance empty. @@@")
    elif exceded_average:
        print("\n@@@ Failed Operation! Withdraw limit excedeed. @@@")
    elif exceded_withdraw:
        print("\n@@@ Failed Operation! Diary limit of withdraw excedeed. @@@")
    elif value > 0:
        balance -= value
        extract += f"Withdraw:\tR$ {value:.2f}\n"
        qt_withdraw += 1
        print("\t\tWithdraw sucessfull!")
    else:
        print("\n@@@ Failed Operation! O valor informando é inválido. @@@")

    return balance, extract


def depositar(saldo, valor, extrato, /):
    if valor >= 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n===Depósito realizado com sucesso!===")
    else:
        print("\n@@@ Operação falhou! O valor informando é inválido. @@@")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n============== EXTRATO BANCÁRIO ============")
    print("Não foram realizdas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==============================================")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia,
                "numero_conta": numero_conta,
                "usuario": usuario}

    print("\n @@@Uusário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência:\t{conta['agencia']},
        C/C:\t\t{conta['numero_conta']},
        Titular:\t{conta['usuario']['nome']} 
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


# Operação referente a usuário criar_usuario, filtrar_usuario                         ------->>>>>>>> 2° Parte
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n @@@Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

    # Menu Principal                                                           --------->>>>>> 3° Parte


def menu():
    menu = """\n
    ================ MENU ====================
    [d]\t\tDepósito
    [s]\t\tSaque
    [e]\t\tExtrato Bancário
    [nu]\tNovo Usuário
    [nc]\tNova Conta
    [lc]\tListar Contas
    [q]\t\tSair
    => """
    return input(textwrap.dedent(menu))

    # Função Principal                                                      ------------>>>>> 4° Parte


def main():
    LIMIT_WITHDRAW = 3
    AGENCY = "0001"

    balance = 0
    extract = ""
    average = 500
    qt_withdraw = 0
    users = []
    accounts = []


    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("\tValor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("\tValor do saque: "))
            saldo, extrato = withdraw(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                average=average,
                qt_withdraw=qt_withdraw,
                limit_withdraw=LIMIT_WITHDRAW,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Operação Inválida! por favor selecione novamente a operação desejada.")


main()
