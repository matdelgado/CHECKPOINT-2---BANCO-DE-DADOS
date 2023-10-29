INSERT INTO T_RHSTU_TIPO_CONTATO (ID_TIPO_CONTATO, NM_TIPO_CONTATO, DT_INICIO, DT_FIM, DT_CADASTRO, NM_USUARIO)
SELECT 1, 'Pai', SYSDATE, NULL, SYSDATE, USER FROM DUAL
UNION ALL
SELECT 2, 'Mãe', SYSDATE, NULL, SYSDATE, USER FROM DUAL
UNION ALL
SELECT 3, 'Esposa', SYSDATE, NULL, SYSDATE, USER FROM DUAL
UNION ALL
SELECT 4, 'Primo', SYSDATE, NULL, SYSDATE, USER FROM DUAL
UNION ALL
SELECT 5, 'Prima', SYSDATE, NULL, SYSDATE, USER FROM DUAL
UNION ALL
SELECT 6, 'Outros contatos', SYSDATE, NULL, SYSDATE, USER FROM DUAL;
COMMIT