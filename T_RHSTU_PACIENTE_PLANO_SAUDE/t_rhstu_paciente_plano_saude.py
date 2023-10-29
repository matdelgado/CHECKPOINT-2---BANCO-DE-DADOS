import random
from datetime import datetime, timedelta
import itertools

def gerar_numero_carteira_saude(existing_numbers):
    while True:
        numero_carteira = ''.join(str(random.randint(0, 9)) for _ in range(10))
        if numero_carteira not in existing_numbers:
            existing_numbers.add(numero_carteira)
            return numero_carteira
        
existing_carteira_numbers = set()

def generate_random_sql_date(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randint(0, days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)

    sql_formatted_date = random_date.strftime("%Y-%m-%d")
    
    return sql_formatted_date

quantidade_pacientes = 1000000
planos_saude = list(range(1, 13))  

with open("T_RHSTU_PACIENTE_PLANO_SAUDE/inserir_paciente_plano_saude.sql", "w") as sqlfile:
    cont = 0
    combinacao_pacientes_planos = list(itertools.product(range(1, quantidade_pacientes + 1), planos_saude))
    random.shuffle(combinacao_pacientes_planos)  
    combinacao_pacientes_planos = combinacao_pacientes_planos[:quantidade_pacientes]
    for _ in range(1, quantidade_pacientes + 1):
        id_combinacao = _
        id_paciente = _
        id_plano_saude = random.randint(1, 12)
        nr_carteira_ps = gerar_numero_carteira_saude(existing_carteira_numbers)
        dt_inicio = generate_random_sql_date(2020, 2022)
          
        sql_command = (
            f"INSERT INTO T_RHSTU_PACIENTE_PLANO_SAUDE (ID_PACIENTE_PS, ID_PACIENTE, ID_PLANO_SAUDE, NR_CARTEIRA_PS, DT_INICIO, DT_CADASTRO, NM_USUARIO) "
            f"VALUES ({id_combinacao}, {id_paciente}, {id_plano_saude}, '{nr_carteira_ps}', TO_DATE('{dt_inicio}', 'YYYY-MM-DD'), SYSDATE, USER);\n"
        )
        sqlfile.write(sql_command)
        
        if cont == 1000:
            sqlfile.write("COMMIT;\n")
            cont = 0
        else:
            cont += 1
    sqlfile.write("COMMIT;")