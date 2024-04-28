import random

BancodedadosUsuarios = []
BancodedadosContas = []
valorSaldo = 0
limite = 500
deposito = ''

def escolhaUsuario():        
 while True: 
    menu()
    escolhadoUsuario = input()
    if int(escolhadoUsuario) == 1:
        criar_usuario()
        
    elif int(escolhadoUsuario) == 2:
        criar_conta() 
    
    elif int(escolhadoUsuario) == 3:
        listar_contas()
    
    elif int(escolhadoUsuario) == 4:
        exibir_extrato()           
    
    elif int(escolhadoUsuario) == 5:
        despositar()

    elif int(escolhadoUsuario) == 6:
        sacar()
    
    elif int(escolhadoUsuario) == 7:
        escolhaUsuario()    

    elif int(escolhadoUsuario) == 8:
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")              

def menu():
 menu = f"""
 ################# MENU #################
        
 Por favor, selecione a opção desejada:
 [1] -> Para novo usuario
 [2] -> Para nova conta
 [3] -> Para listar conta 
 [4] -> Para retirar extrato
 [5] -> Para depositar um valor
 [6] -> Para retirar um valor
 [7] -> Para voltar ao menu inicial 
 [8] -> Para sair 
"""
 print(menu)
   
def despositar():
    global valorSaldo
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
            valorSaldo += valor
            print(f"Depósito: R$ {valor:.2f}\n")

    else:
            print("Operação falhou! O valor informado é inválido.")

def sacar():
    global valorSaldo
    global deposito
    numeroDeSaques = 0
    LIMITE_SAQUES = 3
    
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > valorSaldo

    excedeu_limite = valor > limite

    excedeu_saques = numeroDeSaques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        valorSaldo -= valor
        deposito += f"Saque: R$ {valor:.2f}\n"
        numeroDeSaques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")       
    
def exibir_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not deposito else deposito)
    print(f"\nSaldo: R$ {valorSaldo:.2f}")
    print("==========================================")
           
def criar_usuario():
    nome = input("Digite seu nome: ")
    senha = input("Crie sua senha de 6 dígitos:")
    CPF = input('Dígite seu CPF')

    for usuario in BancodedadosUsuarios:
        if usuario["nome"] == nome or usuario["CPF"] == CPF:
            print("Erro: Nome ou CPF já cadastrado.")
            return
    conta = {"nome": nome, "senha": senha, "CPF": CPF} 
    
    BancodedadosUsuarios.append(conta)
    print("Usuario criado com sucesso")  

def gerar_numero_conta():
    return str(random.randint(100000, 999999))    

def criar_conta():
    
    CPF = input('Digite seu CPF: ')
    nome= input('Digite seu nome: ')
    for usuario in BancodedadosUsuarios:
        if usuario["CPF"] == CPF:
            numero_conta = gerar_numero_conta()
            usuarioExistente = {"CPF": CPF, "Conta": [numero_conta], "nome": nome}
            BancodedadosContas.append(usuarioExistente)
            print("Nova conta criada para o CPF existente. Seu número de conta é:", numero_conta)
            return
    numero_conta = gerar_numero_conta()
    novo_usuario = {"CPF": CPF, "Conta": [numero_conta], "nome": nome}
    BancodedadosContas.append(novo_usuario)
    print("Conta criada com sucesso. Seu número de conta é:", numero_conta)

    
def listar_contas(): 
    print(BancodedadosContas)

def main():
   escolhaUsuario()
   

main()    
              