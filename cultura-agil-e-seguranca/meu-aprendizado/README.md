# Meu Aprendizado

Nessa sprint, pude conhecer algo novo e essencial que eu apenas ouvia falar, seja em requisitos de vagas ou em outros contextos. É muito importante perceber que a indústria de software é mais do que apenas produzir software. Existe toda uma filosofia por trás disso para garantir que tudo ocorra conforme o planejado e com flexibilidade. Tambem conheci a parte de security, confesso que não tenho muito interesse nessa parte mas foi interessante saber o essencial para ter um aplicação protegida e blindada contra ataques.


## Índice

- [Cultura Àgil](#cultura-agil)
- [Segurança](#seguranca)


## Cultura Àgil

### Manifesto Ágil

A importância do Manifesto Ágil reside em sua capacidade de proporcionar um ambiente que favorece a entrega de valor ao cliente de maneira rápida e eficiente. Ele nos lembra que, em um mundo onde a mudança é constante, a agilidade e a flexibilidade são essenciais para o sucesso no desenvolvimento de software.

- Indivíduos e interações mais que processos e ferramentas:

Aprendi que o foco deve ser nas pessoas e na comunicação entre elas. Processos e ferramentas são importantes, mas a colaboração efetiva é o cerne do desenvolvimento ágil.

- Software em funcionamento mais que documentação abrangente:

Entendi a importância de ter um produto que realmente funcione. Isso não significa que a documentação não seja necessária, mas o código executável é a medida principal de progresso.

- Colaboração com o cliente mais que negociação de contratos:

Aprendi que envolver o cliente de forma contínua e colaborativa é essencial. A abordagem ágil preza por responder às mudanças e atender às necessidades do cliente de maneira rápida e flexível.

- Responder a mudanças mais que seguir um plano:

Compreendi que a adaptação a mudanças é mais valiosa do que aderir rigidamente a um plano. Isso significa estar aberto a ajustes contínuos com base no feedback e nas mudanças nas condições do projeto.

---

### Scrum

- **Estrutura em Sprints:** Desenvolvimento dividido em iterações fixas chamadas sprints, geralmente de 2 a 4 semanas.
- **Papéis Definidos:** Scrum Master (facilitador), Product Owner (responsável pelos requisitos), Time de Desenvolvimento.
- **Reuniões Regulares:** Daily Scrum (reunião diária de 15 minutos), Sprint Review (revisão do trabalho concluído), Sprint Planning (planejamento da próxima sprint).
- **Artefatos:** Product Backlog (lista de requisitos), Sprint Backlog (tarefas para a sprint), Incremento (versão funcional do software ao final da sprint).

---

### Kanban

- **Visualização do Fluxo de Trabalho:** Uso de quadro visual para representar o fluxo de trabalho, com colunas que representam diferentes etapas.
- **Limitação de WIP:** Restrição do trabalho em progresso para otimizar o fluxo e evitar gargalos.
- **Adaptação Contínua:** Foco na melhoria contínua e na eficiência do processo.
- **Sem Iterações Fixas:** Não utiliza sprints fixas, permitindo uma abordagem mais flexível.

---

### Lean

- **Eliminação de Desperdícios:** Identificação e eliminação de atividades que não agregam valor.
- **Melhoria Contínua:** Ênfase na busca constante por eficiência e qualidade.
- **Entrega de Valor ao Cliente:** Priorização da entrega de valor ao cliente, reduzindo o tempo de desenvolvimento.
- **Kanban como Ferramenta Lean:** O Kanban é frequentemente utilizado como uma ferramenta dentro da filosofia Lean.

---

### Trello

- **Boards e Cards:** Organização do trabalho em boards (quadros) que representam projetos, e cards (cartões) que representam tarefas.
- **Colaboração Visual:** Facilita a colaboração e comunicação visual entre membros da equipe.
- **Listas e Etapas:** Cards movem-se através de listas, representando diferentes etapas do processo.
**Customização:** Permite a personalização para atender às necessidades específicas da equipe.

---

## Segurança

A segurança em aplicações web é crítica devido ao crescente aumento das ameaças digitais. Proteger dados sensíveis, a integridade das aplicações e a confiança dos usuários são elementos essenciais para o sucesso e a reputação de qualquer sistema online. A implementação eficaz de medidas de segurança não apenas protege contra ataques maliciosos, mas também fortalece a resiliência da aplicação diante de ameaças constantes.

### Princípios da Segurança em Aplicações Web:

- **Princípio do Menor Privilégio:** Limitar acessos aos mínimos necessários reduz a superfície de ataque.
- **Segurança em Profundidade:** Adotar camadas de defesa múltiplas para fortalecer a segurança global.
- **Validação de Dados:** Verificar rigorosamente dados de entrada para prevenir ataques de injeção.
- **Autenticação e Autorização:** Garantir que apenas usuários autorizados tenham acesso a funcionalidades e dados.
- **Monitoramento e Registro:** Detectar precocemente atividades suspeitas ou violações de segurança.
- **Atualizações e Patches:** Manter sistemas e software atualizados com as últimas correções de segurança.

### Testes de Vulnerabilidade:

- **Injection Attacks:**
  - **SQL Injection:** Manipulação maliciosa de consultas SQL.
  - **XSS (Cross-Site Scripting):** Inserção de scripts maliciosos no lado do cliente.
- **Cross-Site Request Forgery (CSRF):**
  - Exploração da confiança em solicitações não autorizadas.

### Métodos para Descobrir Vulnerabilidades:

- **Testes de Penetração:** Simulação de ataques controlados.
- **Scanner de Vulnerabilidades:** Ferramentas automatizadas para identificar vulnerabilidades.
- **Auditorias de Código:** Revisão manual do código-fonte.
- **Monitoramento de Tráfego:** Análise contínua do tráfego.

### Formas de Proteção:

- **Filtragem de Entrada:** Rigorosa validação e filtragem de dados para prevenir injeções.
- **Uso de Parâmetros Preparados:** Consultas preparadas para evitar SQL Injection.
- **Utilização de HTTPS:** Criptografia do tráfego para proteger a comunicação.
- **Proteção contra XSS:** Políticas de segurança, sanitização e codificação adequada.
- **Controle de Sessão:** Uso de tokens e práticas seguras para evitar CSRF e ataques de sessão.
- **Firewalls de Aplicação Web (WAF):** Defesa contra ameaças web conhecidas.
- **Atualizações Regulares:** Manutenção atualizada para corrigir vulnerabilidades conhecidas.
