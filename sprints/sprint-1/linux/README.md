# Comandos Linux

## cd
    O comando cd é utilizado para mudar de diretório no sistema de arquivos.

### cd -
    Volta para o diretório anterior.

### cd ~
    Muda para o diretório home do usuário.

### cd </caminho/do/diretorio>
    Muda para o diretório especificado.

## ls
    O comando ls lista os arquivos e diretórios no diretório atual.

### ls -a
    Lista todos os arquivos, incluindo os ocultos.

### ls -l
    Apresenta a listagem em formato detalhado, exibindo permissões, proprietário, grupo, tamanho, data de modificação e nome do arquivo.

### ls -lh
    Igual ao -l, mas mostra o tamanho dos arquivos de forma legível (ex: KB, MB).

### ls -R
    Lista recursivamente, exibindo também os subdiretórios.

## clear
    O comando clear limpa a tela do terminal.

## cat
    O comando cat é usado para concatenar e exibir o conteúdo de arquivos.

### cat arquivo.txt
    Exibe o conteúdo do arquivo.txt no terminal.

## touch
    O comando touch cria arquivos vazios ou atualiza o carimbo de data e hora de arquivos existentes.

### touch novo_arquivo.txt
    Cria um novo arquivo chamado novo_arquivo.txt.

### man
    O comando man exibe o manual do usuário para outros comandos.

### man ls
    Abre o manual para o comando ls.

## mkdir
    O comando mkdir é usado para criar novos diretórios.

### mkdir novo_diretorio
    Cria um novo diretório chamado novo_diretorio.

## rm
    O comando rm remove arquivos ou diretórios.

### rm -r diretorio
    Remove um diretório e seu conteúdo de forma recursiva.

### rmdir
    O comando rmdir remove diretórios vazios.

## cp
    O comando cp copia arquivos ou diretórios.

## cp arquivo.txt destino/
    Copia o arquivo.txt para o diretório destino.

## mv
    O comando mv move ou renomeia arquivos ou diretórios.

### mv arquivo.txt novo_nome.txt
    Renomeia o arquivo.txt para novo_nome.txt.

## pwd
    O comando pwd exibe o diretório de trabalho atual.

## head
    O comando head exibe as primeiras linhas de um arquivo.

### head -n 10 arquivo.txt
    Exibe as primeiras 10 linhas do arquivo.txt.

## tail
    O comando tail exibe as últimas linhas de um arquivo.

### tail -n 20 arquivo.txt
    Exibe as últimas 20 linhas do arquivo.txt.

## grep
    O comando grep procura padrões em arquivos.

### grep "palavra" arquivo.txt
    Procura a palavra no arquivo.txt.

## find
    O comando find procura por arquivos e diretórios.

### find < /caminho> -name "arquivo.txt"
    Procura pelo arquivo.txt no caminho especificado.

## locate
    O comando locate localiza arquivos no sistema.

### locate arquivo.txt
    Localiza o arquivo.txt no sistema.

## !!
    O comando !! executa o último comando digitado.

# Adicionar, Deletar e Editar Usuários

## sudo adduser nome_do_usuario
    O comando adduser é utilizado para adicionar novos usuários ao sistema.

## sudo deluser nome_do_usuario
    O comando deluser é usado para deletar usuários do sistema.

## sudo usermod -G novo_grupo nome_do_usuario
    O comando usermod permite a modificação de atributos de usuários, incluindo a adição ou remoção de grupos.

# Criar, Deletar e Mover Grupos

## addgroup
    O comando addgroup é empregado para criar novos grupos no sistema.

```bash
sudo addgroup nome_do_grupo
```

## delgroup
    O comando delgroup é utilizado para deletar grupos existentes.

```bash
sudo usermod -G novo_grupo nome_do_usuario
```

## usermod -G
    O comando usermod -G permite mover usuários entre grupos.

```bash
sudo usermod -G novo_grupo nome_do_usuario
```

# Permissão Numérica
    As permissões numéricas são representadas por três dígitos (de 0 a 7) e concedem diferentes níveis de acesso para proprietário, grupo e outros.

- 4 (read): Permissão de leitura.
- 2 (write): Permissão de escrita.
- 1 (execute): Permissão de execução.

## chmod 754 arquivo.txt

- Proprietário tem permissões de leitura, escrita e execução (7).
- Grupo tem permissão de leitura e execução (5).
- Outros têm permissão de leitura (4).

# Permissão Simbólica
    As permissões simbólicas utilizam letras para representar as permissões.

- r (read): Permissão de leitura.
- w (write): Permissão de escrita.
- x (execute): Permissão de execução.

## chmod u=rw, g=r, o=r arquivo.txt

- Proprietário tem permissões de leitura e escrita.
- Grupo tem permissão de leitura.
- Outros têm permissão de leitura.

# Compactar Arquivos
## tar
    O comando tar é usado para criar, visualizar e extrair arquivos compactados.

### tar -cvf arquivo.tar <pasta/ >
    Este comando cria um arquivo compactado chamado arquivo.tar da pasta especificada.

## zip
    O comando zip compacta arquivos em um formato zip.

### zip arquivo.zip arquivo.txt
    Este comando cria um arquivo zip chamado arquivo.zip contendo arquivo.txt.