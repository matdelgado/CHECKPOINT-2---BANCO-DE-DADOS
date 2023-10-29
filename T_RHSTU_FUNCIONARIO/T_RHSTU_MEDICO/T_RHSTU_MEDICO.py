import oracledb
import random

conn = oracledb.connect(user='rm552189', password='310503',
                        dsn='oracle.fiap.com.br/orcl')

#RECUPERANDO ID´S de médicos
cursor = conn.cursor()
cursor.execute("SELECT ID_FUNC FROM T_RHSTU_FUNCIONARIO WHERE DS_CARGO = 'Médico'")
id_medico = [row[0] for row in cursor.fetchall()]
cursor.close()
conn.close()

especialidades_medicas = [

    "Cardiologia",
    "Dermatologia",
    "Ortopedia",
    "Pediatria",
    "Ginecologia",
    "Oftalmologia",
    "Oncologia",
    "Neurologia",
    "Psiquiatria",
    "Cirurgia Geral",
    "Endocrinologia",
    "Urologia",
    "Gastroenterologia",
    "Nefrologia",
    "Otorrinolaringologia",
    "Radiologia",
    "Anestesiologia",
    "Dentista",
    "Cirurgia Plástica",
    "Nutrologia"
]

with open("T_RHSTU_MEDICO/inserir_medico.sql", "w") as sqlfile:
    cont = 0
    for id_func in id_medico:  
        nr_crm = random.randint(10000, 99999)  
        ds_especialidade = random.choice(especialidades_medicas)
        
        sql_command = (
            f"INSERT INTO T_RHSTU_MEDICO (ID_FUNC, NR_CRM, DS_ESPECIALIDADE, DT_CADASTRO, NM_USUARIO) "
            f"VALUES ({id_func}, {nr_crm}, '{ds_especialidade}', SYSDATE, USER);\n"
        )
        sqlfile.write(sql_command)
    
        if cont == 1000:
            sqlfile.write("COMMIT;\n")
            cont = 0
        else:
            cont += 1
    sqlfile.write("COMMIT;")