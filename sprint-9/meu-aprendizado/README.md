# Modelagem de Dados

A modelagem de dados baseia-se na teoria de conjuntos (álgebra relacional), onde a localização ou formato dos dados é irrelevante para o usuário final. Envolve a representação de dados por meio de uma coleção de tabelas (entidade/relação), consistindo em conjuntos de linhas (tuplas) e uma lista de valores de atributos.

## Modelo Relacional:

Proposto por Peter P. Chen, o modelo entidade-relacionamento descreve o mundo como cheio de entidades que possuem características próprias e se relacionam entre si. Esse modelo é dividido em três partes: o mundo está cheio de coisas, que possuem características próprias e se relacionam entre si.

## Objeto de Dados ou Entidade:

Representa um componente do mundo real sobre o qual desejamos armazenar informações. Pode ser tangível ou intangível e é definido como algo que produz ou consome informações.

## Atributo:

Propriedades particulares que descrevem uma entidade, como nome, idade ou endereço. Os atributos podem ser simples ou compostos, monovalorados ou multivalorados, e podem ser derivados de outros atributos.

## Relacionamento:

Associação entre entidades, representado por verbos que indicam a relação entre elas. Pode ser classificado como um-para-um, um-para-muitos ou muitos-para-muitos, com base em sua cardinalidade.

## Tipos de Modelos de Dados:

1. **Modelo Conceitual:** Representa o mais alto nível de abstração e está próximo da realidade dos usuários.
2. **Modelo Lógico:** Descreve como os dados serão armazenados no banco e seus relacionamentos, adotando alguma tecnologia como SQL, NoSQL, entre outros.
3. **Modelo Físico:** Descreve como os dados serão armazenados fisicamente em um sistema de gerenciamento de banco de dados.

## Normalização:

É um processo formal que examina os atributos de uma entidade para evitar anomalias na inclusão, exclusão e alteração de dados. Envolve a organização dos dados em formas normais, como a Primeira Forma Normal (1FN), Segunda Forma Normal (2FN) e Terceira Forma Normal (3FN), visando preservar a integridade dos dados, gerar estabilidade para o modelo e eliminar redundâncias.




































# Exercícios

## Índice

- [Hadoop e MapReduce](#hadoop-e-mapreduce)
- [Spark com Pyspark](#spark-com-pyspark)

# Sprint 9:

Na nona sprint, concentrei-me nas atividades de Modelagem Relacional e Modelagem Dimensional, avançando no desafio proposto. Esta sprint foi marcada pela diversidade de tarefas, priorizando a execução de atividades específicas em detrimento da participação em cursos extensivos

## Tarefa 1: Modelagem Relacional - Normalização

### Criação de Tabelas:

Inicialmente, foram criadas diversas tabelas no banco de dados, cada uma com um nome específico, como "Cliente", "Carro", "Combustivel", "Vendedor" e "Locacao". Cada tabela foi projetada para armazenar informações relacionadas a um aspecto específico dos registros de locação.

### Importação de Dados:

Após a criação das tabelas, foi realizada uma etapa crucial de importação de dados. Nesta fase, os dados foram selecionados da tabela "tb_locacao" com base nas colunas correspondentes e inseridos nas tabelas recém-criadas. Isso incluiu preencher a tabela "Cliente" com informações sobre os clientes, a tabela "Carro" com dados sobre os carros disponíveis, a tabela "Combustivel" com informações sobre o tipo de combustível utilizado, a tabela "Vendedor" com detalhes sobre os vendedores envolvidos e a tabela "Locacao" com registros detalhados sobre cada locação.

## Tarefa 2: Modelagem Dimensional - Criação de Modelo

Inicialmente, foram criadas tabelas de dimensão para armazenar informações essenciais. A tabela DimCliente contém detalhes sobre os clientes, enquanto DimCarro guarda informações sobre os carros e DimVendedor sobre os vendedores. Para popular essas tabelas, os dados foram copiados das tabelas originais usando o comando INSERT INTO, resultando em dimensões bem estruturadas a partir dos dados brutos.

Em seguida, foi criada a tabela de fatos FatoLocacao, registrando informações cruciais sobre as locações de carros, incluindo informações como IDs do cliente, carro e vendedor envolvidos, datas e horários de locação, quantidade e valor diário, entre outros. Chaves estrangeiras foram estabelecidas para garantir uma conexão sólida entre os fatos e as dimensões.

Finalmente, foram criadas visualizações para facilitar o acesso aos dados. A visualização VwFatoLocacao combina informações da tabela FatoLocacao com detalhes das tabelas de dimensão DimCliente, DimCarro e DimVendedor, permitindo consultas mais eficientes. As visualizações VwDimCliente, VwDimCarro e VwDimVendedor fornecem representações diretas das tabelas de dimensão originais, simplificando a consulta dos dados.

## Desafio:

### Parte 3:

Foi criada a camada Trusted no bucket e o Apache Spark foi utilizado para processar os dados da camada Raw Zone, padronizando-os. Os dados processados foram armazenados no Amazon S3, na pasta "trusted," em formato PARQUET. O processamento foi realizado pelo AWS Glue, onde um job no Spark script editor foi desenvolvido para converter os arquivos JSONs da pasta RAW para PARQUET e enviá-los para a pasta Trusted.

### Parte 4:

Foi criado um Crawler no AWS Glue e configurado para rastrear a pasta "trusted" contendo os arquivos no formato PARQUET. O Crawler foi utilizado para criar automaticamente uma tabela no AWS Glue Data Catalog com base nos metadados dos arquivos PARQUET na pasta "trusted."

### Parte 5:

#### Passo 1: Criação do Job

Inicialmente, um novo job foi criado.

#### Passo 2: Seleção de Colunas e Armazenamento

Um código foi desenvolvido para selecionar as colunas de dados relevantes e filtrar apenas os filmes a serem utilizados. Esses filmes foram então enviados para uma pasta criada no bucket de armazenamento.