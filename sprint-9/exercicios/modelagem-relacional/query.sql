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

-- Query para testar as tabelas após a normização da tabela tb_locacao

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

