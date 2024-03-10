-- Criando as Tabelas usadas para as Dimensões e Fato

CREATE TABLE DimCliente (
  idCliente INTEGER NOT NULL PRIMARY KEY,
  nomeCliente VARCHAR(255) NOT NULL,
  cidadeCliente VARCHAR(255),
  estadoCliente VARCHAR(255),
  paisCliente VARCHAR(255)
);

CREATE TABLE DimCarro (
  idCarro INTEGER NOT NULL PRIMARY KEY,
  kmCarro INTEGER,
  classiCarro VARCHAR(255),
  marcaCarro VARCHAR(255),
  modeloCarro VARCHAR(255),
  anoCarro INTEGER,
  tipoCombustivel VARCHAR(255)
);

CREATE TABLE DimVendedor (
  idVendedor INTEGER NOT NULL PRIMARY KEY,
  nomeVendedor VARCHAR(255),
  sexoVendedor SMALLINT(1),
  estadoVendedor VARCHAR(255)
);

CREATE TABLE FatoLocacao (
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
  FOREIGN KEY (idCliente) REFERENCES DimCliente (idCliente),
  FOREIGN KEY (idCarro) REFERENCES DimCarro (idCarro),
  FOREIGN KEY (idVendedor) REFERENCES DimVendedor (idVendedor)
);

-- Inserts realizados para popular as tabelas com dados de teste das tabelas Cliente, Carro, Vendedor e Locacao

INSERT INTO DimCliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente FROM Cliente;
 
INSERT INTO DimCarro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, tipoCombustivel)
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, tipoCombustivel FROM Carro;

INSERT INTO DimVendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor FROM Vendedor;

INSERT INTO FatoLocacao (idLocacao, idCliente, idCarro, qtdDiaria, vlrDiaria, dataLocacao, horaLocacao, dataEntrega, horaEntrega, idVendedor)
SELECT idLocacao, idCliente, idCarro, qtdDiaria, vlrDiaria, dataLocacao, horaLocacao, dataEntrega, horaEntrega, idVendedor FROM Locacao;

-- Criando as Views para as Dimensões e Fato

CREATE VIEW VwFatoLocacao AS
SELECT
    FL.idLocacao,
    C.idCliente,
    CA.idCarro,
    V.idVendedor,
    FL.dataLocacao,
    FL.horaLocacao,
    FL.qtdDiaria,
    FL.vlrDiaria,
    FL.dataEntrega,
    FL.horaEntrega
FROM FatoLocacao fl 
JOIN DimCliente C ON FL.idCliente = C.idCliente
JOIN DimCarro CA ON FL.idCarro = CA.idCarro
JOIN DimVendedor V ON FL.idVendedor = V.idVendedor;

CREATE VIEW VwDimCliente AS
SELECT * FROM DimCliente;

CREATE VIEW VwDimCarro AS
SELECT * FROM DimCarro;

CREATE VIEW VwDimVendedor AS
SELECT * FROM DimVendedor;

-- Query para testar as Dimensões e Fato criados

SELECT 
  c.idCarro,
  c.marcaCarro,
  c.modeloCarro,
  COUNT(l.idLocacao) AS totalLocacoes
FROM 
  FatoLocacao l
JOIN 
  DimCarro c ON l.idCarro = c.idCarro
GROUP BY 
  c.idCarro, c.marcaCarro, c.modeloCarro
ORDER BY 
  totalLocacoes DESC;

| idCarro | marcaCarro | modeloCarro | totalLocacoes |
|---------|------------|-------------|---------------|
| 5       | Fiat       | Fiat Palio  | 5             |
| 2       | Fiat       | Fiat Uno    | 4             |
| 3       | Fiat       | Fiat Palio  | 4             |
| 4       | Fiat       | Fiat Palio  | 3             |
| 1       | Fiat       | Fiat Uno    | 2             |
| 6       | VW         | Fusca 78    | 1             |
| 7       | VW         | Fusca 78    | 1             |
| 10      | Fiat       | Fiat 147    | 1             |