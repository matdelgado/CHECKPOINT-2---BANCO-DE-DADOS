import random

cargos_hospital = [
    "Médico",
    "Enfermeiro",
    "Técnico de Enfermagem",
    "Fisioterapeuta",
    "Farmacêutico",
    "Recepcionista",
    "Administrador Hospitalar",
    "Assistente Social",
    "Nutricionista",
    "Psicólogo",
    "Motorista de Ambulância",
    "Técnico de Radiologia",
    "Auxiliar de Limpeza",
    "Segurança",
    "Auxiliar Administrativo",
    "Técnico de Laboratório",
    "Fonoaudiólogo",
    "Terapeuta Ocupacional",
    "Coordenador de Enfermagem",
    "Auxiliar de Farmácia"
]

descricoes_cargos = [
    "Atende pacientes e realiza diagnósticos e tratamentos médicos.",
    "Cuida dos pacientes e auxilia nos procedimentos médicos.",
    "Assiste os enfermeiros e cuida dos pacientes.",
    "Realiza tratamentos de fisioterapia para os pacientes.",
    "Gerencia os medicamentos e auxilia na farmácia.",
    "Atende e auxilia pacientes na recepção.",
    "Gerencia as operações do hospital.",
    "Oferece suporte e assistência social aos pacientes.",
    "Elabora planos de nutrição para pacientes.",
    "Oferece suporte psicológico aos pacientes.",
    "Transporta pacientes com ambulâncias.",
    "Opera máquinas de raio-X e outros equipamentos de imagem.",
    "Mantém a limpeza e higiene do hospital.",
    "Garante a segurança das instalações e dos pacientes.",
    "Auxilia nas tarefas administrativas do hospital.",
    "Realiza exames laboratoriais e analisa amostras.",
    "Trabalha com problemas de fala e linguagem.",
    "Ajuda pacientes a recuperar habilidades cotidianas.",
    "Coordena as equipes de enfermagem.",
    "Auxilia na gestão dos medicamentos e estoque."
]

def gerar_data_nascimento():
    ano = random.randint(1930, 2022)
    mes = random.randint(1, 12)
    dia = random.randint(1, 28)  
    return f"{ano:04d}-{mes:02d}-{dia:02d}"

def gerar_salario(max_desvio_percentual=10):
    salario_minimo = 1350.00  # Salário mínimo padrão
    desvio_percentual = random.uniform(-max_desvio_percentual, max_desvio_percentual)
    salario = salario_minimo + (salario_minimo * desvio_percentual / 100)

    return salario

def gerar_rg():
    rg_parcial = [str(random.randint(0, 9)) for _ in range(8)]
    soma = sum(int(digito) * (9 - i) for i, digito in enumerate(rg_parcial))
    resto = soma % 11
    digito_verificador = 0 if resto == 10 else resto
    return ''.join(rg_parcial) + str(digito_verificador)


def gerar_cpf():
    def calcular_digito(cpf_parcial):
        total = 0
        for i, digito in enumerate(cpf_parcial):
            total += int(digito) * (len(cpf_parcial) + 1 - i)
        digito = 11 - (total % 11)
        return str(digito) if digito < 10 else '0'

    cpf_parcial = [str(random.randint(0, 9)) for _ in range(9)]
    cpf = ''.join(cpf_parcial)
    cpf += calcular_digito(cpf)
    cpf += calcular_digito(cpf)
    return int(cpf)

def obter_status_cargo():
    status = "Ativo"  
    return status

with open("T_RHSTU_FUNCIONARIO/inserir_funcionarios.sql", "w") as sqlfile:
    cont = 0
    for id_funcionario in range(1, 100001):
        if id_funcionario <= 10000:
            cargo = "Médico"
        elif id_funcionario <= 12000:
            cargo = "Motorista de Ambulância"
        else:
            cargo = random.choice(cargos_hospital)
            
        id_superior = random.randint(1, id_funcionario - 1) if id_funcionario > 1 else 0
        nm_func = f"Funcionário {id_funcionario}"
        ds_cargo = cargo
        dt_nascimento = gerar_data_nascimento()
        vl_salario = gerar_salario()
        nr_rg = gerar_rg()
        nr_cpf = gerar_cpf()
        st_func = obter_status_cargo()
        
        sql_command = (
            f"INSERT INTO T_RHSTU_FUNCIONARIO (ID_FUNC, ID_SUPERIOR, NM_FUNC, DS_CARGO, DT_NASCIMENTO, VL_SALARIO, NR_RG, NR_CPF, ST_FUNC, DT_CADASTRO, NM_USUARIO) "
            f"VALUES ({id_funcionario}, {id_superior}, '{nm_func}', '{ds_cargo}', TO_DATE('{dt_nascimento}', 'YYYY-MM-DD'), {vl_salario}, '{nr_rg}', {nr_cpf}, '{st_func}', SYSDATE, USER);\n"
        )
        sqlfile.write(sql_command)

        if cont == 1000:
            sqlfile.write("COMMIT;\n")
            cont = 0
        else:
            cont += 1
    sqlfile.write("COMMIT;")