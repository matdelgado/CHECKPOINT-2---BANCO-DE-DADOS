from datetime import datetime, timedelta
import random

def generate_random_foundation_date():
    # Define a data de início (por exemplo, 50 anos atrás)
    start_date = datetime.now() - timedelta(days=365 * 50)

    # Define a data atual
    current_date = datetime.now()

    # Gera uma data aleatória entre a data de início e a data atual
    random_date = start_date + timedelta(days=random.randint(0, (current_date - start_date).days))

    return random_date.strftime("%d/%m/%Y")

# Lista de nomes fictícios de hospitais
nomes_hospitais = [
    "Hospital Sao Lucas",
    "Hospital Santa Maria",
    "Hospital Albert Einstein",
    "Hospital Samaritano",
    "Hospital das Clinicas",
    "Hospital Moinhos de Vento",
    "Hospital Sirio-Libanes",
    "Hospital Beneficencia Portuguesa",
    "Hospital Alemao Oswaldo Cruz",
    "Hospital 9 de Julho",
    "Hospital do Coracao",
    "Hospital do Cancer",
    "Hospital do Rim",
    "Hospital Infantil",
    "Hospital Maternidade",
    "Hospital da Crianca",
    "Hospital da Mulher",
    "Hospital das Mulheres",
    "Hospital Geral",
    "Hospital Universitario",
    "Hospital Municipal",
    "Hospital Regional",
    "Hospital Santo Antonio",
    "Hospital Santa Casa",
    "Hospital de Emergencia",
    "Hospital Ortopedico",
    "Hospital de Clinicas",
]

razoes_sociais = [
    "Hospital ABC",
    "Clinica XYZ",
    "Centro Medico 123",
    "Hospital Infantil",
    "Clinica Cardiaca",
    "Maternidade Sao Joao",
    "Centro de Saude A",
    "Hospital Ortopedico",
    "Clinica Odontologica",
    "Maternidade Bem-Vindo",
    "Hospital Sao Lucas",
    "Clinica Pediatrica",
    "Centro de Reabilitacao",
    "Hospital Geral",
    "Clinica Veterinaria",
    "Centro Cirurgico",
    "Hospital Municipal",
    "Clinica de Olhos",
    "Maternidade Feliz",
    "Centro Medico ABC",
    "Hospital Infantil B",
    "Clinica Cardiologica",
    "Centro de Fisioterapia",
    "Hospital Ortopedia X",
    "Clinica Dentaria",
    "Maternidade Alegre",
    "Centro de Saude Y",
]

pontos_referencia = [
    "Proximo a estacao de metro",
    "Em frente ao shopping",
    "Perto da praca central",
    "Ao lado da escola",
    "Proximo ao supermercado",
    "Em frente a igreja",
    "Perto do parque",
    "Ao lado da biblioteca",
    "Proximo ao centro de convencoes",
    "Em frente ao hospital",
    "Perto do terminal de onibus",
    "Ao lado do teatro",
    "Proximo a praia",
    "Em frente ao aeroporto",
    "Perto do centro esportivo",
    "Ao lado do museu",
    "Proximo ao rio",
    "Em frente a universidade",
    "Perto do mercado municipal",
    "Ao lado do centro de saude",
]

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

# Gere 27 unidades hospitalares e crie a query SQL
with open("T_RHSTU_UNID_HOSPITALAR/inserir_unidades_hospitalares.sql", "w") as sqlfile:
    for i in range(1, 28):
        ID_UNID_HOSPITALAR = i
        NM_UNID_HOSPITALAR = random.choice(nomes_hospitais)
        NM_RAZAO_SOCIAL_UNID_HOSP = random.choice(razoes_sociais)
        DT_FUNDACAO = generate_random_foundation_date()
        NR_LOGRADOURO = random.randint(1, 1000)
        DS_COMPLEMENTO_NUMERO = random.choice(complementos_endereco)
        DS_PONTO_REFERENCIA = random.choice(pontos_referencia)
        DT_INICIO = datetime.now().strftime("%d/%m/%Y")

        sql_command = (
            f"INSERT INTO T_RHSTU_UNID_HOSPITALAR (ID_UNID_HOSPITAL, NM_UNID_HOSPITALAR, NM_RAZAO_SOCIAL_UNID_HOSP, "
            f"DT_FUNDACAO, NR_LOGRADOURO, DS_COMPLEMENTO_NUMERO, DS_PONTO_REFERENCIA, DT_INICIO, DT_CADASTRO, NM_USUARIO) "
            f"VALUES ({ID_UNID_HOSPITALAR}, '{NM_UNID_HOSPITALAR}', '{NM_RAZAO_SOCIAL_UNID_HOSP}', "
            f"TO_DATE('{DT_FUNDACAO}', 'DD/MM/YYYY'), {NR_LOGRADOURO}, '{DS_COMPLEMENTO_NUMERO}', '{DS_PONTO_REFERENCIA}', "
            f"TO_DATE('{DT_INICIO}', 'DD/MM/YYYY'), "
            f"SYSDATE, USER);\n")
        sqlfile.write(sql_command)
