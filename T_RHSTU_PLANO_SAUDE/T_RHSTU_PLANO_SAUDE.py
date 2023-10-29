import random
from datetime import datetime, timedelta

razoes_sociais = [
    "Unimed Seguradora S/A",
    "Sul América Companhia Nacional de Seguros",
    "Bradesco Saúde S.A.",
    "Amil Assistência Médica Internacional S.A.",
    "Golden Cross Assistência Internacional de Saúde Ltda.",
    "GNDI - Grupo NotreDame Intermédica",
    "Hapvida Assistência Médica Ltda.",
    "Porto Seguro Cia de Seguros Gerais",
    "Associação Auxiliadora das Classes Laboriosas",
    "Allianz Saúde S/A",
    "Sompo Seguros S.A.",
    "Caixa Seguradora Seguros de Vida e Previdência S.A.",
    "MedSênior - Planos de Saúde para Terceira Idade",
    "Unimed Santa Helena - Cooperativa de Trabalho Médico",
    "GreenLine Sistema de Saúde S/A",
    "Assistência à Saúde do Banco do Brasil"
]

nome_fantasia = [
    "Unimed",
    "SulAmérica Saúde",
    "Bradesco Saúde",
    "Amil",
    "Golden Cross",
    "NotreDame Intermédica",
    "Hapvida",
    "Porto Seguro Saúde",
    "São Francisco Saúde",
    "Allianz Saúde",
    "Sompo Seguros",
    "Caixa Seguradora",
    "MedSênior",
    "Santa Helena Saúde",
    "Greenline Sistema de Saúde",
    "Saúde Caixa"
]

descricoes = [
    "Maior cooperativa de saúde do Brasil.",
    "Uma das maiores seguradoras do país, oferecendo ampla rede credenciada.",
    "Plano de saúde oferecido pelo Banco Bradesco.",
    "Maior operadora de planos de saúde do Brasil, com ampla cobertura nacional.",
    "Especializada em planos de saúde para terceira idade.",
    "Oferece planos de saúde com foco em medicina preventiva.",
    "Plano de saúde presente principalmente nas regiões Norte e Nordeste do Brasil.",
    "Oferece planos de saúde com vantagens para segurados Porto Seguro.",
    "Operadora de planos de saúde com foco na região Sudeste.",
    "Seguradora internacional com planos de saúde no Brasil.",
    "Oferece diversos tipos de seguros, incluindo planos de saúde.",
    "Plano de saúde oferecido pela Caixa Econômica Federal.",
    "Especializada em planos de saúde para a terceira idade.",
    "Operadora de planos de saúde com foco na região Sudeste.",
    "Oferece serviços de saúde na cidade de São Paulo.",
    "Plano de saúde para funcionários da Caixa Econômica."
]

cnpjs = [
    "04487255000181",
    "01685053000156",
    "92693118000160",
    "29309127000179",
    "01518211000850",
    "44649812000138",
    "63554067000198",
    "61198164000160",
    "61740791000180",
    "04439627000102",
    "61383493000180",
    "03730204000176",
    "41263240000166",
    "43202472000300",
    "61849980000196",
    "03273648000120"
]


ds_telefones = [
    "21 99663-5118",
    "11 3597-7082",
    "66 99435-5478",
    "15 3347-2322",
    "54 98046-4421",
    "11 99163-2142",
    "19 2817-6332",
    "11 3455-0432",
    "14 2067-5197",
    "11 3068-6766",
    "11 2175-9405",
    "11 98323-6010",
    "15 3682-3368",
    "82 98865-3832",
    "21 3385-7313",
    "17 97951-9144"
]

def generate_random_sql_date(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randint(0, days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)

    sql_formatted_date = random_date.strftime("%Y-%m-%d")
    
    return sql_formatted_date

random_date = generate_random_sql_date(2020, 2022)

with open("T_RHSTU_PLANO_SAUDE/inserir_planos_saude.sql", "w") as sqlfile:
    for id_plano, razao_social, nome_fantasia, descricao, cnpj in zip(range(1, len(razoes_sociais) + 1), razoes_sociais, nome_fantasia, descricoes, cnpjs):
        sql_command = (
            f"INSERT INTO T_RHSTU_PLANO_SAUDE (ID_PLANO_SAUDE, DS_RAZAO_SOCIAL, NM_FANTASIA_PLANO_SAUDE, DS_PLANO_SAUDE, NR_CNPJ, NM_CONTATO, DS_TELEFONE, DT_INICIO, DT_FIM, DT_CADASTRO, NM_USUARIO) "
            f"VALUES ({id_plano}, '{razao_social}', '{nome_fantasia}', '{descricao}', '{cnpj}', 'Contao', '1234-5678', TO_DATE('{generate_random_sql_date(2020, 2022)}', 'YYYY-MM-DD'), NULL, TO_DATE('{generate_random_sql_date(2020, 2022)}', 'YYYY-MM-DD'), USER);\n"
        )
        sqlfile.write(sql_command)
    sqlfile.write("COMMIT")
    sqlfile.close()