# Comandos Git

## git init
    Inicializa um novo repositório Git localmente no diretório raiz do projeto.

## git add
    Adiciona um arquivo específico ao área de staging.

### git add .
    Adiciona todos os arquivos no projeto ao área de staging.

### git add < nome_do_arquivo>
    Adiciona um arquivo específico ao área de staging.

### git add <fil*>
    Adiciona todos os arquivos que começam com 'fil' ao área de staging.

## git status
    Mostra o status atual do repositório, incluindo arquivos no área de staging, não rastreados e modificados.

## git commit
    Abre um editor de texto no terminal para escrever uma mensagem de commit.

### git commit -m "sua mensagem de commit aqui"
    Adiciona uma mensagem de commit sem abrir o editor de texto.

### git commit -a -m "sua mensagem de commit aqui"
    Adiciona e commita automaticamente arquivos rastreados sem passar pela área de staging.

## git log
    Mostra o histórico de commits do repositório.

### git log -p
    Mostra o histórico de commits com as mudanças em cada commit.

### git log --stat
    Mostra estatísticas sobre as mudanças em cada commit.

## git show <commit-id>
    Mostra as alterações em um commit específico.

## git branch
    Lista todas as branches existentes no repositório.

### git branch < nome_branch>
    Cria uma nova branch com o nome especificado.

### git checkout < nome_branch>
    Muda para a branch especificada.

### git branch -d < nome_branch>
    Deleta a branch especificada.

## git merge < nome_branch>
    Mescla a branch atual com a branch especificada.

## git remote
    Lista todos os repositórios remotos associados ao repositório local.

### git remote -v
    Mostra os URLs de todos os repositórios remotos.

## git push
    Envia as alterações locais para o repositório remoto.

### git push -u origin < nome_branch>
    Envia uma nova branch para o repositório remoto.

## git pull
    Obtém as alterações do repositório remoto e as mescla com a branch local.

## git fetch
    Obtém as alterações do repositório remoto, mas não realiza a mesclagem local.

## git revert HEAD
    Cria um novo commit que desfaz as alterações do último commit.

## git revert < commit-id>
    Cria um novo commit que desfaz as alterações de um commit específico.

## git rebase
    Transfere o trabalho concluído de uma branch para outra.

### git rebase -i master
    Executa o rebase interativamente, permitindo alterações específicas.

## git push -f
    Força um push, sobrescrevendo o histórico remoto. Cuidado ao usar em repositórios compartilhados.

## git remote update
    Baixa alterações do repositório remoto sem mesclá-las automaticamente.

## git push --delete origin < nome_branch>
    Remove uma branch remota.

## git add remote https://repo_here
    Adiciona um repositório remoto ao repositório local.

## git remote show origin
    Fornece informações detalhadas sobre um repositório remoto.

# Nota
Evite utilizar git commit --amend em commits já públicos.

## git checkout -
    Volta para o diretório anterior.

## git checkout ~
    Muda para o diretório home do usuário.

## git checkout < /caminho/do/diretorio>
    Muda para o diretório especificado.

## git diff
    Mostra as mudanças entre o diretório de trabalho e a área de staging.

## git diff < nome_do_arquivo>
    Mostra as mudanças em um arquivo específico.

## git diff --staged
    Mostra as mudanças entre a área de staging e o último commit.

## git add -p
    Abre um prompt para escolher quais alterações serão adicionadas ao área de staging.

## git rm < nome_do_arquivo>
    Remove um arquivo rastreado e prepara a mudança para o próximo commit.

## git mv < nome_antigo> < novo_nome>
    Renomeia ou move um arquivo e prepara a mudança para o próximo commit.

## gitignore
    Cria um arquivo .gitignore para listar os arquivos que devem ser ignorados pelo Git.

## git checkout < nome_do_arquivo>
    Desfaz as mudanças em um arquivo no diretório de trabalho.

## git reset HEAD < nome_do_arquivo>
    Remove um arquivo da área de staging, mantendo as alterações no diretório de trabalho.

## git reset HEAD -p
    Remove interativamente partes específicas de um arquivo da área de staging.

## git commit --amend
    Modifica e adiciona mudanças ao commit mais recente.

## git revert HEAD
    Desfaz o último commit criando um novo commit que reverte as alterações.

## git revert < commit_id>
    Desfaz um commit específico criando um novo commit que reverte as alterações.

## git branch -b < nome_branch>
    Cria e muda imediatamente para uma nova branch.

## git log --graph --oneline
    Mostra o histórico de commits como um gráfico de linhas.

## git log --graph --oneline --all
    Mostra o histórico de commits como um gráfico de linhas para todas as branches.

## git merge --abort
    Aborta uma mesclagem conflitante e reinicia o processo de mesclagem.

## git remote update
    Baixa alterações do repositório remoto sem mesclá-las automaticamente.

## git push -u origin < nome_branch>
    Envia uma nova branch para o repositório remoto e a define como upstream.

## git push --delete origin < nome_branch>
    Remove uma branch remota do repositório remoto.

## git rebase < nome_branch>
    Transfere alterações de uma branch para outra.

### git rebase -i master
    Executa um rebase interativamente permitindo a manipulação do histórico.

## git push -f
    Força um push, substituindo o histórico remoto. Cuidado ao usar em repositórios compartilhados.
