import oracledb
import random
from datetime import datetime, timedelta

conn = oracledb.connect(user='rm552189', password='310503',
                        dsn='oracle.fiap.com.br/orcl')

#RECUPERANDO ID´S dos motoristas
cursor = conn.cursor()
cursor.execute("SELECT ID_FUNC FROM T_RHSTU_FUNCIONARIO WHERE DS_CARGO = 'Motorista de Ambulância'")
id_motorista = [row[0] for row in cursor.fetchall()]
cursor.close()
conn.close()

def gerar_numero_cnh():
    numero_cnh = ''.join(random.choice("0123456789") for _ in range(11))
    return numero_cnh
def gerar_categoria_cnh():
    categorias = ["A", "B", "C", "D", "E"]
    categoria_cnh = random.choice(categorias)
    return categoria_cnh
def gerar_validade_cnh():
    data_atual = datetime.now()
    anos = random.randint(1, 10)
    data_validade = data_atual + timedelta(days=anos * 365)
    return data_validade.strftime("%Y-%m-%d")


with open("T_RHSTU_FUNCIONARIO/inserir_motoristas.sql", "w") as sqlfile:
    cont = 0
    for id_funcionario in id_motorista:
        numero_cnh = gerar_numero_cnh()
        categoria_cnh = gerar_categoria_cnh()
        validade_cnh = gerar_validade_cnh()

        sql_command = (
            f"INSERT INTO T_RHSTU_FUNCIONARIO (ID_FUNC, NR_CNH, NM_CATEGORIA_CNH, DT_VALIDADE_CNH, DT_CADASTRO, NM_USUARIO) "
            f"VALUES ({id_funcionario}, '{numero_cnh}', '{categoria_cnh}', TO_DATE('{validade_cnh}', 'YYYY-MM-DD'), SYSDATE, USER);\n"
        )
        sqlfile.write(sql_command)

        if cont == 1000:
            sqlfile.write("COMMIT;\n")
            cont = 0
        else:
            cont += 1
    sqlfile.write("COMMIT;")