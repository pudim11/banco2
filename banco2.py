import textwrap

def menu():
    menu = """\n
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova contas
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    => """
    return input(textwrap.dedent(menu))
 
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito com sucesso")
    else:
        print("\nOperação falhou")
        
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if saldo >= valor and numero_saques < limite_saques and valor <= limite:
        saldo -= valor
        extrato += f"Saque de {valor:.2f} reais\n"
        numero_saques += 1
        print(f"Seu saldo é: {saldo:.2f}")
    elif saldo < valor:
        print("Saldo insuficiente")
    else:
        print("Limite de saques excedido")

    return saldo, extrato
    
def exibir_extrato(saldo,/, *, extrato):
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nsaldo:\t\tR$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o cpf (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Já exixte usuáario com esse cpf!")
        return

    nome = input("informe nome completo: ")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("informe o endereço(logadouro, nro - bairrp, cidade -estado: ")
    
    usuarios.append({"nome" : nome,
                     "data_nascimento": data_nascimento,
                     "cpf" : cpf,
                     "endereço": endereco})
    
    print("criado com sucesso!")
    
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("criada com sucesso!")
        return {"agencia": agencia,"numero_conta": numero_conta,"usuario": usuario}

    print("usuario não encontrado, fluxo de criação de conta encerrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['usuario']['nome']}
        """
        print("+"* 100)
        print(textwrap.dedent(linha))
def Main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = [] 
    
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        op = menu()
        
        if op == "d":
            valor = float(input("Digite um valor: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif op == "s":
            valor = float(input("Digite um valor: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES 
                

            )

        elif op == "e":
            exibir_extrato(saldo, extrato =  extrato)
            
        elif op == "nu":
            criar_usuario(usuarios)
        
        elif op == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
            
        elif op == "lc":
            listar_contas(contas)    
        
        elif op == "q":
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a opção desejada")

Main()
