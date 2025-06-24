# Script para solucionar o 2º desafio de uma vesrsão V2 de operações bancárias com funções
from datetime import datetime

# Listas
usuarios = []

# Funções úteis
def pontuacao():
    p = "=-=" * 10 

    return p


def data_hora_atual():
    data_hora = datetime.now()
    data_hora = str(data_hora)[:-7]

    return data_hora


def criar_usuario(nome, data_nascimento, cpf, logradouro, bairro, cidade, sigla_estado, lista_usuarios):

    nome = str(nome).strip().title()
    data_nascimento = str(data_nascimento).strip()
    cpf = str(cpf).strip()
    logradouro = str(logradouro).strip().title()
    bairro = str(bairro).strip().title()
    cidade = str(cidade).strip().title()
    sigla_estado = str(sigla_estado).strip().upper()

    endereco = f"{logradouro} - {bairro} - {cidade}/{sigla_estado}"

    for cpf_usuario in lista_usuarios:
        if cpf_usuario[0] == cpf:
            return print("CPF já está cadastrado!")
        
    lista_usuarios.append([cpf, nome, data_nascimento, endereco])

    return None


def verificar_usuario(cpf, lista_usuarios):
    for usuario in lista_usuarios:
        if cpf == usuario[0]:
            return True
        else:
            return False 


# Funções do sistema
def realizar_depositos():
    while True:
        try:
            print(linha)
            deposito = float(input("Digíte o valor do depósito R$ "))
            if deposito <= 0:
                print("Erro...digíte um valor maior que 0!")
                break
            saldo += deposito
            data_hora = data_hora_atual()
            extrato += f"\n\nData: {data_hora}\nDepósito + R$ {deposito}"
            break
        except ValueError:
            print("Entrada inválida, digíte novamente!")

    return None


def realizar_saque(*, saque):
    while True:
        try:
            print(linha)
            if saque > saldo or saque <= 0:
                print(f"Operação inválida! Saldo total: {saldo}")
                break
            data_hora = data_hora_atual()
            extrato += f"\n\nData: {data_hora}\nSaque - {saque}"
            break
        except ValueError:
            print("Entrada inválida, digíte novamente!")

    return saque, saldo, extrato


def visualizar_extrato():
    while True:
        try:
            extrato += f"\n\nSaldo Total: {saldo}"
            print(extrato)
            break
        except ValueError:
            print("Entrada inválida, digíte novamente!")

    return None


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

while True:
    print(login)
    try:
        inicio_usuario = int(input("Opção: "))
        if inicio_usuario in (1, 2, 0):

            match inicio_usuario:

                case 1:
                    while True:
                        cpf = str(input("Digíte o seu CPF (somente números Ex: 12345678910): "))
                        if len(cpf) < 11:
                            print(f"Erro! Total digítado: {len(cpf)}, é necessário 11 digítos...Tente novamente!")
                        elif not cpf.isdigit():
                             print("Erro! Digíte somente números...")
                        else:
                            usuario_cadastrado = verificar_usuario(cpf=cpf, lista_usuarios=usuarios)
                            # if usuario_cadastrado == True:

    except ValueError:
        print("Entrada inválida, digíte novamente!")

    try:
        operacao = int(input("Digíte qual operação deseja fazer: "))
        if operacao in (1, 2, 3, 0):

            match operacao:

                case 1:
                    saque = float(input("Digíte o valor do saque: R$ "))
                    realizar_depositos(saque)

                case 2:
                    realizar_saque()

                case 3:
                    visualizar_extrato()

                case 0:
                    print(linha)
                    print("Sistema bancário finalizado com sucesso!")
                    break
        else:
            print("Operação inválida...digíte novamente!")
    except ValueError:
        print("Entrada inválida, digíte novamente!")