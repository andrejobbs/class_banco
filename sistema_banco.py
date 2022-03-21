import time
contaNumero = []
contaNome = []
contaSaldo = []
contaCredito = []
totalCredito = []
class conta:  #1
    def __init__(self,nome,numero,saldo,credito):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        self.credito = credito
        
    def criarConta(self):
        i = 0
        for x in contaNumero:
            i += 1
            if(x == self.numero):
                print("Esta conta já existe, por favor, informe outra conta.")
                print("")
                opcoes()
                return
            else:
                contaNumero.append(self.numero)
                contaNome.append(self.nome)
                contaSaldo.append(self.saldo)
                contaCredito.append(self.credito)
                totalCredito.append(self.credito)
                print("")
                print("Conta criada com sucesso.")
                print("> Nome:",self.nome)
                print("> Numero da conta:",self.numero)
                print("> Saldo da conta:",self.saldo)
                print("> Limite de credito:",self.credito)
                print("")
                opcoes()
                return
        if(i == 0):
            contaNumero.append(self.numero)
            contaNome.append(self.nome)
            contaSaldo.append(self.saldo)
            contaCredito.append(self.credito)
            totalCredito.append(self.credito)
            print("")
            print("Conta criada com sucesso.")
            print("> Nome:",self.nome)
            print("> Numero da conta:",self.numero)
            print("> Saldo da conta:",self.saldo)
            print("> Limite de credito:",self.credito)
            print("")
            opcoes()

    def infoConta(self): #2
       count = 0
       for x in contaNumero:
           if(x == self.numero):
               print("> Nome da conta:",contaNome[count])
               print("> Numero da conta:",contaNumero[count])
               print("> Saldo da conta:",contaSaldo[count])
               print("> Credito da conta:",contaCredito[count])
               print("")
               opcoes()
           count += 1

class banco: #3
    def __init__(self,numero):
        self.numero = numero

    def depositar(self):
        count = 0
        for x in contaNumero:
            if(self.numero == x):
                valor = float(input("Insira o valor que deseja depositar: "))
                contaSaldo[count] = valor
                print("> Novo saldo:",contaSaldo[count])
                print("")
                opcoes()

    def retirarDinheiro(self):
        count = 0
        for x in contaNumero:
           if(x == self.numero):
               print("Saldo da conta:",contaSaldo[count])
               valor = float(input("Insira o valor que deseja sacar: "))
               if(valor <= contaSaldo[count]):
                   print("Saldo atual:",contaSaldo[count])
                   print("")
                   opcoes()
               else:
                   print("")
                   print("Operação cancelada")
                   print("O valor que deseja sacar é maior do que há na conta")
                   print("")
                   opcoes()

    def transferir(self):
       count1 = 0
       count2 = 0
       conta2 = 0
       for x in contaNumero:
           if(x == self.numero):
               conta2 = int(input("Informe o numero da conta que deseja transferir o dinheiro: "))
               print("")
               for y in contaNumero:
                   if(y == conta2):
                       print("Saldo da sua conta:",contaSaldo[count1])
                       valor = float(input("Informe o valor que deseja transferir: "))
                       print("")
                       if(valor <= contaSaldo[count1]):
                           print("Realizando transfencia...")
                           print("")
                           contaSaldo[count1] = contaSaldo[count1] - valor
                           contaSaldo[count2] = contaSaldo[count2] + valor
                           time.sleep(2)
                           print("Transferencia realizada com sucesso")
                           print("> Valor transferido:",valor)
                           print("> Seu novo saldo:",contaSaldo[count1])
                           print("")
                           opcoes()
                       else:
                           print("O valor informado é maior do que há na conta")
                           print("")
                           opcoes()
                   count2 +=1
           count1 += 1

    def pagarCredito(self):
        count = 0
        for x in contaNumero:
            if(x == self.numero):
                print("Seu credito disponivel é de:",contaCredito[count])
                valor = float(input("Informe o valor da conta: "))
                if(valor <= contaCredito[count]):
                    contaCredito[count] = contaCredito[count] - valor
                    print("")
                    print("Pagamento efetuado com sucesso")
                    print("Credito restante:",contaCredito[count])
                    opcoes()
                else:
                    print("O valor que deseja pagar é maior que o limite disponivel")
                    print("")
                    opcoes()
        print("Esta conta não existe")
        opcoes()

    def pagarDebito(self):
        count = 0
        for x in contaNumero:
            if(x == self.numero):
                print("Seu saldo disponivel é de:",contaSaldo[count])
                valor = float(input("Informe o valor da conta: "))
                if(valor <= contaSaldo[count]):
                    contaSaldo[count] = contaSaldo[count] - valor
                    print("")
                    print("Conta paga com sucesso")
                    print("Seu saldo disponivel é de:",contaSaldo[count])
                    opcoes()
                else:
                    print("O valor que deseja pagar é maior que o saldo disponivel")
                    opcoes()
        print("Esta conta não existe")
        opcoes()

    def pagarFatura(self):
        count = 0
        for x in contaNumero:
            if(x == self.numero):
                devendo = totalCredito[count] - contaCredito[count]
                print("Limite total:",totalCredito[count])
                print("Credito disponivel",contaCredito[count])
                print("Sua divida é de:",devendo)
                valor = float(input("Informe o valor que deseja pagar:"))
                if(valor <= devendo):
                    contaCredito[count] = contaCredito[count] + valor
                    print("Seu novo limite disponivel é de:",contaCredito[count])
                    print("")
                    opcoes()
                else:
                    print("O valor que deseja pagar é maior do que esta devendo")
                    opcoes()
            count += 1
        print("Esta conta não existe")
        print("")
        opcoes()

class extrato:
    def __init__(self,numero):
        self.numero = numero
        count = 0
        for x in contaNumero:
            if(x == self.numero):
                print("")
                print("> Numero da conta:",contaNumero[count])
                print("> Nome:",contaNome[count])
                print("> Limite de credito total:",totalCredito[count])
                print("> Credito disponivel:",contaCredito[count])
                print("> Saldo disponivel",contaSaldo[count])
                opcoes()
            count += 1
        print("Esta conta não existe")
        print("")
        opcoes()
    
def opcoes():
    print("1: Novo usuario")
    print("2: Já possuo uma conta")
    op = int(input("Informe o numero da opção desejada: "))
    status = True
    prosseguir = False
    if(op == 1):
        nome_completo = str(input("Informe seu nome completo: "))
        numero_conta = int(input("Informe um numero para sua conta: "))
        saldo = float(input("Informe o saldo da conta: "))
        credito = float(input("Informe o limite de credito da conta: "))
        criar = conta(nome_completo,numero_conta,saldo,credito)
        criar.criarConta()
    elif(op == 2):
        print("")
        print("1: Extrato")
        print("2: Depositar")
        print("3: Retirar dinheiro")
        print("4: Transferir")
        print("5: Pagar com credito")
        print("6: Pagar com debito")
        print("7: Pagar fatura")
        op2 = int(input("Informe o numero da opção desejada: "))
        if(op2 == 1):
           print("")
           numero_conta = int(input("Informe o numero da conta: "))
           visu = extrato(numero_conta)
        if(op2 == 2):
            print("")
            numero_conta = int(input("Informe o numero da conta: "))
            depos = banco(numero_conta)
            depos.depositar()
            
        elif(op2 == 3):
           print("")
           numero_conta = int(input("Informe o numero da conta: "))
           retirar = banco(numero_conta)
           retirar.retirarDinheiro()
        elif(op2 == 4):
           print("")
           numero_conta = int(input("Informe o numero da conta: "))
           transf = banco(numero_conta)
           transf.transferir()
        elif(op2 == 5):
            print("")
            numero_conta = int(input("Informe o numero da conta: "))
            pagCredito = banco(numero_conta)
            pagCredito.pagarCredito()
        elif(op2 == 6):
            print("")
            numero_conta = int(input("Informe o numero da conta: "))
            pagDebito = banco(numero_conta)
            pagDebito.pagarDebito()
        elif(op2 == 7):
            print("")
            numero_conta = int(input("Informe o numero da conta: "))
            pagFatura = banco(numero_conta)
            pagFatura.pagarFatura()
    else:
        print("")
        print("Esta opção não existe, por favor, selecione uma opção valida")
        print("")
        opcoes()

opcoes()
