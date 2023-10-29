from datetime import datetime, timedelta
import random
import oracledb

codigos_barras_usados = set()

def gerar_nome_medicamento():
    prefixos = ["Apo", "Neo", "Pro", "Ulti", "Zylo", "Xeno", "Cyto", "Mega", "Omni", "Ultra", "Zyto", "Nexa", "Lipo", "Mito", "Penta", "Keto", "Tera", "Retro", "Vita", "Nexo", "Lipo", "Myo", "Spira", "Hypo", "Iso", "Pyra", "Dyna", "Cryo", "Lyso", "Xylo",
                "Phyto", "Glyco", "Zara", "Qubo", "Lyra", "Zora", "Vexo", "Sylva", "Pyro", "Zyva", "Cyva", "Myra", "Zyra", "Kora", "Nera", "Vela", "Yara", "Cera", "Fera", "Gara", "Hera", "Iera", "Jera", "Lera", "Mera", "Pera", "Rera", "Sera", "Tera", "Vera", "Zera"]

    sufixos = ["cin", "fen", "nol", "dol", "pam", "zol", "xan", "zin", "ron", "pex", "nox", "bex", "tex", "pox", "mycin", "phine", "zine", "dine", "sine", "mide", "zide", "cide", "tide", "nide", "ride", "pide", "vire", "tane", "sone", "sate",
               "vate", "cate", "date", "late", "pate", "rate", "tate", "mate", "nate", "kate", "pyle", "lyte", "tyne", "ryne", "cyte", "phyte", "vate", "cate", "rate", "fate", "gate", "hate", "kate", "late", "mate", "nate", "pate", "sate", "tate"]

    meio = ["med", "tec", "zon", "sol", "trez", "fex", "vew", "rex", "zel", "dea", "gen", "zen", "heg", "lez", "ven", "rem", "tex", "pey", "bey", "zex", "mei", "kea", "nix", "pil", "six", "lix", "vin", "tix", "ciu", "riz",
            "mil", "nux", "lun", "dua", "lyx", "pyw", "mya", "cyo", "tya", "rye", "zyx", "poa", "voa", "doz", "nom", "zol", "coo", "fom", "lou", "mou", "soa", "toz", "boe", "gox", "hox", "joz", "kox", "roy", "voy", "woy", "yol", "zoe"]

    nome = random.choice(prefixos) + random.choice(meio) + \
        random.choice(sufixos)
    return nome

def gerar_ds_detalhada(nm_medicamento):
    lista_problemas = [
        "Febre", "Gripe", "Dor de cabeca", "Dor de ouvido", "Dor de estomago", "Insonia",
        "Alergia", "Pressao alta", "Infeccao", "Inflamacao", "Enjoo", "Ansiedade",
        "Depressao", "Doenca cronica", "Controle de colesterol", "Artrite", "Asma",
        "Diabetes", "Enxaqueca", "Transtorno digestivo", "Convulsoes", "Tratamento pos-operatorio",
        "Acne", "Osteoporose", "Hipertensao", "Dores musculares", "Problemas cardiacos",
        "Problemas respiratorios", "Transtornos do sono", "Infeccoes urinarias",
        "Problemas de tireoide", "Disturbios hormonais", "Ulcera", "Aftas", "Dores nas articulacoes",
        "Problemas de pele", "Transtornos neurologicos", "Dores nas costas", "Problemas renais",
        "Disturbios psicologicos", "Transtornos de ansiedade", "Transtornos de humor",
        "Problemas gastrointestinais", "Doencas autoimunes", "Reacoes alergicas",
        "Dores neuropaticas", "Enxaquecas cronicas", "Problemas de visao", "Doencas infecciosas",
        "Problemas de audicao", "Problemas de circulacao", "Transtornos alimentares",
        "Problemas de fertilidade", "Doencas hereditarias", "Dores menstruais", "Dores pos-operatorias",
        "Problemas de prostata", "Transtornos de sono", "Sintomas de menopausa", "Tratamento de cancer",
        "Transtornos de atencao", "Alivio de sintomas de gripes e resfriados", "Problemas de tireoide",
        "Doencas cardiacas", "Problemas pulmonares", "Disturbios de ansiedade", "Depressao pos-parto",
        "Transtorno obsessivo-compulsivo (TOC)", "Transtorno do deficit de atencao com hiperatividade (TDAH)",
        "Transtorno do espectro autista (TEA)", "Esquizofrenia", "Transtorno bipolar",
        "Transtorno de personalidade", "Insuficiencia renal", "Cirrose hepatica",
        "Doencas gastrointestinais cronicas", "Fibromialgia", "Sindrome do intestino irritavel (SII)",
        "Doencas sexualmente transmissiveis (DSTs)", "Artrite reumatoide", "Psoriase", "Lupus",
        "Doenca de Crohn", "Colite ulcerativa", "Enfisema", "Bronquite cronica",
        "Doenca de Alzheimer", "Parkinson", "Esclerose multipla", "Lupus eritematoso sistemico (LES)",
        "Anemia", "Hipotireoidismo", "Hipertireoidismo", "Doenca de Raynaud", "Endometriose",
        "Sindrome do ovario policistico (SOP)", "Doenca renal policistica", "Doenca de Lyme",
        "Tuberculose", "Leucemia", "Linfoma", "Doenca de Hodgkin", "Doenca de Gaucher",
        "Doenca de Fabry", "Hemofilia", "Doenca de von Willebrand", "Hepatite B", "Hepatite C",
        "HIV/AIDS", "Tuberculose", "Malaria", "Doenca de Chagas", "Toxoplasmose", "Dengue",
        "Zika virus", "Chikungunya", "Febre amarela", "Ebola", "COVID-19", "Herpes", "Candidiase",
        "Infeccao por fungos", "Infeccao por bacterias", "Infeccao por virus"
    ]

    lista_grau = ["medio", "leve", "grave"]

    problema = random.choice(lista_problemas)
    grau = random.choice(lista_grau)

    return f"O medicamento {nm_medicamento} e usado para problemas de {problema} de grau {grau}."

def gerar_mg():
    mgs = [0.5, 0.7, 1, 1.5, 2.5, 2.8, 3.7, 5, 10, 15, 20, 25, 50, 60,
           70, 75, 80, 85, 90, 100, 200, 250, 325, 500, 600, 750, 1000]
    return random.choice(mgs)


def gerar_codigo_barras():
    while True:
        codigo_barras = ''.join([str(random.randint(1, 9)) for _ in range(13)])
        if codigo_barras not in codigos_barras_usados:
            codigos_barras_usados.add(codigo_barras)
            return codigo_barras



def gerar_data_cadastro():
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2022, 12, 31)
    random_date = start_date + \
        timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date


with open("T_RHSTU_MEDICAMENTO/inserir_medicamentos.sql", "w") as sqlfile:
    for id_medicamento in range(100000):
        nm_medicamento = gerar_nome_medicamento()
        nr_codigo_barras = gerar_codigo_barras()
        ds_detalhada = gerar_ds_detalhada(nm_medicamento)
        dt_cadastro = gerar_data_cadastro()

        sql_command = (
            f"INSERT INTO T_RHSTU_MEDICAMENTO (ID_MEDICAMENTO, NM_MEDICAMENTO, DS_DETALHADA_MEDICAMENTO, NR_CODIGO_BARRAS, DT_CADASTRO, NM_USUARIO) "
            f"VALUES ({id_medicamento}, '{nm_medicamento}', '{ds_detalhada}', '{nr_codigo_barras}', SYSDATE, USER);\n"
        )
        sqlfile.write(sql_command)
        if id_medicamento % 10000 == 0:
            sqlfile.write("COMMIT\n")
    sqlfile.write("COMMIT\n")
    sqlfile.close()