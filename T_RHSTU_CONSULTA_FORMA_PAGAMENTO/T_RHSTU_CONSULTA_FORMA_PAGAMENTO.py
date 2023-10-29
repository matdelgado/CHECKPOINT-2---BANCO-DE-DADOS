import oracledb
import random
from datetime import datetime, timedelta

conn = oracledb.connect(user='rm552189', password='310503',
                        dsn='oracle.fiap.com.br/orcl')

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

with open("T_RHSTU_CONSULTA_FORMA_PAGAMENTO/inserir_forma_pagto.sql", "w") as sqlfile:
    cont = 0
    for _ in range(1, 1000001):
        id_consulta_forma_pagamento = _
        id_paciente_ps = _
        cursor = conn.cursor()
        cursor.execute("SELECT ID_UNID_HOSPITAL FROM T_RHSTU_CONSULTA WHERE ID_CONSULTA = :id_consulta", id_consulta=_)
        row = cursor.fetchone()
        cursor.execute("")
        if row is not None:
            id_unid_hospital = row[0]
        id_forma_pagto = random.randint(1, 6)
        dt_pagto_consulta = generate_random_datetime(start_date, end_date)
        st_pagto_consulta = random.choice(["P", "A", "C"])
        sql_command = (
            f"INSERT INTO T_RHSTU_CONSULTA_FORMA_PAGTO (ID_CONSULTA_FORMA_PAGTO, ID_UNID_HOSPITAL, ID_CONSULTA, ID_PACIENTE_PS, ID_FORMA_PAGTO, DT_PAGTO_CONSULTA, ST_PAGTO_CONSULTA, DT_CADASTRO, NM_USUARIO) "
            f"VALUES ({id_consulta_forma_pagamento}, {id_unid_hospital}, {_}, {id_paciente_ps}, {id_forma_pagto}, TO_DATE('{dt_pagto_consulta}', 'YYYY-MM-DD HH24:MI:SS'), '{st_pagto_consulta}', SYSDATE, USER);\n"
        )
        sqlfile.write(sql_command)

        if cont == 1000:
            sqlfile.write("COMMIT;\n")
            cont = 0
        else:
            cont += 1

    sqlfile.write("COMMIT;")

conn.close()




    