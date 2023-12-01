# Exercícios Biblioteca de 1 a 7

## Exercício 1

Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.
Atenção às colunas esperadas no resultado final: **cod, titulo, autor, editora, valor, publicacao, edicao, idioma**

## Resolução

```sql
SELECT * FROM livro
WHERE publicacao > '2014-12-31'
ORDER BY cod;
```

---

## Exercício 2

Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  
Atenção às colunas esperadas no resultado final:  **titulo, valor**

## Resolução

```sql
SELECT titulo, valor
FROM livro
ORDER BY valor DESC
LIMIT 10;
```

---

## Exercício 3

Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas: **quantidade, nome, estado e cidade**. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

## Resolução

```sql
SELECT
  COUNT(livro.cod) AS quantidade,
  editora.nome,
  endereco.estado,
  endereco.cidade
FROM
  livro
INNER JOIN editora ON livro.editora = editora.codeditora
INNER JOIN endereco ON editora.endereco = endereco.codendereco
GROUP BY
  editora.codeditora
ORDER BY
  quantidade DESC
LIMIT 5;
```

---

## Exercício 4

Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna **nome** (autor), em ordem crescente. Além desta, apresentar as colunas **codautor, nascimento e quantidade** (total de livros de sua autoria).

## Resolução

```sql
SELECT
  autor.codautor,
  autor.nome,
  autor.nascimento,
  COUNT(livro.cod) AS quantidade
FROM
  autor
LEFT JOIN livro ON autor.codautor = livro.autor
GROUP BY
  autor.codautor
ORDER BY
  autor.nome ASC;
```

---

## Exercício 5

Apresente a query para listar o **nome** dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil.
Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

## Resolução

```sql
SELECT 
    DISTINCT autor.nome
FROM 
    autor
INNER JOIN 
    livro ON autor.codautor = livro.autor
INNER JOIN 
    editora ON livro.editora = editora.codeditora
INNER JOIN 
    endereco ON editora.endereco = endereco.codendereco
WHERE 
    endereco.estado NOT IN ('RIO GRANDE DO SUL', 'SANTA CATARINA', 'PARANÁ')
ORDER BY autor.nome ASC;
```

---

## Exercício 6

Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas **codautor, nome, quantidade_publicacoes**

## Resolução

```sql
SELECT
  autor.codautor,
  autor.nome,
  COUNT(livro.cod) AS quantidade_publicacoes
FROM
  autor
LEFT JOIN livro ON autor.codautor = livro.autor
GROUP BY
  autor.codautor, autor.nome
ORDER BY
  quantidade_publicacoes DESC
LIMIT 1;
```

---

## Exercício 7

Apresente a query para listar o **nome** dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

## Resolução

```sql
SELECT
  autor.nome
FROM
  autor
LEFT JOIN livro ON autor.codautor = livro.autor
WHERE
  livro.cod IS NULL
ORDER BY
  autor.nome ASC;
```