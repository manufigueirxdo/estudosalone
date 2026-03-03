# Módulo 02: Condicionais e Arquitetura Defensiva 🛡️

Este módulo foca na criação de regras de negócios dinâmicas e na proteção do sistema contra entradas inválidas de usuários.

## 🚀 Microserviços Desenvolvidos

### 1. Validador de Bonificação (`validador_bonificacao.py`)
* **Problema resolvido:** Sistema de RH que calcula bônus de funcionários (10% ou 20%) dependendo da faixa salarial.
* **Habilidades aplicadas:** Arquitetura defensiva. O sistema possui uma trava de segurança (`if` inicial) que impede o cálculo sobre salários zerados ou negativos, evitando quebras (bugs) no fluxo financeiro da empresa.

### 2. Motor de Retenção de Impostos (`calculadora_imposto.py`)
* **Problema resolvido:** Algoritmo de dedução fiscal com múltiplas faixas de renda (Isento, 10% e 20%).
* **Habilidades aplicadas:** Controle de fluxo avançado (`if/elif/else`), operadores lógicos (`and`) e aplicação do princípio DRY (Don't Repeat Yourself) para manter o código limpo e escalável.

### 3. Calculadora de Frete Dinâmico (`calculadora_frete_dinamico.py`)
* **Problema resolvido:** Motor de e-commerce que calcula frete baseado no valor do carrinho e na distância, aplicando regras de isenção e taxas fixas.
* **Habilidades aplicadas:** Controle de fluxo em cascata (Top-Down), otimização de condicionais eliminando verificações redundantes e uso de arquitetura lógica limpa.