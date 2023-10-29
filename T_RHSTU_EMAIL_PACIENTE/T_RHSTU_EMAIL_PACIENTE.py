from datetime import datetime
import random
import oracledb
from datetime import datetime, timedelta

def gerar_tipos_email():
    tipos = ["Pessoal", "Profissional"]
    return random.choice(tipos)

def gerar_st_email():
    estados = ['A'] * 95 + ['I'] * 5
    return random.choice(estados)

conn = oracledb.connect(user='rm552189', password='310503',
                        dsn='oracle.fiap.com.br/orcl')

# RECUPERANDO NOMES EXISTENTES NO BANCO DE DADOS
cursor = conn.cursor()
cursor.execute("SELECT NM_PACIENTE FROM T_RHSTU_PACIENTE")
nome_completo = [row[0] for row in cursor.fetchall()]
cursor.close()
conn.close()

dominios = [
    'gmail.com',
    'outlook.com',
    'yahoo.com',
    'hotmail.com',
    'aol.com',
    'icloud.com',
    'protonmail.com',
    'mail.com',
    'zoho.com',
    'yandex.com',
    'fastmail.com',
    'gmx.com',
]

def gerar_emails_aleatorios(nomes_completos):
    emails = set()

    for nome_completo in nomes_completos:
        primeiro_nome = nome_completo.split(' ')[0].lower()
        segundo_nome = nome_completo.split(' ')[1].lower()
        dominio = random.choice(dominios)

        for i in range(2):  # Gera 2 e-mails por paciente
            numero_aleatorio = random.randint(1, 9999)
            email = f"{primeiro_nome}{numero_aleatorio}@{dominio}"

            while email in emails:
                numero_aleatorio = random.randint(1, 9999)
                email = f"{primeiro_nome}.{segundo_nome}.{numero_aleatorio}@{dominio}"

            emails.add(email)
    return list(emails)

with open('T_RHSTU_EMAIL_PACIENTE/inserir_emails.sql', 'w', encoding='utf-8') as sql_file:
    count = 0
    for i, nome in enumerate(nome_completo):
        id_paciente = i + 1
        emails_unicos = gerar_emails_aleatorios([nome])

        for j, ds_email in enumerate(emails_unicos):
            id_email = (i * 2) + j + 1
            tp_email = gerar_tipos_email()
            st_email = gerar_st_email()

            insert_statement = f"INSERT INTO T_RHSTU_EMAIL_PACIENTE (ID_EMAIL, ID_PACIENTE, DS_EMAIL, TP_EMAIL, ST_EMAIL, DT_CADASTRO, NM_USUARIO) VALUES ({id_email}, {id_paciente}, '{ds_email}', '{tp_email}', '{st_email}', SYSDATE, USER);\n"
            sql_file.write(insert_statement)

            if count == 10000:
                sql_file.write("COMMIT\n")
                count = 0
            else:
                count += 1

    sql_file.write("COMMIT")
