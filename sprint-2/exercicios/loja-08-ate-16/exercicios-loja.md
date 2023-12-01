# Exercícios Loja de 8 a 16

## Exercício 8

Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

## Resolução

```sql
SELECT
  tbvendedor.cdvdd,
  tbvendedor.nmvdd
FROM
  tbvendedor
JOIN
  tbvendas ON tbvendedor.cdvdd = tbvendas.cdvdd
WHERE
  tbvendas.status = 'Concluído'
GROUP BY
  tbvendedor.cdvdd, tbvendedor.nmvdd
ORDER BY
  COUNT(tbvendas.cdven) DESC
LIMIT 1;
```

---

## Exercício 9

Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

## Resolução

```sql
SELECT
  v.cdpro,
  MAX(v.nmpro) AS nmpro
FROM
  tbvendas v
WHERE
  v.dtven BETWEEN '2014-02-03' AND '2018-02-02'
  AND v.status = 'Concluído'
GROUP BY
  v.cdpro
ORDER BY
  COUNT(*) DESC
LIMIT 1;
```

---

## Exercício 10

A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído. As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

## Resolução

```sql
SELECT
    nmvdd AS vendedor,
    SUM(v.qtd * v.vrunt) AS valor_total_vendas,
    ROUND(SUM(v.qtd * v.vrunt) * ve.perccomissao / 100, 2) AS comissao
FROM
    tbvendas v
JOIN
    tbvendedor ve ON v.cdvdd = ve.cdvdd
WHERE
    v.status = 'Concluído'
GROUP BY
    v.cdvdd, ve.perccomissao
ORDER BY
    comissao DESC;
```

---

## Exercício 11

Apresente a query para listar o código e nome cliente com maior         v.status = 'Concluído'
    GROUP BY
        v.cdvdd
    HAVING
        total_sales > 0
)

SELECT
    d.cddep AS cddep,
    d.nmdep AS nmdep,
    d.dtnasc AS dtnasc,
    s.total_sales AS valor_total_vendas
FROM
    SellerTotalSales s
JOIN
    tbvendedor v ON s.seller_id = v.cdvdd
JOIN
    tbdependente d ON v.cdvdd = d.cdvdd
WHERE
    s.total_sales = (SELECT MIN(total_sales) FROM SellerTotalSales)
ORDER BY
    d.cddep;
```
gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

## Resolução

```sql
SELECT
    v.cdcli AS cdcli,
    v.nmcli AS nmcli,
    SUM(v.qtd * v.vrunt) AS gasto
FROM
    tbvendas v
WHERE
    v.status = 'Concluído'
GROUP BY
    v.cdcli, v.nmcli
ORDER BY
    gasto DESC
LIMIT 1;
```

---

## Exercício 12

Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.

> Observação: Apenas vendas com status concluído.

## Resolução

```sql
WITH SellerTotalSales AS (
    SELECT
        v.cdvdd AS seller_id,
        SUM(v.qtd * v.vrunt) AS total_sales
    FROM
        tbvendas v
    WHERE
```

---

## Exercício 13

Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

## Resolução

```sql
SELECT
    v.cdpro AS cdpro,
    v.nmcanalvendas AS nmcanalvendas,
    v.nmpro AS nmpro,
    SUM(v.qtd) AS quantidade_vendas
FROM
    tbvendas v
WHERE
    v.status = 'Concluído'
    AND v.nmcanalvendas IN ('Ecommerce', 'Matriz')
GROUP BY
    v.cdpro, v.nmcanalvendas, v.nmpro
ORDER BY
    quantidade_vendas
LIMIT 10;
```

---

## Exercício 14

Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

> Observação: Apenas vendas com status concluído.

## Resolução

```sql
SELECT
    estado,
    ROUND(AVG(qtd * vrunt), 2) AS gastomedio
FROM
    tbvendas
WHERE
    status = 'Concluído'
GROUP BY
    estado
ORDER BY
    gastomedio DESC;
```

---

## Exercício 15

Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.

## Resolução

```sql
SELECT
    cdven
FROM
    tbvendas
WHERE
    deletado = '1'
ORDER BY
    cdven ASC;
```

---

## Exercício 16

Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).

> Obs: Somente vendas concluídas.

## Resolução

```sql
SELECT
    estado,
    nmpro,
    ROUND(AVG(qtd), 4) AS quantidade_media
FROM
    tbvendas
WHERE
    status = 'Concluído'
GROUP BY
    estado, nmpro
ORDER BY
    estado, nmpro;
```