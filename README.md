# 📊 Python API to Database

Projeto em Python que consome dados de uma **API pública**, trata
respostas em **JSON** e armazena as informações em um **banco de dados
MySQL**.

A aplicação permite consultar diferentes endpoints da API de Dados
Abertos da Câmara dos Deputados e salvar os dados localmente para
consulta posterior.

------------------------------------------------------------------------

## 🌐 API Utilizada

**API de Dados Abertos da Câmara dos Deputados**

Documentação oficial:\
https://dadosabertos.camara.leg.br/swagger/api.html

Endpoints utilizados: - `/deputados` - `/partidos` - `/grupos` -
`/frentes`

------------------------------------------------------------------------

## 🛠️ Tecnologias Utilizadas

-   Python 3\
-   MySQL\
-   Biblioteca `requests`\
-   Biblioteca `mysql-connector-python`\
-   Formato de dados: JSON

------------------------------------------------------------------------

## 🧱 Estrutura do Banco de Dados

``` sql
CREATE DATABASE camara_leg_db;
USE camara_leg_db;

CREATE TABLE Deputados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uri VARCHAR(100) UNIQUE NOT NULL,
    nome VARCHAR(55) NOT NULL,
    sigla_partido VARCHAR(55) NOT NULL,
    email VARCHAR(55)
);

CREATE TABLE Partidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sigla VARCHAR(55) NOT NULL,
    nome VARCHAR(55) NOT NULL,
    uri VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE Grupos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uri VARCHAR(100) UNIQUE NOT NULL,
    nome VARCHAR(55) NOT NULL,
    ano_criacao INT
);

CREATE TABLE Frentes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    uri VARCHAR(100) UNIQUE NOT NULL,
    titulo TEXT NOT NULL,
    id_legislativo INT NOT NULL
);
```

------------------------------------------------------------------------

## ▶️ Como Executar o Projeto

``` bash
git clone https://github.com/seu-usuario/python-api-to-db.git
cd python-api-to-db

python -m venv venv
venv\Scripts\activate

pip install requests mysql-connector-python

# Execute o script SQL no MySQL
python program.py
```

------------------------------------------------------------------------

## 🖥️ Funcionamento do Programa

1.  O programa exibe um menu no terminal
2.  O usuário escolhe o tipo de dado
3.  A aplicação consulta a API pública
4.  Os dados são exibidos no console
5.  O usuário pode salvar os dados no banco MySQL

------------------------------------------------------------------------

## 🔒 Boas Práticas Utilizadas

-   Queries parametrizadas
-   Tratamento de valores nulos
-   Chaves únicas para evitar duplicações
-   Código organizado em funções

------------------------------------------------------------------------

## 🚀 Possíveis Melhorias Futuras

-   Tratamento de exceções
-   Implementar UPDATE
-   Relacionamentos entre tabelas
-   Paginação da API
-   Interface gráfica
