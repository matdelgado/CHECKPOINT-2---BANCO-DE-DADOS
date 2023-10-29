from datetime import datetime
from datetime import datetime, timedelta
from random import choices
import random

# Lista de DDDs do Brasil
ddd_brasil = [
    '021', '022', '027', '031', '032', '033', '034', '035', '037', '019',
    '016', '017', '018', '014', '015', '012', '013', '011', '053', '051',
    '055', '054', '033', '024'
]

existing_numbers = set()

def gerar_numero_telefone(existing_numbers):
    while True:
        numero = random.randint(10**7, 10**8) 
        if random.choice([True, False]):  
            numero = random.randint(10**8, 10**9 - 1)
        
        if numero not in existing_numbers:
            existing_numbers.add(numero)
            return numero
        
def gerar_tp_telefone():
    tipos = ['CELULAR', 'COMERCIAL', 'CONTATO OU RECADO', 'RESIDENCIAL']
    return random.choice(tipos)

def gerar_st_telefone():
    estados = ['A'] * 95 + ['I'] * 5
    return choices(estados, k=1)[0]


with open('old\gerar_telefone_paciente/script_inserir_telefones.sql', 'w') as sqlfile:
    cont = 0
    for id_paciente in range(1, 1000001):  
        for _ in range(1, 3): 
            id_telefone = (id_paciente - 1) * 3 + _ 
            nr_ddi = "+55" 
            nr_ddd = random.choice(ddd_brasil)
            nr_telefone = gerar_numero_telefone(existing_numbers)
            tp_telefone = gerar_tp_telefone()
            st_telefone = gerar_st_telefone()

            sql_command = (
                f"INSERT INTO T_RHSTU_TELEFONE_PACIENTE (ID_PACIENTE, ID_TELEFONE, NR_DDI, NR_DDD, NR_TELEFONE, TP_TELEFONE, ST_TELEFONE, DT_CADASTRO, NM_USUARIO) "
                f"VALUES ({id_paciente}, {id_telefone}, '{nr_ddi}', '{nr_ddd}', '{nr_telefone}', '{tp_telefone}', '{st_telefone}', SYSDATE, USER);\n"
            )
            sqlfile.write(sql_command)
        if cont == 10000:
            sqlfile.write("COMMIT\n")
            cont = 0
        else:
            cont += 1