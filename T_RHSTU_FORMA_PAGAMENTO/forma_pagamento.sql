INSERT INTO T_RHSTU_FORMA_PAGAMENTO (ID_FORMA_PAGTO, NM_FORMA_PAGTO, DS_FORMA_PAGTO, ST_FORMA_PAGTO, DT_CADASTRO, NM_USUARIO)
SELECT 1, 'Gratuito', 'Pagamento Gratuito', 'A', SYSDATE, USER FROM DUAL
UNION ALL
SELECT 2, 'Plano de saúde', 'Pagamento via Plano de Saúde', 'A', SYSDATE, USER FROM DUAL
UNION ALL
SELECT 3, 'Dinheiro', 'Pagamento em Dinheiro', 'A', SYSDATE, USER FROM DUAL
UNION ALL
SELECT 4, 'Cartão de Crédito', 'Pagamento com Cartão de Crédito', 'A', SYSDATE, USER FROM DUAL
UNION ALL
SELECT 5, 'Cartão de Débito', 'Pagamento com Cartão de Débito', 'A', SYSDATE, USER FROM DUAL
UNION ALL
SELECT 6, 'Pix', 'Pagamento via Pix', 'A', SYSDATE, USER FROM DUAL;
COMMIT