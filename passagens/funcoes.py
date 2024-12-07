import sqlite3
import os


def cabecalho(nome_cabecalho):
    os.system('cls')
    print(f'::::::::::  {nome_cabecalho}  ::::::::::\n\n')

def crud():
    while True:
    
        print('1 - Adicionar Cliente\n')
        print('2 - Alterar dados do cliente\n')  
        print('3 - Remover Cliente\n')  
        print('4 - Visualizar Clientes\n')


