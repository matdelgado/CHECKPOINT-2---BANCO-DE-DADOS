import oracledb
import random
from datetime import datetime, timedelta

conn = oracledb.connect(user='rm552189', password='310503',
                        dsn='oracle.fiap.com.br/orcl')

#RECUPERANDO ID´S de médicos
cursor = conn.cursor()
cursor.execute("SELECT ID_FUNC FROM T_RHSTU_FUNCIONARIO WHERE DS_CARGO = 'Medico'")
id_medico = [row[0] for row in cursor.fetchall()]
cursor.close()
conn.close()


def generate_random_datetime(start_date, end_date):
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')
    time_diff = (end_datetime - start_datetime).total_seconds()
    random_seconds = random.randint(0, int(time_diff))
    random_datetime = start_datetime + timedelta(seconds=random_seconds)
    formatted_datetime = random_datetime.strftime('%Y-%m-%d %H:%M:%S')

    return formatted_datetime

start_date = '2022-01-01 00:00:00'
end_date = '2023-12-31 23:59:59'

dt_hr_consulta = generate_random_datetime(start_date, end_date)

with open("T_RHSTU_CONSULTA/inserir_consulta.sql", "w") as sqlfile:
    cont = 0
    for _ in range(1, 1000001):
        id_unid_hospital = random.randint(1, 27)
        id_consulta = _
        id_paciente = _
        id_func = random.choice(id_medico)
        dt_hr_consulta = dt_hr_consulta
        nr_consultorio = random.randint(1, 99999)

        sql_command = (
            f"INSERT INTO T_RHSTU_CONSULTA (ID_UNID_HOSPITAL, ID_CONSULTA, ID_PACIENTE, ID_FUNC, DT_HR_CONSULTA, NR_CONSULTORIO, DT_CADASTRO, NM_USUARIO) "
            f"VALUES ({id_unid_hospital}, {id_consulta}, {id_paciente}, {id_func}, TO_DATE('{dt_hr_consulta}', 'YYYY-MM-DD HH24:MI:SS'), {nr_consultorio}, SYSDATE, USER);\n"
        )
        sqlfile.write(sql_command)

        if cont == 1000:
            sqlfile.write("COMMIT;\n")
            cont = 0
        else:
            cont += 1
    sqlfile.write("COMMIT;")