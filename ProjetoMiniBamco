extrato = 1
depositar = 2
sacar = 3
sair = 4
usuario_dict = {'nome': 'fulano', 'cpf': 1257283894, 'senha': 123456}
usuario = usuario_dict['nome']
mensagemBemvindo = f"""Bem-vindo,Senhor {usuario},ao Banco Dinherama."""
menu = f"""
 Por favor, selecione a opção desejada:

({extrato}) -> Para retirar extrato
({depositar}) -> Para depositar um valor
({sacar}) -> Para retirar um valor
({sair}) -> Para sair
"""
def escolhasUsuarios():
 global extrato
 deposito = ''
 valorSaldo = 0
 limite = 500
 numeroDeSaques = 0
 LIMITE_SAQUES = 3
 while True: 

    escolhaUsuario = input(menu)
    if int(escolhaUsuario) == int(depositar):
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            valorSaldo += valor
            print(f"Depósito: R$ {valor:.2f}\n")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif int(escolhaUsuario) == int(sacar):
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

    elif int(escolhaUsuario) == int(extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not deposito else deposito)
        print(f"\nSaldo: R$ {valorSaldo:.2f}")
        print("==========================================")

    elif int(escolhaUsuario) == int(sair):
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


def loginUsuario():
    cpfDigitado = float(input('Digite por gentileza seu CPF (sem pontos e traços): '))
    senhaDigitada = float(input('Digite sua senha de 6 dígitos: '))
    if cpfDigitado == usuario_dict['cpf'] and senhaDigitada == usuario_dict['senha']:
        print(mensagemBemvindo)
        escolhasUsuarios()
    else:
        print('CPF ou Senha inválidos.')
              
loginUsuario()
