UPDATE t_rhstu_telefone_paciente 
    SET NR_TELEFONE = 945442345,
        NR_DDD = 11
WHERE ID_PACIENTE = 1;

UPDATE t_rhstu_paciente
    SET nm_paciente = 'Denden Lindo',
    nr_cpf = 54878232862
WHERE id_paciente = 25;

UPDATE t_rhstu_medicamento 
    SET ds_detalhada_medicamento = 'Zeranixpate e usado para problemas de Dor de estomago de grau leve'
WHERE nm_medicamento = Zeranixpate;


UPDATE t_rhstu_email_paciente
    SET DS_EMAIL = 'XaolinMatadorDePorco@gmail.com',
    TP_EMAIL = 'I'
WHERE ds_email = 'flavia5490@outlook.com';

UPDATE t_rhstu_unid_hospitalar
    SET nm_unid_hospitalar = 'Hospital dos olhos',
    nm_razao_social_unid_hosp = 'Clinica de Olhos'
WHERE id_unid_hospital = 2;
