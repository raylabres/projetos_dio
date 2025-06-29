# Script para solucionar o 2º desafio de uma vesrsão V2 de operações bancárias com funções
from datetime import datetime
from time import sleep

# Listas
usuarios = []
contas = []

# Funções úteis
def pontuacao():
    p = "=-=" * 10 

    return p


def data_hora_atual():
    data_hora = datetime.now()
    data_hora = str(data_hora)[:-7]

    return data_hora


def criar_usuario(lista_usuarios, cpf=None):
    print(linha)
    nome = str(input("Digíte seu nome: ")).strip().title()
    data_nascimento = str(input("Digíte sua data de nascimento (somente números): ")).strip()
    if cpf is None:
        cpf = str(input("Digíte seu CPF (somente números): ")).strip()
    logradouro = str(input("Digíte o logradouro: ")).strip().title()
    numero = str(input("Digíte o numero: ")).strip().title()
    bairro = str(input("Digíte o bairro: ")).strip().title()
    cidade = str(input("Digíte a cidade: ")).strip().title()
    sigla_estado = str(input("Digíte a sigla do estado: ")).strip().upper()
    print(linha)

    endereco = f"{logradouro} - {numero} - {bairro} - {cidade}/{sigla_estado}"

    for cpf_usuario in lista_usuarios:
        if cpf_usuario[0] == cpf:
            return "CPF já está cadastrado!"
        
    lista_usuarios.append([cpf, nome, data_nascimento, endereco])

    return "Usuário criado com sucesso!"


def verificar_usuario(cpf, lista_usuarios):

    if len(lista_usuarios) < 1:
        return False, None 
    
    for usuario in lista_usuarios:
        if cpf == usuario[0]:
            return True, usuario[1]
    
    return False, None


def criar_conta(cpf):
    global contas
    AGENCIA = "0001"
    if len(contas) == 0:
       contas.append([cpf, 1, AGENCIA])
    else:
        numero_ultima_conta = contas[-1][1]
        contas.append([cpf, numero_ultima_conta+1, AGENCIA])

    return "Conta criada com sucesso!"


# Funções do sistema
def realizar_depositos(deposito):
    global saldo, extrato
    while True: 
        try:
            print(linha)
            if deposito <= 0:
                print("Operação negado! Valor de depósito deve ser maior que 0.")
                break
            saldo += deposito
            data_hora = data_hora_atual()
            print(f"Depósito de R${deposito} realizado com sucesso!")
            print(f"Saldo: R${saldo}")
            extrato += f"\n\nData: {data_hora}\nDepósito + R$ {deposito}"
            break
        except ValueError:
            print("Entrada inválida, digíte novamente!")

    return True


def realizar_saque(*, saque, numero_saques):
    global saldo, extrato
    LIMITE_QTDE_SAQUES = 3
    LIMITE_VALOR_SAQUES = 500
    while True:
        try:
            print(linha)
            if saque > saldo or saque <= 0:
                print(f"Operação negada! Saldo total: {saldo}")
                break
            if numero_saques >= LIMITE_QTDE_SAQUES:
                print(f"Limite diário de saques ({LIMITE_QTDE_SAQUES}) atingido, tente novamente amanhã!")
                break
            if saque > LIMITE_VALOR_SAQUES:
                print(f"Limite de valor de saque (R$ {LIMITE_VALOR_SAQUES},00) atingido, tente um valor menor!")
                break
            saldo -= saque
            data_hora = data_hora_atual()
            print(f"Saque de R${saque} realizado com sucesso!")
            print(f"Saldo: {saldo}")
            extrato += f"\n\nData: {data_hora}\nSaque - {saque}"
            break
        except ValueError:
            print("Entrada inválida, digíte novamente!")

    return True


def visualizar_extrato():
    global saldo, extrato
    while True:
        try:
            print(extrato)
            print(linha)
            print(f"Saldo Total: {saldo}")
            break
        except ValueError:
            print("Entrada inválida, digíte novamente!")

    return None


def operacoes(numero_saques):
    while True:
        try:
            print(menu)
            operacao = int(input("Digíte qual operação deseja fazer: "))
            if operacao in (1, 2, 3, 0):

                match operacao:

                    case 1:
                        deposito = float(input("Digíte o valor do depósito: R$ "))
                        realizar_depositos(deposito)

                    case 2:
                        saque = float(input("Digíte o valor do saque: R$ "))
                        saque_realizado = realizar_saque(saque=saque, numero_saques=numero_saques)
                        if saque_realizado:
                            numero_saques += 1

                    case 3:
                        visualizar_extrato()

                    case 0:
                        print(linha)
                        print("Saindo da conta...")
                        sleep(1)
                        print("Logout realizado com sucesso!")
                        break
            else:
                print("Operação inválida...digíte novamente!")
        except ValueError:
            print("Entrada inválida, digíte novamente!")


linha = pontuacao() # Pontuações (utilizando como moldura do sistema)

# Variáveis 
deposito = 0
saque = 0
saldo = 0

# Variáveis multiplás linhas (menus, logins, extratos, etc)
extrato = f"""
{linha}
{"Extrato Bancário".center(len(linha))}
{linha}
"""
login = f"""
{linha}
{"Banco DIO".center(len(linha))}
{linha}
Olá! Seja bem-vindo(a) ao Banco DIO, você + digital!
\n
Para começar selecione umas das opções abaixo:
\n
[ 1 ] - Já tenho cadastro (login)
[ 2 ] - Não tenho cadastro (registrar)
[ 0 ] - Sair
{linha}
"""
menu = f"""
{linha}
{"Operações Bancárias".center(len(linha))}
{linha}
[ 1 ] - Depósito
[ 2 ] - Saque
[ 3 ] - Extrato
[ 0 ] - Sair
"""

finaliza_sistema = False
while finaliza_sistema is False:
    numero_saques = 0
    print(login)
    try:
        inicio_usuario = int(input("Opção: "))
        if inicio_usuario in (1, 2, 0):

            match inicio_usuario:

                case 1:
                    while True:
                        print(linha)
                        cpf = str(input("Digíte o seu CPF (somente números Ex: 12345678910): "))
                        if len(cpf) < 11 or len(cpf) > 11:
                            print(f"Erro! Total digítado: {len(cpf)}, é necessário 11 digítos...Tente novamente!")
                        elif not cpf.isdigit():
                             print("Erro! Digíte somente números...")
                        else:
                            usuario_cadastrado, nome_usuario_cadastrado = verificar_usuario(cpf=cpf, lista_usuarios=usuarios)
                            if usuario_cadastrado == False:
                                print("Verificando cadastro...")
                                sleep(2)
                                print("Ao que parece você não está cadastrado...")
                                sleep(1)
                                print("Vamos criar um cadastro para você!")
                                cadastrar_usuario = criar_usuario(usuarios, cpf=cpf)
                                criar_conta_usuario = criar_conta(cpf)
                                print(cadastrar_usuario)
                                print(criar_conta_usuario)
                            elif usuario_cadastrado == True:
                                print(linha)
                                print(f"Olá, {nome_usuario_cadastrado}.")
                                operacoes(numero_saques)
                                break
                
                case 2:
                    print(linha)
                    cpf = str(input("Digíte o seu CPF (somente números Ex: 12345678910): "))
                    if len(cpf) < 11 or len(cpf) > 11:
                        print(f"Erro! Total digítado: {len(cpf)}, é necessário 11 digítos...Tente novamente!")
                    elif not cpf.isdigit():
                            print("Erro! Digíte somente números...")
                    cadastrar_usuario = criar_usuario(usuarios, cpf=cpf)
                    criar_conta_usuario = criar_conta(cpf)
                    print(cadastrar_usuario)
                    print(criar_conta_usuario)
                    operacoes(numero_saques)
                    break

                case 0:
                    print(linha)
                    print("Sistema bancário finalizado com sucesso!")
                    finaliza_sistema = True
                    break                   

    except ValueError:
        print("Entrada inválida, digíte novamente!")