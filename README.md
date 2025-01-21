# Automação de Arquivos

Este repositório contém um script Python que automatiza o processo de **gerenciamento de arquivos** entre duas pastas: uma pasta de **origem** e uma pasta de **destino**. O script é projetado para listar, mover, remover e gerar logs detalhados das ações realizadas nos arquivos, garantindo uma organização eficiente e sem erros.

## 🚀 Objetivo

O principal objetivo desse projeto é automatizar a organização e limpeza de arquivos em diretórios, removendo arquivos antigos e fazendo backups de forma simples e eficiente.

## 📋 Como Funciona

### Passo 1: Listar os Arquivos

O primeiro passo do script é listar todos os arquivos da pasta de **origem**. A função percorre a pasta e coleta algumas informações importantes dos arquivos, como:
- Nome
- Tamanho
- Data de Criação
- Data de Modificação

Esses dados são salvos em um arquivo de **log**, criando um histórico completo da pasta de origem.

### Passo 2: Gerenciar os Arquivos

Na função `gerenciar_arquivos`, o script realiza duas ações principais:
- **Remover arquivos antigos**: Caso algum arquivo tenha mais de **3 dias** de criação, ele é automaticamente removido.
- **Copiar arquivos novos**: Arquivos que não têm mais de 3 dias de criação são copiados para a pasta de destino. A cópia é feita de forma que **preserva as datas de criação e modificação** dos arquivos.

### Passo 3: Gerar o Log de Cópias

Ao final do processo, o script gera um **log detalhado** dos arquivos que foram copiados para a pasta de destino, incluindo suas informações, como tamanho e datas de criação e modificação.

### Detalhes Extras

Antes de executar qualquer operação, o script verifica se as pastas de **origem** e **destino** existem. Caso elas não existam, o próprio script cria as pastas automaticamente, garantindo que o processo funcione sem erros, mesmo que as pastas ainda não tenham sido criadas manualmente.

## ⚙️ Como Usar

### 1. Clone o Repositório

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/mgabriiella/automacao-arquivos.git
