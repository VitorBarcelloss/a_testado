# Testes unitarios

---

## Objetivo

Testes unitários tem como objetivo homologar o funcionamento de uma função 
única, porém eles acabam sendo muito mais que isso. São de grande ajuda 
na hora de consertar bugs e implementar novas modificações no código, 
por ser um teste de baixo custo, ou seja requer menos tempo e equipe 
para seu desenvolvimento, é um ótimo aliado para desenvolvedores.

## Funcionamento

A implementação de testes unitários é relativamente simples, 
você vai testar uma função sem ter conexão com outras funções do código.
Primeiro separamos o teste em três partes: Arranje, Act e Assert. 
Na primeira parte é onde iremos fazer toda a preparação para os testes,
importar os fixtures, tirar ou colocar algum parametro e assim vai.
Em seguida é a parte em que o teste age, você vai chamar a função, 
vai pegar informações do banco de dados, vai alterar alguma variavel.
Por ultimo vem a parte do assert, que é onde verificamos se o resultado 
gerado de fato bateu com o esperado.

Muito cuidado na hora de escrever os testes, tente sempre ter bem definido 
seu script e suas regras de negócio, para que nenhum detalhe seja perdido no caminho,
e para evitar flake tests.


## Configurações

### pytest.ini
Este arquivo contém as configurações de execução do pytest. Neste exemplo foram utilizads as seguintes configurações.

python_files: Procura testes dentro dos arquivos com esta marcação.

python_functions: Executa o teste nas funções com esta marcação.

testpaths: Uma lista de diretórios que pode conter testes a serem executados.

### conftest.py

Neste arquivo deve ser colocado todas as configurações e arranjos iniciais para os testes.

fixture: Um recurso que permite fornecer dados ou configurar o ambiente que seu teste vai utilizar.