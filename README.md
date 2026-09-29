# 🤖 Automação de Cadastro de Produtos com Python

Automação que faz login em um sistema web e cadastra, um a um, todos os produtos de uma base de dados (`produtos.csv`), simulando o teclado e o mouse com **PyAutoGUI** e lendo os dados com **Pandas**.

> Projeto desenvolvido durante o Intensivão de Python da Hashtag Treinamentos, com foco em automação de tarefas repetitivas (RPA).

---

## 📌 Sobre o projeto

Cadastrar centenas de produtos manualmente é lento e sujeito a erros. Este script automatiza todo o processo:

1. Abre o navegador (Microsoft Edge) e acessa o sistema da empresa.
2. Faz login no site.
3. Lê a base de produtos a partir de um arquivo CSV.
4. Preenche o formulário de cadastro de cada produto e clica em enviar.
5. Repete o processo até o fim da lista (293 produtos na base de exemplo).

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/): controle de mouse e teclado
- [Pandas](https://pandas.pydata.org/): leitura e manipulação da base de dados
- [openpyxl](https://openpyxl.readthedocs.io/): suporte a arquivos Excel (opcional)

## 📁 Estrutura do repositório

```
.
├── codigo.py       # Script principal da automação
├── auxiliar.py     # Utilitário para descobrir coordenadas (x, y) na tela
├── produtos.csv    # Base de dados com os produtos a cadastrar
└── README.md
```

## 🗂️ Formato da base de dados

O arquivo `produtos.csv` deve conter as seguintes colunas:

| Coluna           | Descrição                              | Exemplo            |
|------------------|----------------------------------------|--------------------|
| `codigo`         | Código único do produto                | `MOLO000251`       |
| `marca`          | Marca do produto                       | `Logitech`         |
| `tipo`           | Tipo do produto                        | `Mouse`            |
| `categoria`      | Número da categoria                    | `1`                |
| `preco_unitario` | Preço de venda                         | `25.95`            |
| `custo`          | Custo do produto                       | `6.50`             |
| `obs`            | Observações (opcional, pode ser vazio) | `Conferir estoque` |

## ⚙️ Como funciona

O fluxo do `codigo.py` segue estes passos:

1. **Abrir o sistema:** aperta a tecla `Win`, digita "edge", abre o navegador e acessa o link de login.
2. **Login:** clica no campo de e-mail, preenche e-mail e senha usando `Tab` para navegar entre os campos e `Enter` para entrar.
3. **Carregar a base:** lê o `produtos.csv` com `pandas.read_csv`.
4. **Cadastrar produtos:** para cada linha da tabela, clica no campo *código*, preenche todos os campos navegando com `Tab` e envia o formulário com `Enter`. O campo `obs` só é preenchido quando não está vazio.
5. **Finalizar:** rola a página de volta ao topo.

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instale as dependências

```bash
pip install pyautogui pandas openpyxl
```

### 3. Ajuste as coordenadas para a sua tela

As posições de clique (`x`, `y`) do `codigo.py` foram capturadas em uma tela específica e provavelmente vão precisar de ajuste no seu computador.

Rode o script auxiliar, posicione o mouse sobre o local desejado em até 5 segundos e anote as coordenadas exibidas no terminal:

```bash
python auxiliar.py
```

Depois, atualize no `codigo.py` os cliques correspondentes:

```python
pyautogui.click(x=1082, y=34)   # campo de login/e-mail
pyautogui.click(x=123, y=374)   # campo "código" do formulário de cadastro
```

### 4. Configure e execute

Edite as variáveis `link`, `email` e a senha no `codigo.py` com os seus dados e rode:

```bash
python codigo.py
```

> ⚠️ **Durante a execução, não mexa no mouse nem no teclado.** O PyAutoGUI está controlando os dois. Para interromper em caso de emergência, mova o mouse rapidamente para um dos cantos da tela (*fail-safe* do PyAutoGUI).

## ⏱️ Ajustes de tempo

- `pyautogui.PAUSE = 1`: pausa de 1 segundo entre cada comando.
- `time.sleep(3)` e `time.sleep(4)`: esperas para o carregamento das páginas. Se a sua internet ou o site forem mais lentos, aumente esses valores.

## 🔒 Boas práticas

- **Não versione senhas reais.** Use variáveis de ambiente ou um arquivo `.env` (com `python-dotenv`) em vez de deixar credenciais no código.
- Feche outras janelas antes de rodar, para que o foco fique sempre no navegador.
- Teste primeiro com poucas linhas do CSV antes de rodar a base completa.

## 💡 Possíveis melhorias

- Usar variáveis de ambiente para e-mail e senha.
- Substituir cliques por coordenadas fixas por localização de imagens (`pyautogui.locateOnScreen`) ou por Selenium/Playwright, tornando a automação mais robusta.
- Adicionar tratamento de erros e log dos produtos cadastrados.
- Trocar as esperas fixas (`time.sleep`) por esperas dinâmicas.

## 📄 Licença

Este projeto é de uso educacional. Sinta-se à vontade para estudar, adaptar e melhorar.

---

Feito com 🐍 e automação.
