# Script para solucionar o 1º desafio de uma vesrsão V1 de operações bancárias 
from datetime import datetime


def pontuacao():
    p = "=-=" * 10 

    return p


def data_hora_atual():
    data_hora = datetime.now()
    data_hora = str(data_hora)[:-7]

    return data_hora


linha = pontuacao()

deposito = 0
saque = 0
extrato = f"""
{linha}
{"Extrato Bancário".center(len(linha))}
{linha}
"""
saldo = 0

menu = f"""
{linha}
{"Banco DIO".center(len(linha))}
{linha}
[ 1 ] - Depósito
[ 2 ] - Saque
[ 3 ] - Extrato
[ 0 ] - Sair
"""

while True:
    print(menu)
    try:
        operacao = int(input("Digíte qual operação deseja fazer: "))
        if operacao in (1, 2, 3, 0):

            match operacao:

                case 1:
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

                case 2:
                    while True:
                        try:
                            print(linha)
                            saque = float(input("Digíte o valor do saque: R$ "))
                            if saque > saldo or saque <= 0:
                                print(f"Operação inválida! Saldo total: {saldo}")
                                break
                            data_hora = data_hora_atual()
                            extrato += f"\n\nData: {data_hora}\nSaque - {saque}"
                            break
                        except ValueError:
                            print("Entrada inválida, digíte novamente!")

                case 3:
                    while True:
                        try:
                           extrato += f"\n\nSaldo Total: {saldo}"
                           print(extrato)
                           break
                        except ValueError:
                            print("Entrada inválida, digíte novamente!")

                case 0:
                    print(linha)
                    print("Sistema bancário finalizado com sucesso!")
                    break
        else:
            print("Operação inválida...digíte novamente!")
    except ValueError:
        print("Entrada inválida, digíte novamente!")