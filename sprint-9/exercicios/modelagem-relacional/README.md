# Exercicío 1: Modelagem Relacional

## Normalização da Tabela tb_locacao

Esse README descreve o processo de normalização da tabela tb_locacao, incluindo as motivações para a normalização, os passos realizados para atingir o resultado final e o diagrama resultante do banco de dados normalizado.

## Motivações para a Normalização:

- **Redundância de Dados**: A presença de dados duplicados levava a problemas de integridade e consistência.
  
- **Anomalias de Atualização**: A redundância de dados poderia resultar em anomalias durante as atualizações.

- **Dificuldade de Manutenção**: A complexidade e a redundância dos dados dificultavam a manutenção e a garantia de consistência.

## Passos para a Normalização

### 1. Análise da Tabela Original

O primeiro passo é analisar a estrutura da tabela tb_locacao e identificar as dependências funcionais entre os atributos e como podemos fazer para desacoplar essa tabela em tabelas menores.

<div align=center>
      <img width=300px src="01-tb_locacao.png">
</div>

### 2. Identificação das Entidades

Apos algumas analises, eu pude identificar as entidades distintas presentes na tabela, como Cliente, Carro, Combustivel, Vendedor e Locação.

#### Motivos por trás da escolha e separação dessas novas entidades:

- **Dependências Funcionais:** Existe uma dependência Funcional entre os atributos da tabela, identificando conjuntos de atributos que determinam outros atributos. Por exemplo, os atributos relacionados aos carros (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro) dependem diretamente do identificador único do carro.

- **Repetição de Informações:** Levamos em consideração a repetição de informações na tabela, identificando conjuntos de atributos que são frequentemente repetidos em múltiplas linhas. Por exemplo, as informações dos vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) são repetidas para cada locação realizada.

### 3. Criação de Tabelas Normalizadas

Criei as tabelas separadas para cada entidade e fiz as relações com a chave estrangeira, removendo as redundâncias e garantindo a integridade dos dados.

#### Script para a criação das novas tabelas:

```sql
-- Tabelas resultantes após a normalização da tabela tb_locacao

CREATE TABLE Cliente (
  idCliente INTEGER NOT NULL PRIMARY KEY,
  nomeCliente VARCHAR(255) NOT NULL,
  cidadeCliente VARCHAR(255),
  estadoCliente VARCHAR(255),
  paisCliente VARCHAR(255)
);

CREATE TABLE Carro (
  idCarro INTEGER NOT NULL PRIMARY KEY,
  kmCarro INTEGER,
  classiCarro VARCHAR(255),
  marcaCarro VARCHAR(255),
  modeloCarro VARCHAR(255),
  anoCarro INTEGER,
  idcombustivel INTEGER NOT NULL,
  tipoCombustivel VARCHAR(255),
  FOREIGN KEY (idcombustivel) REFERENCES Combustivel (idcombustivel)
);

CREATE TABLE Locacao (
  idLocacao INTEGER NOT NULL PRIMARY KEY,
  idCliente INTEGER NOT NULL,
  idCarro INTEGER NOT NULL,
  qtdDiaria INTEGER,
  vlrDiaria DECIMAL,
  dataLocacao DATE,
  horaLocacao TIME,
  dataEntrega DATE,
  horaEntrega TIME,
  idVendedor INTEGER,
  FOREIGN KEY (idCliente) REFERENCES Cliente (idCliente),
  FOREIGN KEY (idCarro) REFERENCES Carro (idCarro),
  FOREIGN KEY (idVendedor) REFERENCES Vendedor (idVendedor)
);

CREATE TABLE Combustivel (
  idcombustivel INTEGER NOT NULL PRIMARY KEY,
  tipoCombustivel VARCHAR(255)
);

CREATE TABLE Vendedor (
  idVendedor INTEGER NOT NULL PRIMARY KEY,
  nomeVendedor VARCHAR(255),
  sexoVendedor SMALLINT(1),
  estadoVendedor VARCHAR(255)
);
```

### 4. Inserir Dados Normalizados

Após a criação da estrutura normalizada, agora irei inserir os dados correspondentes em cada tabela normalizada, utilizando as cláusulas `INSERT` e `INSERT OR IGNORE` para evitar duplicatas ou violações de chave primária.

#### Script para a inserção dos dados:

```sql
-- Inserts realizados para popular as tabelas com os dados da tabela tb_locacao

INSERT INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

INSERT OR IGNORE INTO Carro (kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel, tipoCombustivel)
SELECT DISTINCT kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel, tipoCombustivel
FROM tb_locacao;

INSERT OR IGNORE INTO Combustivel (idcombustivel, tipoCombustivel)
SELECT DISTINCT idcombustivel, tipoCombustivel
FROM tb_locacao;

INSERT OR IGNORE INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

INSERT INTO Locacao (idLocacao, idCliente, idCarro, qtdDiaria, vlrDiaria, dataLocacao, horaLocacao, dataEntrega, horaEntrega, idVendedor)
SELECT DISTINCT idLocacao, idCliente, idCarro, qtdDiaria, vlrDiaria, dataLocacao, horaLocacao, dataEntrega, horaEntrega, idVendedor
FROM tb_locacao;
```

## Estrutura do Banco de Dados Normalizado

A estrutura resultante do banco de dados normalizado consiste em várias tabelas separadas para cada entidade identificada, com chaves estrangeiras estabelecendo as relações entre elas.

### Modelo Normalizado:

<div align=center>
      <img width=400px src="04-diagrama-ER-normalizado.png">
</div>

### Query teste:

```sql
-- Query para testar as tabelas após a normalização da tabela tb_locacao

SELECT 
    l.idLocacao,
    c.nomeCliente,
    ca.marcaCarro,
    ca.modeloCarro,
    co.tipoCombustivel,
    l.dataLocacao,
    l.horaLocacao,
    l.dataEntrega,
    l.horaEntrega,
    v.nomeVendedor
FROM Locacao l
JOIN Cliente c ON l.idCliente = c.idCliente
JOIN Carro ca ON l.idCarro = ca.idCarro
JOIN Combustivel co ON ca.idcombustivel = co.idcombustivel
JOIN Vendedor v ON l.idVendedor = v.idVendedor;
```

#### Resultado

| idLocacao | nomeCliente | marcaCarro | modeloCarro | tipoCombustivel | dataLocacao | horaLocacao | dataEntrega | horaEntrega | nomeVendedor |
|----|-----------------|----------------|-----------------|---------------------|-----------------|-----------------|-----------------|-----------------|------------------|
| 6  | Cliente seis    | Fiat | Fiat Palio | Gasolina | 20160302 | 14:00 | 20160312 | 14:00 | Vendedora oito |
| 7  | Cliente seis    | Fiat | Fiat Palio | Gasolina | 20160802 | 14:00 | 20160812 | 14:00 | Vendedora oito |
| 8  | Cliente quatro  | Fiat | Fiat Palio | Gasolina | 20170102 | 18:00 | 20170112 | 18:00 | Vendedora seis |
| 9  | Cliente quatro  | Fiat | Fiat Palio | Gasolina | 20180102 | 18:00 | 20180112 | 18:00 | Vendedora seis |
| 10 | Cliente dez     | Fiat | Fiat 147 | Gasolina | 20180302 | 18:00 | 20180312 | 18:00 | Vendedor dezesseis |
| 11 | Cliente vinte   | VW | Fusca 78 | Gasolina | 20180401 | 11:00 | 20180411 | 11:00 | Vendedor dezesseis |
| 12 | Cliente vinte   | VW | Fusca 78 | Gasolina | 20200401 | 11:00 | 20200411 | 11:00 | Vendedor dezesseis |
| 13 | Cliente vinte e dois | Fiat | Fiat Uno | Gasolina | 20220501 | 8:00 | 20220521 | 18:00 | Vendedor trinta |
| 14 | Cliente vinte e dois | Fiat | Fiat Uno | Gasolina | 20220601 | 8:00 | 20220621 | 18:00 | Vendedor trinta |
| 15 | Cliente vinte e dois | Fiat | Fiat Uno | Gasolina | 20220701 | 8:00 | 20220721 | 18:00 | Vendedor trinta |
| 16 | Cliente vinte e dois | Fiat | Fiat Uno | Gasolina | 20220801 | 8:00 | 20220721 | 18:00 | Vendedor trinta |
| 17 | Cliente vinte e tres | Fiat | Fiat Palio | Gasolina | 20220901 | 8:00 | 20220921 | 18:00 | Vendedor trinta e um |
| 18 | Cliente vinte e tres | Fiat | Fiat Palio | Gasolina | 20221001 | 8:00 | 20221021 | 18:00 | Vendedor trinta e um |
| 19 | Cliente vinte e tres | Fiat | Fiat Palio | Gasolina | 20221101 | 8:00 | 20221121 | 18:00 | Vendedor trinta e um |
| 20 | Cliente cinco   | Fiat | Fiat Uno | Gasolina | 20230102 | 18:00 | 20230112 | 18:00 | Vendedor dezesseis |
| 21 | Cliente cinco   | Fiat | Fiat Uno | Gasolina | 20230115 | 18:00 | 20230125 | 18:00 | Vendedor dezesseis |
| 22 | Cliente vinte e seis | Fiat | Fiat Palio | Gasolina | 20230125 | 8:00 | 20230130 | 18:00 | Vendedora trinta e dois |
| 23 | Cliente vinte e seis | Fiat | Fiat Palio | Gasolina | 20230131 | 8:00 | 20230205 | 18:00 | Vendedora trinta e dois |
| 24 | Cliente vinte e seis | Fiat | Fiat Palio | Gasolina | 20230206 | 8:00 | 20230211 | 18:00 | Vendedora trinta e dois |
| 25 | Cliente vinte e seis | Fiat | Fiat Palio | Gasolina | 20230212 | 8:00 | 20230217 | 18:00 | Vendedora trinta e dois |
| 26 | Cliente vinte e seis | Fiat | Fiat Palio | Gasolina | 20230218 | 8:00 | 20230219 | 18:00 | Vendedora trinta e dois |