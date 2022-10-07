# Backend Challenge 20220626

## Product Scraping - Objetivo
Desenvolver uma REST API que utilizará os dados da Open Food Facts um banco de dados aberto com informçaões nutricionais de vários produtos.

### Linguagens, Frameworks e Biblotecas usadas
- Python
- Django
- Djangorestframework
- Pymysql
- Requests
- BeautfulSoup
- mysql-client

### O Projeto
Este projeto consiste em um banco de dados Mysql e um sistema de atualiazação.

O sistema de atualização realiza um scraping diário na página [Open Food Facts](https://world.openfoodfacts.org/) e sincroniza essas informações ao banco de dados.

### Rodar o programa

Foi escrito funções em python para testar os 3 endpoints da API.

Todos os testes foram feitos em ambiente de desenvolvimento.

Para rodar o programa é necessário ter o pycharm ou Vscode e o Ptyhon3 instalado instalado na máquina. Todas a bibliotecas estão armazenadas no ambinete virtual, sendo assim não é necessário instala-los novamente.

O arquivo requirements.txt tem todos as bibliotecas usadas no desenvonvilmento de projeto.

O principal foco na construção do programa foi o backend. 

Para atualizar (sincronizar) os produtos no banco de dados é necessário rodar o arquivo main.py. Antes de rodar, certifique-se que o ambiente virtual está ativo e que o tem o servidor conectado. 

No desenvolvimento foi usado o wampserver como servidor para conectar o banco de dados.

Para vizualizar as informações dos produtos na API é necessário seguir os seguintes passos:
- Rodar no trminal a seguinte linha no terminal: py manage.py runserver
- Acessar o serviço em  http://127.0.0.1:8000/
- Exibir as páginas de acordo com os endpoints

Os endpoints são:
- `GET /`: Retornar um Status: 200 e uma Mensagem "Fullstack Challenge 20201026"
- `GET /products/:code`: Obter a informação somente de um produto;
- `GET /products`: Listar todos os produtos da base de dados, utilizar o sistema de paginação para não sobrecarregar a `REQUEST`.
- `GET /documentations`: Página de documentação.

Foi utilizado o sistema de Paginação para exibir na interface da API 10 produtos por página. Para exibir outras páginas informa o seguinte caminho: http://127.0.0.1:8000/products/?page=numero_da_pagina

Número da página recebe um valor númerico inteiro.

## Vídeo de apresentação do projeto
https://www.loom.com/share/2b451ce5536b438f8429a74f23bc6872
