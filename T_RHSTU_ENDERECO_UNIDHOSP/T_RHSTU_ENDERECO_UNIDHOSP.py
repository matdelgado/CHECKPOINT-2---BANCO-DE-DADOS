import random
from datetime import datetime, timedelta
import oracledb 

connection = oracledb.connect(user='rm552189', password='310503',
                        dsn='oracle.fiap.com.br/orcl')

def obter_ids_logradouro():
        cursor = connection.cursor()
        query = """
        SELECT l.id_logradouro, l.nm_logradouro, b.nm_bairro, c.nm_cidade, e.nm_estado
        FROM t_rhstu_logradouro l
        JOIN t_rhstu_bairro b ON b.id_bairro = l.id_bairro
        JOIN t_rhstu_cidade c ON c.id_cidade = b.id_cidade
        JOIN t_rhstu_estado e ON e.id_estado = c.id_estado
        WHERE l.id_logradouro IN (
            SELECT MAX(l.id_logradouro)
            FROM t_rhstu_logradouro l
            JOIN t_rhstu_bairro b ON b.id_bairro = l.id_bairro
            JOIN t_rhstu_cidade c ON c.id_cidade = b.id_cidade
            JOIN t_rhstu_estado e ON e.id_estado = c.id_estado
            GROUP BY e.id_estado
        )
        """

        cursor.execute(query)

        ids_logradouro = [row[0] for row in cursor.fetchall()]

        cursor.close()
        connection.close()
        return ids_logradouro

array = obter_ids_logradouro()

def obter_info_endereco(id_end_hospital):
        connection = oracledb.connect(user='rm552189', password='310503',
                        dsn='oracle.fiap.com.br/orcl')
        cursor = connection.cursor()
        query = """
        SELECT NR_LOGRADOURO, DS_COMPLEMENTO_NUMERO, DS_PONTO_REFERENCIA
        FROM T_RHSTU_UNID_HOSPITALAR
        WHERE ID_UNID_HOSPITAL = :id_end_hospital
        """

        cursor.execute(query, id_end_hospital=id_end_hospital)

        row = cursor.fetchone()
        cursor.close()
        connection.close()
        if row:
            nr_logradouro, ds_complemento_numero, ds_ponto_referencia = row
            return nr_logradouro, ds_complemento_numero, ds_ponto_referencia
        else:
            return None



def generate_random_foundation_date():
    start_date = datetime.now() - timedelta(days=365 * 50)

    current_date = datetime.now()

    random_date = start_date + timedelta(days=random.randint(0, (current_date - start_date).days))

    return random_date.strftime("%d/%m/%Y")

complementos_endereco = [
    "Apto. 101",
    "Sala 3A",
    "Bloco B",
    "Lote 27",
    "Casa Verde",
    "Edificio Central",
    "Andar 2",
    "Loja 5",
    "Torre Sul",
    "Condominio Residencial",
    "Fundos",
    "Terreo",
    "Subsolo",
    "Casa Amarela",
    "Loja 12",
    "Apto. 205",
    "Bloco 3",
    "Lote 8",
    "Casa Branca",
    "Edificio Azul",
]

with open("T_RHSTU_ENDERECO_UNIDHOSP/inserir_enderecos_unid_hosp.sql", "w") as sqlfile:
    for i in range(1, 28):
        A = obter_info_endereco(i)
        ID_END_UNIDHOSP = i
        ID_UNID_HOSPITAL = i
        ID_LOGRADOURO = array[i-1]
        NR_LOGRADOURO = A[0]
        DS_COMPLEMENTO_NUMERO = A[1]
        DS_PONTO_REFERENCIA = A[2]
        DT_INICIO = datetime.now().strftime("%d/%m/%Y")
        sql_command = (
            f"INSERT INTO T_RHSTU_ENDERECO_UNIDHOSP (ID_END_UNIDHOSP, ID_UNID_HOSPITAL, ID_LOGRADOURO, NR_LOGRADOURO, "
            f"DS_COMPLEMENTO_NUMERO, DS_PONTO_REFERENCIA, DT_INICIO, DT_CADASTRO, NM_USUARIO) "
            f"VALUES ({ID_END_UNIDHOSP}, {ID_UNID_HOSPITAL}, {ID_LOGRADOURO}, {NR_LOGRADOURO}, "
            f"'{DS_COMPLEMENTO_NUMERO}', '{DS_PONTO_REFERENCIA}', "
            f"TO_DATE('{DT_INICIO}', 'DD/MM/YYYY'), "
            f"SYSDATE, USER);\n")
        sqlfile.write(sql_command)

