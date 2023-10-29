from datetime import datetime
import oracledb
from datetime import datetime, timedelta
import requests
from itertools import combinations
 
def buscar_dados(estado, cidade):
    try:
        request = requests.get(f"https://viacep.com.br/ws/{estado}/{cidade}/a+a/json/")
        request.raise_for_status()  # Lança uma exceção para códigos de status HTTP diferentes de 200
        return request.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

def filter_enderecos(data):
    result = []
    quantidade = 0
    
    # Filtra os dados para incluir apenas objetos com "bairro" preenchido
    data_com_bairro = [entry for entry in data if "bairro" in entry and entry["bairro"]]
    
    # Agrupa os dados por bairro
    grouped_data = {bairro: [entry for entry in data_com_bairro if entry["bairro"] == bairro] for bairro in set(entry["bairro"] for entry in data_com_bairro)}
 
    for bairro, bairro_data in grouped_data.items():
        # Garante que há pelo menos dois CEPs para o mesmo bairro
        if len(bairro_data) >= 2:
            # Adiciona dois objetos com o mesmo bairro e CEPs diferentes
            result.extend(bairro_data[:2])
            quantidade += 1
            if quantidade == 2:
                break
        else:
            result.extend(bairro_data[:1])
 
    return result

conn = oracledb.connect(user='', password='',
                        dsn='oracle.fiap.com.br/orcl')
 
# RECUPERANDO CIDADES EXISTENTES NO BANCO DE DADOS
cursor = conn.cursor()
cursor.execute("SELECT C.ID_CIDADE, C.NM_CIDADE, E.SG_ESTADO FROM T_RHSTU_CIDADE C JOIN T_RHSTU_ESTADO E ON E.ID_ESTADO = C.ID_ESTADO ORDER BY C.ID_CIDADE")
cidades = [row for row in cursor.fetchall()]
cursor.close()
conn.close()
 
with open('gera-enderecos2.sql', 'w', encoding='utf-8') as sql_file:
    id_bairro = 0
    id_logradouro = 0
    for cidade in cidades:
        idCidade, nmCidade, sgEstado = cidade
 
        lista_enderecos = buscar_dados(sgEstado, nmCidade)
        lista_enderecos = filter_enderecos(lista_enderecos)
 
        bairro_atual = " "
 
        for endereco in lista_enderecos:
            if endereco['bairro'] != bairro_atual:
                id_bairro += 1
                insert_statement = "INSERT INTO T_RHSTU_BAIRRO (ID_BAIRRO, ID_CIDADE, NM_BAIRRO, NM_ZONA_BAIRRO, DT_CADASTRO, NM_USUARIO) VALUES ({}, {}, '{}', 'CENTRO', SYSDATE, {});\n".format(id_bairro, idCidade, endereco['bairro'].replace("'", ""), USER)
                sql_file.write(insert_statement)
 
            id_logradouro += 1
            insert_statement = f"INSERT INTO T_RHSTU_LOGRADOURO (ID_LOGRADOURO, ID_BAIRRO, NM_LOGRADOURO, NR_CEP, DT_CADASTRO, NM_USUARIO) VALUES ({id_logradouro}, {id_bairro}, '{endereco['logradouro']}', '{endereco['cep'].replace('-', '')}', SYSDATE, USER);\n"
            sql_file.write(insert_statement)
 
            bairro_atual = endereco['bairro']
