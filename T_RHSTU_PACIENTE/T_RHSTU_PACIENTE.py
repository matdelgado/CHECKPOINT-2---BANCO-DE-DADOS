from datetime import datetime
import random
import multiprocessing
import time

nomes = [
    'Joao', 'Mateo', 'Leonardo', 'Hugo', 'Miguel', 'Enzo', 'Theo', 'Pedro', 'Fernando', 'Gabriel',
    'Ricardo', 'Renato', 'Bruno', 'Marco', 'Geraldo', 'Marcelo', 'Flavio', 'Artur', 'Alfredo',
    'Sofia', 'Isabela', 'Julia', 'Clara', 'Beatriz', 'Maria', 'Luisa', 'Helena', 'Livia', 'Laura',
    'Rafaela', 'Anita', 'Bruna', 'Roberta', 'Flavia', 'Carolina', 'Amanda', 'Gabriela', 'Mariana', 'Ana'
]

mid_nome = ['Thornton', 'Salazar', 'Haynes', 'Blankenship', 'Huerta', 'Lawrence', 'Mitchell', 'Doyle', 'Aguirre', 'Hughes', 'Schwartz', 'Vazquez', 'Walsh', 'Hicks', 'Banks', 'Bradley', 'Johnston', 'Hebert', 'Lucero', 'Preston', 'Murray', 'Mccormick', 'Murillo', 'Knox', 'Cantrell', 'Dorsey', 'Velazquez', 'Villegas', 'Hughes', 'Guerra', 'Weber', 'Solomon', 'Watts', 'Frank', 'Dudley', 'Houston', 'Russo', 'Combs', 'Bonilla', 'Lang', 'Mathews', 'Hunter', 'Logan', 'Garrison', 'Webb', 'Erickson',
            'Bradley', 'Raymond', 'Petroni', 'Boris', 'Estrulo', 'Revollo', 'Delgado', 'Oriene', 'Bombomnati', 'Fibonatti', 'Calsnari', 'Ronqui', 'Yamamoto', 'Izuki', 'Kamikaze', 'Kalui',	'Kailane', 'Zampar', 'Camillis', 'Pedrolo', 'Bortolotto', 'Bortoluzzi', 'Paldikast', 'Cordeio', 'Polo', 'Dellosso', 'Maluf', 'Baltar', 'Cavichili', 'Ferrari', 'Arnoni', 'Bertolucci', 'Durex', "Gibson", "Mcdonald", "Cruz", "Marshall", "Ortiz", "Gomez", "Freeman", "Wells", "Simpson", "Stevens", "Tucker", "Porter"]

last_nome = [
    "Almeida", "Peregrino", "Fonseca", "Santana", "Borges", "Ribeira", "Carreira", "Cruz", "Machado", "Lobato",
    "Figueiredo", "Brito", "Albuquerque", "Montenegro", "Ferraz", "Dantas", "Queiros", "Cavalcanti", "Vargas",
    "Lemos", "Lins", "Vasconcelos", "Paes", "Rocha", "Pimenta", "Sa", "Andrade", "Mesquita", "Coutinho",
    "Barros", "Guedes", "Magalhaes", "Goulart", "Peixoto", "Aragao", "Siqueira", "Azevedo", "Tavares", "Amaral",
    "Pimentel", "Fernandez", "Ramirez", "Villanueva", "Gomez", "Lopez", "Martinez", "Rodriguez", "Chavez",
    "Mendoza", "Soto", "Garcia", "Perez", "Torres", "Ortega", "Hernandez", "Ruiz", "Ferrer", "Gonzalez", "Lara",
    "Alonso", "Jimenez", "Vega", "Gutierrez", "Sanchez", "Flores", "Gomez", "Moreno", "Ramos", "Villa", "Hidalgo",
    "Castillo", "Navarro", "Molina", "Fernando", "Dominguez", "Ponce", "Lugo", "Camacho", "Escobar",
    "Reyes", "Ortiz", "Iglesias", "Fuentes", "Cordova", "Guillen", "Sosa", "Pinto", "Roque", "Alarcon",
    "Paredes", "Herrera", "Velasquez", "Estrada", "Solis", "Bernal", "Campos", "Rosales", "Aguilar", "Cabrera",
    "Figueroa", "Gallegos", "Vasquez", "Serrano", "Cisneros", "Landa", "Laguna", "Cruz", "Carvajal", "Parra", "Smith", "Johnson", "Brown", "Taylor", "Anderson", "Williams", "Jones", "Miller", "Davis", "Garcia", "Rodriguez",
    "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin",
    "Thompson", "Young", "Clark", "Hall", "Allen", "Lewis", "Scott", "Hill", "Green", "Adams", "Baker", "Nelson",
    "Carter", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins",
    "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey", "Rivera", "Cooper",
    "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly",
    "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long",
    "Patterson", "Flores", "Washington", "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander",
    "Russell", "Griffin", "Diaz", "Hayes", "Myers", "Ford", "Hamilton", "Graham", "Sullivan", "Wallace", "Woods", "Cole",
    "West", "Jordan", "Owens", "Reynolds", "Fisher", "Ellis", "Harrison"
]


cpf_set = set()
rg_set = set()

# Função para gerar CPF
def gerar_cpf():
    while True:
        cpf_parcial = [str(random.randint(0, 9)) for _ in range(9)]
        cpf = ''.join(cpf_parcial)
        cpf += calcular_digito(cpf)
        cpf += calcular_digito(cpf)
        if cpf not in cpf_set:
            cpf_set.add(cpf)
            return cpf
# Função para gerar RG
def gerar_rg():
    while True:
        rg_parcial = [str(random.randint(0, 9)) for _ in range(8)]
        soma = sum(int(digito) * (9 - i) for i, digito in enumerate(rg_parcial))
        resto = soma % 11
        digito_verificador = 0 if resto == 10 else resto
        rg = ''.join(rg_parcial) + str(digito_verificador)
        
        if rg not in rg_set:
            rg_set.add(rg)
            return rg
        
# Função para calcular o dígito de verificação do CPF
def calcular_digito(cpf):
    soma = 0
    for i, peso in enumerate(range(10, 1, -1)):
        soma += int(cpf[i]) * peso
    resto = soma % 11
    if resto < 2:
        digito = 0
    else:
        digito = 11 - resto
    return str(digito)

# Função para gerar um registro
def gerar_registro(id_paciente):
    nm_paciente = random.choice(nomes) + ' ' + random.choice(mid_nome) + ' ' + random.choice(last_nome)
    nr_cpf = gerar_cpf()
    nm_rg = gerar_rg()
    return f"INSERT INTO T_RHSTU_PACIENTE (ID_PACIENTE, NM_PACIENTE, NR_CPF, NM_RG) VALUES ({id_paciente}, '{nm_paciente}', '{nr_cpf}', '{nm_rg}');"

# Função para gerar registros em paralelo
def gerar_registros_em_paralelo(num_registros):
    num_cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(num_cores)
    registros = pool.map(gerar_registro, range(1, num_registros + 1))
    pool.close()
    pool.join()
    return registros

# Função para gerar sexo com base no nome
def gerar_sexo(nome):
    if nome[-1].lower() == 'o':
        return 'M'
    elif nome[-1].lower() == 'a':
        return 'F'
    else:
        return 'I'

# Função para gerar escolaridade
def gerar_escolaridade():
    opções = [
        "Analfabeto", "1 grau completo", "2 grau completo",
        "1 grau cursando", "2 grau cursando", "3 grau cursando", "3 grau completo"
    ]
    return random.choice(opções)

# Função para gerar estado civil
def gerar_estado_civil():
    opções = ["Solteiro(a)", "Casado(a)", "Namorando", "Viuvo(a)"]
    return random.choice(opções)

# Função para gerar grupo sanguíneo
tipos_sanguíneos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
def gerar_grupo_sanguineo():
    return random.choice(tipos_sanguíneos)

# Função para gerar altura
def gerar_altura():
    altura = round(random.uniform(1.4, 2.1), 2)
    return f"{altura:.2f}"

# Função para gerar peso
def gerar_peso():
    peso = round(random.uniform(35.1, 150.0), 1)
    return f"{peso:.1f}"

# Função para gerar data de nascimento
def gerar_data_nascimento():
    ano = random.randint(1930, 2022)
    mes = random.randint(1, 12)
    dia = random.randint(1, 28)  # Limitando a 28 para evitar datas inválidas
    return f"{ano:04d}-{mes:02d}-{dia:02d}"


# Grava os registros em um arquivo SQL
def gerar_registro_paciente(id_paciente):
    nome_completo = random.choice(nomes) + ' ' + random.choice(mid_nome) + ' ' + random.choice(last_nome)
    nr_cpf = gerar_cpf()
    nm_rg = gerar_rg()
    dt_nascimento = gerar_data_nascimento()
    fl_sexo_biologico = gerar_sexo(nome_completo)
    ds_escolaridade = gerar_escolaridade()
    ds_estado_civil = gerar_estado_civil()
    nm_grupo_sanguineo = gerar_grupo_sanguineo()
    nr_altura = gerar_altura()
    nr_peso = gerar_peso()
    
    return (
        f"INSERT INTO T_RHSTU_PACIENTE (ID_PACIENTE, NM_PACIENTE, NR_CPF, NM_RG, DT_NASCIMENTO, FL_SEXO_BIOLOGICO, "
        f"DS_ESCOLARIDADE, DS_ESTADO_CIVIL, NM_GRUPO_SANGUINEO, NR_ALTURA, NR_PESO, DT_CADASTRO, NM_USUARIO) "
        f"VALUES ({id_paciente}, '{nome_completo}', '{nr_cpf}', '{nm_rg}', TO_DATE('{dt_nascimento}', 'YYYY-MM-DD'), "
        f"'{fl_sexo_biologico}', '{ds_escolaridade}', '{ds_estado_civil}', '{nm_grupo_sanguineo}', {nr_altura}, {nr_peso}, SYSDATE, USER);"
    )

num_registros = 1000000
start_time = time.time()

with open('script.sql', 'w') as sqlfile:
    for i in range(num_registros):
        registro = gerar_registro_paciente(i + 1)
        sqlfile.write(registro + '\n')
        if (i + 1) % 10000 == 0:
            sqlfile.write("COMMIT;\n")
        print(i)
    sqlfile.write("COMMIT;\n")
end_time = time.time()
print(f"Arquivo gerado com sucesso. Tempo total de execução: {end_time - start_time} segundos")

