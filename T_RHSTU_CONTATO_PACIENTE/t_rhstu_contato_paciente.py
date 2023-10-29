from datetime import datetime
from datetime import datetime, timedelta
import random

ddd_brasil = [
    '021', '022', '027', '031', '032', '033', '034', '035', '037', '019',
    '016', '017', '018', '014', '015', '012', '013', '011', '053', '051',
    '055', '054', '033', '024'
]

numeros_telefone_gerados = set()

def gerar_numero_telefone():
    while True:
        numero = random.randint(10**7, 10**8)
        if random.choice([True, False]):
            numero = random.randint(10**8, 10**9 - 1)
        if numero not in numeros_telefone_gerados:
            numeros_telefone_gerados.add(numero)
            return numero

with open('T_RHSTU_CONTATO_PACIENTE/T_RHSTU_CONTATO_PACIENTE.sql', 'w') as sqlfile:
    cont = 0
    for id_paciente in range(1, 1000001):
        for _ in range(1, 3):
            id_contato = (id_paciente - 1) * 2 + _
            id_tipo_contato = random.randint(1, 6)
            nm_contato = f"Contato_{id_contato}"
            nr_ddi = "+55"
            nr_ddd = random.choice(ddd_brasil)
            nr_telefone = gerar_numero_telefone()

            sql_command = (
                f"INSERT INTO T_RHSTU_CONTATO_PACIENTE (ID_PACIENTE, ID_CONTATO, ID_TIPO_CONTATO, NM_CONTATO, NR_DDI, NR_DDD, NR_TELEFONE, DT_CADASTRO, NM_USUARIO) "
                f"VALUES ({id_paciente}, {id_contato}, {id_tipo_contato}, '{nm_contato}', '{nr_ddi}', '{nr_ddd}', '{nr_telefone}', SYSDATE, USER);\n"
            )
            sqlfile.write(sql_command)
        if cont == 5000:
            sqlfile.write("COMMIT\n")
            cont = 0
        else:
            cont += 1
    sqlfile.write("COMMIT")
            