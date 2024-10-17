def sacar(*,saldo, valor, extrato, limite,numero_saques, limite_saques):
    if valor >= 0:
        if numero_saques <=3:
            saldo -= valor
            extrato += f"Saque:\tR$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")  
    return saldo, extrato

def depositar(saldo, valor, extrato,/):
    if valor >= 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")    
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    return f"O saldo atual é {saldo}"

LIMITE_SAQUES = 3
saldo = 0
extrato = ""
limite = 500
numero_saques = 0

print("Escolha a opção:\n[1]-Depósito\n[2]-Saque")

while True:
    opcao = int(input())
    if opcao == 1:
        valor = float(input("Valor do depósito: "))
        saldo, extrato = depositar(valor, saldo, extrato)
        print(f"Saldo: R$ {saldo:.2f}")
    elif opcao == 2:
        valor = float(input("Valor do saque: "))
        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )
        print(f"Saldo: R$ {saldo:.2f}")