CREATE TABLE DimensaoFilme (
    id INT PRIMARY KEY,
    title VARCHAR(255)
);

CREATE TABLE DimensaoAtorPrincipal (
    id INT PRIMARY KEY,
    main_actor VARCHAR(255)
);

CREATE TABLE DimensaoDiretor (
    id INT PRIMARY KEY,
    director VARCHAR(255)
);

CREATE TABLE DimensaoDataLancamento (
    id INT PRIMARY KEY,
    release_date DATE
);

CREATE TABLE DimensaoOrcamento (
    id INT PRIMARY KEY,
    budget DECIMAL(15, 2)
);

CREATE TABLE DimensaoReceita (
    id INT PRIMARY KEY,
    revenue DECIMAL(15, 2)
);

CREATE TABLE FatoVotacaoFilme (
    id INT PRIMARY KEY,
    vote_average DECIMAL(3, 2),
    vote_count INT,
    filme_id INT,
    ator_principal_id INT,
    diretor_id INT,
    data_lancamento_id INT,
    orcamento_id INT,
    receita_id INT,
    FOREIGN KEY (filme_id) REFERENCES DimensaoFilme(id),
    FOREIGN KEY (ator_principal_id) REFERENCES DimensaoAtorPrincipal(id),
    FOREIGN KEY (diretor_id) REFERENCES DimensaoDiretor(id),
    FOREIGN KEY (data_lancamento_id) REFERENCES DimensaoDataLancamento(id),
    FOREIGN KEY (orcamento_id) REFERENCES DimensaoOrcamento(id),
    FOREIGN KEY (receita_id) REFERENCES DimensaoReceita(id)
);