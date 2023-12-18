# Meu Aprendizado

Como esse contéudo funciona mais como uma ferramenta, não tive muitas opções de projetos usando apenas as tecnologias dessa Sprint, mas eu utilizo Git e Github constantemente como poder ver no meu perfil do Github

## Índice

- [Linux](#linux)
- [Git](#git)
- [Github](#github)

## Linux

Eu utilizei Linux por 1 ano no meu notebook (Zorin OS, derivado do Ubuntu), aonde eu pude aprender alguns comandos indispensaveis durante esse tempo então a parte de Linux foi um pouco trnaquila, mas alguns pontos eu não sabia então decidi reforçar.

### Permissões

Um ponto chave que achei necessario dar uma atenção maior são as permissões, e essa imagem deixa bem claro de como elas funcionam no Linux:

<div align=center>

![Permissões](https://pplware.sapo.pt/wp-content/images/imagem_permissoes_linux_03.jpg)

</div>

#### Nomes

- u refere-se ao proprietário (user)
- g refere-se ao grupo (group)
- o refere-se a outros (others)

#### Permissões

- r ou 4 é para leitura
- w ou 2 é para escrita
- x ou 1 é para execução

Você pode modificar as permissões usando comandos como `chmod`. Por exemplo, para conceder permissões de **leitura**, **escrita** e **execução** ao `proprietário`, **leitura** e **execução** para o grupo, e apenas **leitura** para os `outros` você usaria o comando:

```bash
chmod 754 arquivo
```

Ou também poderia ser representado diretamente pelas letras

```bash
chmod u=rwx,g=rx,o=r arquivo
```


### Gerenciamento de Pacotes no Linux

O Linux utiliza sistemas de gerenciamento de pacotes para facilitar a instalação, atualização e remoção de software. A ferramenta de gerenciamento de pacotes pode variar de acordo com a distribuição Linux utilizada.

#### Atualizar Lista de Pacotes:

```bash
sudo apt update
```

Este comando atualiza a lista de pacotes disponíveis.

#### Instalar um Novo Software:

```bash
sudo apt install nome-do-pacote
```

Substitua "nome-do-pacote" pelo nome real do pacote que você deseja instalar.

#### Atualizar Todos os Pacotes Instalados:

```bash
sudo apt upgrade
```

Este comando atualiza todos os pacotes instalados no sistema.

#### Remover um Software:

```bash
sudo apt remove nome-do-pacote
```

## Git

Eu já utilizo Git a um bom tempo, é uma ferramente essencial para desenvolvimento nos meus projetos, aonde posso criar versões, testar commits e criar branchs separadas para desenvolvimento, então eu foquei mais na parte de reverter alterações que era onde eu precisava de mais foco

### Desfazendo Alterações

#### Desfazer `git add`:

Quando se adiciona ao índice (`git add`) sem querer, você pode remover essas alterações do índice utilizando o seguinte comando:

```bash
git reset
```

Este comando desfaz a preparação para o commit, mantendo as alterações nos seus arquivos de trabalho.

#### Desfazer Alterações Locais Não Commitadas:

Se você modificou arquivos e deseja desfazer essas alterações não commitadas, utilize o seguinte comando:

```bash
git checkout -- nome-do-arquivo
```

Isso descarta as alterações locais no arquivo especificado.

### Revertendo Commits

#### Desfazer Último Commit (Local):

Para desfazer o último commit, mantendo as alterações locais, pode-se usar:

```bash
git reset HEAD^
```

Este comando move a branch de volta para o commit anterior, mantendo as alterações locais não commitadas.

Desfazer Último Commit (Local e Remoto):

Quando o commit já esta no repositorio remoto, é melhor usar:

```bash
git reset HEAD^ --hard
```

Este comando reverterá as alterações locais para o commit anterior e as refletirá no repositório remoto na próxima vez que você fizer `push`.

Desfazer Commit Específico (Local):

Para desfazer um commit específico mantendo as alterações locais:

```bash
git reset <hash-do-commit>
```

Este comando move a branch de volta para o commit especificado, mantendo as alterações locais.

Desfazer Commit Específico (Local e Remoto):

Se você deseja desfazer um commit específico e já o compartilhou, use:

```bash
git reset <hash-do-commit> --hard
```

Este comando reverterá as alterações locais para o commit especificado e as refletirá no repositório remoto na próxima vez que você fizer `push`.

### Estratégias Avançadas

Reescrevendo Histórico:

Se for necessário reescrever o histórico (por exemplo, para remover um commit específico), use com cautela:

```bash
git rebase -i HEAD~n
```

Isso abrirá uma interface interativa onde você pode escolher como manipular os commits.
