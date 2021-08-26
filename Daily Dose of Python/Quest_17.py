"""
Question: Write a program that computes the net amount
of a bank account based a transaction log from console input. 
The transaction log format is shown as following: D 100 W 200
D means deposit while W means withdrawal. 
Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 
Then, the output should be: 500
"""
def calculate_net_amount(op):
    # separamos los dos tipos de transacciones
    deposit = 0
    withdrawal = 0
    for i in op:
        char=i.split(":")
        if(char[0]=='D'):
            deposit=deposit+int(char[1])
        else:
            withdrawal=withdrawal+int(char[1])   
    return deposit-withdrawal

op=["D:300","D:300","W:200","D:100"]
print(calculate_net_amount(op))

