# Projeto Job Insights 👮🏻‍♂️👩🏼‍🚒👷🏾

Consiste em uma aplicação web desenvolvida com Flask contendo informações a partir da análise de um conjunto de dados sobre empregos.

### Funções e Testes criados

|--|--|--|

### Instruções

- Para rodar a aplicação localmente e os testes, realize o clone do projeto e utilize os comandos a seguir:

```
Para instalar as dependências e iniciar as aplicações:
<-- na raiz do projeto -->
python3 -m venv .venv // para criar o ambiente virtual
source .venv/bin/activate // para ativar o ambiente virtual
python3 -m pip install -r dev-requirements.txt // instalação das dependências

Para inicializar a aplicação criada com Flask:
<-- na raiz do projeto -->
flask run // iniciar a aplicação
CTRL+C // para parar a aplicação

Aplicação estará disponível na url: http://127.0.0.1:5000/

Para rodar todos os testes:
<-- na raiz do projeto -->
python3 -m pytest

PAra rodar os testes individualmente:
<-- na raiz do projeto -->
python3 -m pytest -k test_brazilian_jobs
python3 -m pytest -k test_counter
python3 -m pytest -k test_sort_by_criteria
```
<br />

### Demonstração

<br />
<p align="center">
  <img src="https://github.com/guilherme-ac-fernandes/ng-financial-app/blob/main/images/transactions.png" alt="NG_Cash Página Inicial - Demostração"/>
</p>
