# Módulo 04: Estruturas de Repetição (While e Acumuladores) 🔄

Este módulo introduz o conceito de loops infinitos controlados, persistência de estado em memória e validação de dados em tempo real.

## 🚀 Microserviços Desenvolvidos

### 1. Menu de Navegação Interativo (`menu_interativo.py`)
* **Problema resolvido:** Criação de uma interface de terminal (CLI) que se mantém ativa aguardando comandos do usuário, simulando a base de sistemas de gestão.
* **Habilidades aplicadas:** Loop `while` com controle de fluxo aninhado (`if/elif/else`) e tratamento de indentação para isolamento de escopo.

### 2. Motor de Acumulação Financeira (`somador_gastos.py`)
* **Problema resolvido:** Algoritmo de contabilidade contínua que soma valores dinâmicos em tempo real (Running Total) até que uma condição de parada (Valor Sentinela) seja acionada.
* **Habilidades aplicadas:** Uso de variáveis acumuladoras e inicialização de estado lógico.

### 3. Rastreador de Faturamento Freelancer (`rastreador_freela.py`)
* **Problema resolvido:** Sistema de gestão de tempo (Time Tracking) e faturamento contínuo para profissionais independentes.
* **Habilidades aplicadas:** Acumulação de dados em ponto flutuante (`float`), lógica de faturamento baseada em Billable Hours e encerramento de escopo com processamento final de fatura.

### 4. Sistema de Controle de Orçamento (`controle_orcamento.py`)
* **Problema resolvido:** Prevenção de estouro de caixa em projetos, bloqueando transações que excedem o saldo disponível.
* **Habilidades aplicadas:** Fusão de laços de repetição (`while`) com estruturas condicionais defensivas, garantindo validação de regras de negócio estritas antes da execução de cálculos matemáticos.