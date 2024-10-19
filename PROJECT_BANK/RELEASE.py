import textwrap

#Função de saque
def withdraw(*,balance,value,history, max_value_withdraw,qt_withdraw, qt_limit_withdraw):
    
    #Saldo Insuficiente
    if value > balance:
        print("# Error ---> Operation not autorized! Insuficiente balance.")
    elif qt_withdraw > qt_limit_withdraw:
        print("# Error ---> Operation not autorized! Excedeed quantity <---")
    elif value > max_value_withdraw:
        print("# Error ---> Operation not autorized! Withdraw amount excedeed <---")
    elif value > 0:
        balance -= value
        history += f"Withdraw: R${value:.2f}\n"
        qt_withdraw += 1
        print("\tWithdraw made with Successfully!")
    else:
        print("Operation not autorized!")
    
    return balance, history

#Função de Depósito
def deposit(balance,value,history,/):
    if value > 0:
        balance += value
        history += f"Deposit: R$ {value:.2f}\n"
        print("\tDeposit made with Successfully!")
    else:
        print("Operation not autorized!")
    return balance, history

#Função de Extrato Bancário
def history_account(balance, /,*, history):
    print("=============== HISTORY BANK =================")
    if not history:
        print("Don't have operation executed")
    else:
        print(history)

    print(f"Current Balance R${balance:.2f}\n" + ("="*46))

#Função Principal do Programa
def main():
    #Regras da conta
    QT_LIMIT_WITHDRAW = 3
    max_value_withdraw = 500

    #Informações da conta bancária
    balance = 0
    history = ""
    qt_withdraw = 0
    
    while True:
        options = """\n
    ============== OPERATIONS ==============
    [d]\tDeposit
    [w]\tWithdraw
    [h]\tHistory Bank
    ==> """
        option = input(textwrap.dedent(options))
        
        if option == "d":
            value = float(input("VALUE DEPOSIT: "))
            balance, history = deposit(balance, value, history)
        elif option == "w":
            value = float(input("VALUE WITHDRAW: "))
            balance, history = withdraw(
                balance=balance,
                value=value,
                history=history,
                max_value_withdraw=max_value_withdraw,
                qt_withdraw=qt_withdraw,
                qt_limit_withdraw=QT_LIMIT_WITHDRAW)
        elif option == "h":
            history_account(balance, history=history)
        else:
            print("#Error --> Invalid Operation! ")



#Chamada à Função Principal do Programa
main()



