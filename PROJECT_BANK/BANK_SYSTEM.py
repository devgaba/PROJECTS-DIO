balance_account = 0.0;
withdraw_limit = 0;
lista = [];

#function for withdraw
def withdraw(value):
    global balance_account;
    if(value > 0 and value <= 500.0):
        balance_account -= value;
        lista.append(f"WITHDRAW OF U$ {value}")
        return balance_account;
    elif (value > 500.00):
        print("LIMIT OF WITHDRAW EXCEEDED!");
    else:
        print("NOT ENOUGH BALANCE!");

#function for deposit
def deposit(value):
    global balance_account;
    balance_account += value;
    lista.append(f"DEPOSIT OF U$ {value}")

print("WISH ENTER IN SYSTEM OF BANK? ")
print("[1]YES\n[2]NOT")
user = int(input());

while user == 1:
    print("CHOOSE THE OPERATION: ");
    print("[1] - WITHDRAW \n[2] - DEPOSIT \n[3] - EXTRACT");
    choose = int(input())
    if(choose == 1):
        print("================ WITHDRAW ================")
        withdraw_limit += 1;
        #print(f"The withdraw was u${value_withdraw}");
        #print(f"The balance currently is U${balance_account}");
        if(withdraw_limit > 3):
            print("DIARY QUANTITY OF WITHDRAW EXCEEDED!")
        else:
            value_withdraw = float(input("VALUE WITHDRAW: "));
            withdraw(value_withdraw);
    elif(choose == 2):
        print("================ DEPOSIT ================")
        value_deposit = float(input("VALUE DEPOSIT: "));
        deposit(value_deposit)
        #print(f"The deposit was {value_deposit}");
        print(f"The balance now is U${value_deposit}");
    else:
        print("================ EXTRACT ================")
        for value in lista:
            print(value);
        print(f"The currently extract is U${balance_account}");
    
    
    print("WANNA STAY IN SYSTEM OF BANK? ")
    print("[1]YES\n[2]NOT")
    user = int(input())
