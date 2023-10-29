import random
import oracledb

conn = oracledb.connect(user='rm552189', password='310503',
                        dsn='oracle.fiap.com.br/orcl')

cursor = conn.cursor()


def gerar_posologia_aleatoria():
    doses = ["500 mg", "1000 mg", "50 mg/ml", "2 comprimidos"]
    frequencias = ["A cada 6 horas", "Uma vez ao dia", "A cada 8 horas", "A cada 12 horas"]
    vias_administracao = ["Oral", "Intravenosa", "Intramuscular", "Topica"]
    duracoes = ["3 dias", "1 semana", "2 semanas", "30 dias"]
    
    medicamento = "Medicamento nao especificado"
    dose = random.choice(doses)
    frequencia = random.choice(frequencias)
    via_administracao = random.choice(vias_administracao)
    duracao = random.choice(duracoes)
    
    posologia = f"Medicamento: {medicamento}\n"
    posologia += f"Dose: {dose}\n"
    posologia += f"Frequencia: {frequencia}\n"
    posologia += f"Duracao: {duracao}\n"
    
    return posologia

def gerar_via_administracao_aleatoria():
    vias_administracao = [
        ("Oral", "via oral"),
        ("Intravenosa", "via intravenosa"),
        ("Intramuscular", "via intramuscular"),
        ("Topica", "via topica")
    ]
    
    via, via_descricao = random.choice(vias_administracao)
    
    return f"Via: {via} ({via_descricao})"

def gerar_observacao_uso_aleatoria():
    observacoes_uso = [
        "Tomar antes das refeicoes",
        "Tomar com um copo de agua",
        "Nao tomar em jejum",
        "Nao misturar com alcool",
        "Manter fora do alcance de criancas",
        "Evitar luz solar direta",
        "Suspender em caso de efeitos colaterais",
        "Consultar um medico se houver duvidas",
    ]
    
    observacao = random.choice(observacoes_uso)
    
    return observacao

def gerar_quantidade_medicamento_aleatoria():
    min_quantidade = 1  
    max_quantidade = 10  
    quantidade = random.randint(min_quantidade, max_quantidade)
    return quantidade

cursor = conn.cursor()

with open("T_RHSTU_PRESCRICAO_MEDICA/inserir_consulta2.sql", "w") as sqlfile:
    cont = 0
    for _ in range(1, 1000001):
        id_prescricao_medica = _
        id_consulta = _
        id_medicamento = random.randint(1, 100001)
        posologia = gerar_posologia_aleatoria()
        via_administracao = gerar_via_administracao_aleatoria()
        observacao_uso = gerar_observacao_uso_aleatoria()
        quantidade_medicamento = gerar_quantidade_medicamento_aleatoria()

        cursor.execute("SELECT ID_UNID_HOSPITAL FROM T_RHSTU_CONSULTA WHERE ID_CONSULTA = :id_consulta", id_consulta=id_consulta)
        result = cursor.fetchone()
        id_unid_hospital = result[0] if result else None

        if id_unid_hospital is not None: 
            sqlfile.write(f"INSERT INTO T_RHSTU_PRESCRICAO_MEDICA (ID_PRESCRICAO_MEDICA, ID_UNID_HOSPITAL, ID_CONSULTA, ID_MEDICAMENTO, DS_POSOLOGIA, DS_VIA, DS_OBSERVACAO_USO, QT_MEDICAMENTO, NM_USUARIO, DT_CADASTRO) VALUES ({id_prescricao_medica}, {id_unid_hospital}, {id_consulta}, {id_medicamento}, '{posologia}', '{via_administracao}', '{observacao_uso}', {quantidade_medicamento}, USER, SYSDATE);\n")

        if cont == 1000:
            sqlfile.write("COMMIT;\n")
            cont = 0
        else:
            cont += 1

    sqlfile.write("COMMIT;")

cursor.close()
conn.close()